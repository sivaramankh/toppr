import pymongo
import csv

client = pymongo.MongoClient('mongodb://localhost:28017/')

file_path = r'/home/siva/toppr_files/battles.csv'
dict_items = []

with open(file_path, 'r') as open_file:
    
    csv_reader = csv.DictReader(open_file)
    
    for item in csv_reader:
        for key in list(item.keys()):
            
            if item[key] != "":
                try:
                    item[key] = int(item[key])
                except:
                    continue
                
            else:
                del item[key]
                
        dict_items.append(item)
        
    
db = client.got_battles

result = db.battle_col.insert_many(dict_items)

print(len(result.inserted_ids))
    
