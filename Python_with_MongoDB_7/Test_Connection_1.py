import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["DataBaseOne"]
mycol = mydb["Employees"]

mydata = {"name":"Rudrika","city":"BVN"}
x=mycol.insert_one(mydata)

mydblist = myclient.list_database_names()
print(mydblist)

print(mydb.list_collection_names())

if "Employees" in mydb.list_collection_names():
    print("Database connect successfully")

print(x)