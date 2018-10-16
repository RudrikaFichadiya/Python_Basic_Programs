import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["DataBaseOne"]
mycol = mydb["Employees"]
print("Searching data from Employees Table")
print("*" * 20)


'''Only returns names  list from table
 Employees '''
for n in mycol.find({},{"_id": 0, "name": "Rudrika"}):
    print(n)

'''The below for loop will display full table data
with name, id, and city with respective column name'''
for i in mycol.find():
    print("_" * 80)
    print(i)

