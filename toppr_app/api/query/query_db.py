import pymongo
from toppr_app import MONGODB_HOST, MONGODB_DB, MONGODB_COL


def query(parameters):
    """Function for querying the MongoDB database using the supplied parameters.
    :param parameters: Supply parameters as dictionary
    Returns a list"""

    client = pymongo.MongoClient(MONGODB_HOST)
    db = client[MONGODB_DB]

    if not bool(parameters):
        result = [item for item in db[MONGODB_COL].find({}, {'_id': False})]

    else:
        query_term = {}
        for key, value in parameters.items():
            query_term[key] = { "$in" : value }

        result = [ item for item in db[MONGODB_COL].find(query_term, {'_id': False})]


    return result
