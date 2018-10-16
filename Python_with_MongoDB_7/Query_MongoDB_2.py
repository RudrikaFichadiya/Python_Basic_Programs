import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["DataBaseOne"]
mycol = mydb["Employees"]

myquery = {"city": "BVN"}
x = mycol.find(myquery)

for i in x:
    print(i)
