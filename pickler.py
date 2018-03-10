from pickle import dumps
# from unpickler import Unpickler
# from DB_Local import DBLocal
# from collections import namedtuple


# Wesley
class Pickler:

    # Wesley
    def __init__(self):
        self.pickle_dict = {}

    # Wesley
    def pickle_record_values(self, key, value):
        """ Pickle a record and add to a dictionary
            :param1 key, will be the key defined in the dictionary
            :param2 value, will be pickled
            No return provided
            """
        self.pickle_dict[key] = dumps(value)
        return self.pickle_dict

    # Wesley
    def pickle_dictionary_values(self, dictionary):
        """Create a dictionary with pickled values, the key will remain the same"""
        for key, value in dictionary:
            self.pickle_dict[key] = dumps(value)
        return self.pickle_dict

    # does this need to be static??
    @staticmethod
    def pickle_super_dict(dictionary): # (self, dictionary) (if not static)
        pickled_super_dict = dumps(dictionary) # pickled_super_dict's data type is now a byte stream
        return pickled_super_dict # returns a byte stream


# check that it creates byte stream

# tester = Pickler()
# print(type(tester))
# b = tester.pickle_super_dict({"ONE", "THE NUMBER ONE"})
# print(type(b))


    # using a function to get the dictionary instead of returning each time it changes
    # def get_dictionary(self):

# Just shows that everything works
# thing = Pickler()
# thing.pickle_record_values("hey", "aslkdjflasdkj3r325")
# thing.pickle_record_values("he1y", "aslkdjflasdkj34r325")
# thing.pickle_record_values("h3ey", "aslkdjflasd4kj3r325")
# pickled_dict = thing.pickle_record_values("he2y", "aslkdjflasdkj123r325")
# #
# # print(pickled_dict)
# # #
# aThing = Unpickler()
#
# unpickled_dict = aThing.unpickle_dictionary(pickled_dict)
# # print(unpickled_dict)
#
# conn = DBLocal()
#
# conn.connect(":memory:")
# conn.create_table()
# conn.insert_dictionary(pickled_dict)
# print(dict(conn.get_db()))



