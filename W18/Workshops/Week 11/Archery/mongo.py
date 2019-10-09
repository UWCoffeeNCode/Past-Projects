# External imports
from pymongo import MongoClient
from bson import ObjectId
from bson.errors import InvalidId

client = MongoClient(tz_aware=True)

class Database:
    def __init__(self, db_name):
        self.db = client[db_name]

    @property
    def mongodb(self):
        return self.db

    def coll(self, coll_name):
        return self.db[coll_name]

    def insert(self, collection, data, ordered=True):
        """
        Function to write provided data to database
        :param array data: The data to be written
        :return: True if write succeeded, False otherwise
        :rtype: bool
        """
        result = self.db[collection].insert(data, ordered)
        return result.nInserted == 1

    def find_all(self, collection):
        """
        Function to find all records in the provided collection
        :param string collection: The name of the database collection
        :return: A list containing all records in the collection
        :rtype: list
        """
        pointer = self.db[collection].find()
        return [obj for obj in pointer]


    def find_subset(self, collection, query):
        """
        Function to find a subset of the records in the collection, with the subset determine
        by the query.
        :param string collection: The name of the database collection
        :param dict query: A query, potentially limiting the returned records
        :return: A list of all records in the collection that matched the query
        :rtype: list
        """
        pointer = self.db[collection].find(query)
        return [obj for obj in pointer]


    def find_one(self, collection, query=None):
        """
        Function to find a single record in a collection. If no query is provided, it will return the
        first record based on the natural sort order. Otherwise, it will find the first record based
        on the natural sort order, after filtering the collection based on the query. Deletes the
        **_id** property of the returned dictionary.
        :param string collection: The name of the database collection
        :param dict query: A query, potentially changing the returned record
        :return: A dict containing the first record in the natural ordering based on the search
            criteria. If nothing is found, an empty dict will be returned.
        :rtype: dict
        """
        res = self.db[collection].find_one(query)

        if res:
            del res['_id']
            return res
        else:
            return {}


    def find_by_id(self, collection, object_id, literal=False):
        """
        Function to find an object in the database by its unique MongoDB identifier. If you're using
        your own thing as the **_id** of a record, you need to set the literal property to True.
        Otherwise the  *object_id* argument will be cast to the BSON ObjectId type, before being matched
        to the **_id** in the database.
        :param str collection: he name of the database collection
        :param str_or_int object_id: The unique ID (**_id**) of the record you're looking for
        :param bool literal: If true, the *object_id* argument is kept as a whatever it's passed in as.
            Otherwise it is cast to the BSON ObjectID type
        :return: A dict containing the results of the query (if any). If nothing is found, an empty
            dict is returned
        :rtype: dict
        """
        if not literal:
            try:
                object_id = ObjectId(str(object_id))
            except InvalidId:
                raise ValueError("{} is not a valid literal ObjectID".format(object_id))
        return self.find_one(collection, {"_id": object_id})
