import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["DataBaseOne"]
mycol = mydb["Employees"]
mydata = {"name": "ABC", "city": "ABD"}
x = mycol.insert_one(mydata)
print(x.inserted_id)
mydatamul = [
    {"name": "XYZ", "city": "BRD"},
    {"name": "DVL", "city": "SRT"},
    {"name": "RTY", "city": "RKT"},
    {"name": "EFT", "city": "BHJ"},
    {"name": "JKL", "city": "BVN"}]
y = mycol.insert_many(mydatamul)
print(y.inserted_ids)
datawithid = [
    {"_id": 11, "name": "SAN", "city": "AMD"},
    {"_id": 12, "name": "VIC", "city": "JNG"},
    {"_id": 13, "name": "BTR", "city": "JMR"},
    {"_id": 14, "name": "WIL", "city": "SDR"},
    {"_id": 15, "name": "CHK", "city": "CHR"},
    {"_id": 16, "name": "VLA", "city": "NYK"}]

z = mycol.insert_many(datawithid)
print(z.inserted_ids)