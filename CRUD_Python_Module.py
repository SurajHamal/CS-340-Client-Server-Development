from pymongo import MongoClient 
from bson.objectid import ObjectId 
class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 
    def __init__(self, username, password): 
        """
        Initialize the MongoClient and connect to the aac database.
 
        :param username: MongoDB username for authentication
        :param password: MongoDB password for authentication
        """
        # Connection variables for the MongoDB instance
        USER = username 
        PASS = password 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 

        
        # Establish connection to MongoDB using the provided credentials
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)]

        
    def create(self, data):
        """
        Inserts a document into the MongoDB collection.
 
        :param data: Dictionary of key/value pairs representing the document to insert
        :return: True if the insert was successful, else False
        """
        if data is not None:
            # Result of insert_one is an InsertOneResult object
            result = self.database.animals.insert_one(data)

            # If acknowledged is True, the insert was successful
            if result.acknowledged:
                return True
            else:
                return False
        else:
            # Raise an exception if the data parameter is empty
            raise Exception("Nothing to save, because data parameter is empty") 

    def read(self, query):
        """
        Queries for documents from the MongoDB collection.
        Input: query (dictionary)
        Return: list of results if successful, else empty list
        """
        if query is not None:

            # Use find() to search for all matching documents
            # Convert the cursor to a list and return it
            cursor = self.database.animals.find(query)
            results = list(cursor)
            return results
        else:
            # Return empty list if no query provided
            raise Exception("Nothing to search, because query parameter is empty")

    def update(self, query, update_data):
        """
        Updates document(s) in the MongoDB collection.
        Input: query (dictionary), update_data (dictionary)
        Return: number of documents modified
        """
        if query is not None and update_data is not None:
            result = self.database.animals.update_many(query, {"$set": update_data})
            return result.modified_count
        else:
            raise Exception("Query or update data parameter is empty")
            
    def delete(self, query):
        """
        Removes document(s) from the MongoDB collection.
        Input: query (dictionary)
        Return: number of documents deleted
        """
        if query is not None:
            result = self.database.animals.delete_many(query)
            return result.deleted_count
        else:
            raise Exception("Query parameter is empty")