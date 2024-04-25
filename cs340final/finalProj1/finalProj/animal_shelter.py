from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = '1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32082
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
    #crud CREATE   
    def create(self,data): 
        if data is not None:
            insertSuccess = self.database.animals.insert_one(data)
            
            # run check 
            if insertSuccess.inserted_id is not None:
                return True
            else: 
                return False
                
            
        else:
            raise Exception ("Nothing to save, because data parameter is empty")
    # crud READ
    def read(self, searchData):
        if searchData:
            data = self.database.animals.find(searchData, {"_id": False})
            
        else:
            data = self.database.animals.find( {}, {"_id": False})
            
        return data
    # crud UPDATE
    def update(self, searchData, updateData):
        if searchData is not None:
            result = self.database.animals.update_many(searchData, { "$set": updateData})
        
        else:
            return "{}"
        # returns datasets
        return result.raw_result
    # crud DELETE
    def delete(self, deleteData):
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)
        else:
            return "{}"
        # returns datasets
        return result.raw_result
