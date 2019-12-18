import pymongo
from pymongo import MongoClient
#why there is a 'i=0' ? .....lazy
i = 0
while i < 1:
        #connect to two mongodb instances
        conn1 = MongoClient('mongodb://127.0.0.1:27017')
        conn2 = MongoClient('mongodb://127.0.0.1:27917')
        #get datalist from source mongodb
        dblist = conn1.list_database_names()
        #compare numbers of every collection between mongodb instances
        for db in dblist:
                collist = conn1[db].list_collection_names()
                for coll in collist:
                        numc1 = conn1[db][coll].find().count()
                        numc2 = conn2[db][coll].find().count()
                        if numc1 != numc2:
                                print "db: %20s   |   collection: %40s   |   num1: %20d   |   num2: %20d" % (db,coll,numc1,numc2)

        i+=1
