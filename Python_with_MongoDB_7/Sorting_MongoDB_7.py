import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["DataBaseOne"]
mycol = mydb["Empolyees3"]

datains = {"_id": 1001, "name": "EMP1", "city": "BVN", "email": "emp1@email.com", "salary": "33,000"}
x = mycol.insert_one(datains)
print(x.inserted_id)

multipledata = [
    {"_id": 1002, "name": "EMP2", "city": "AMD", "email": "emp2@email.com", "salary": "31,000"},
    {"_id": 1003, "name": "EMP3", "city": "JNG", "email": "emp3@email.com", "salary": "30,000"},
    {"_id": 1004, "name": "EMP4", "city": "JMR", "email": "emp4@email.com", "salary": "35,000"},
    {"_id": 1005, "name": "EMP5", "city": "SDR", "email": "emp5@email.com", "salary": "39,000"},
    {"_id": 1006, "name": "EMP6", "city": "CHR", "email": "emp6@email.com", "salary": "32,000"},
    {"_id": 1007, "name": "EMP7", "city": "NYK", "email": "emp7@email.com", "salary": "36,000"}]

z = mycol.insert_many(multipledata)
print(z.inserted_ids)
''' 1 for ascending order
 and -1 for descending order '''

datains = mycol.find({}, {"_id": 0}).sort("city", 1)

for i in datains:
    print(i)