from collections import defaultdict

def parser(req_parameters):
    """Helper function for converting dictionary from flask request to normal dictionary.
    :param req_parameters: ImmutableMultiDict
    Returns dictionary"""

    parameters = {}

    for item in req_parameters:

        if req_parameters.getlist(item) != ['']:

            try:
                parameters[item] = [int(i) for i in req_parameters.getlist(item)]
            except:
                parameters[item] = req_parameters.getlist(item)

    return parameters
