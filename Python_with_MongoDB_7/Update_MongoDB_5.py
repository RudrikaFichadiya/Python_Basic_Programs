import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["DataBaseOne"]
mycol = mydb["Employees2"]

# Updation operation, where id = 1
mycol.insert_one({"_id": 1, "name": "TLN", "city": "BVN"})
# above data inserted, so we can perform update on inserted data
# _id inside protected access ("_" for declaring a variable as a protected type)
# we've saved name=TLN on id=1
query1 = {"name":"TLN"}
query2 = {"$set" :{"name":"RHF"}}
# TLN will be replaced with RHF after executing update_one() method
updatedata = mycol.update_one(query1, query2)
print(updatedata)
