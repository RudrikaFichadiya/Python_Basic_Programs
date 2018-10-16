import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["DataBaseOne"]
mycol = mydb["Employees2"]
# insert data for delete
mycol.insert_one({"_id": 9, "name": "ELN", "city": "SRT"})
mycol.insert_one({"_id": 10, "name": "JCS", "city": "LNM"})
query = {"city": "SRT"}
d = mycol.delete_one(query)

for x in mycol.find():
    print(x)
print("*" * 20)
mycol.insert_one({"_id": 21, "name": "BLY", "city": "VDR"})
mycol.insert_one({"_id": 12, "name": "Jolly", "city": "ABD"})
myqeyry={"city":{"$regex": "^A"}}
delete = mycol.delete_many(myqeyry)

print(delete.deleted_count,"documents deleted")
#delte all
print("*" * 20)
delete = mycol.delete_many({})
print(delete.deleted_count,"documents deleted")