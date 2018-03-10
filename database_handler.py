from abc import ABCMeta, abstractmethod
from sqlite3 import connect
from pymysql import connect as remote_connect
from pymysql import cursors as remote_cursor
from database_abstract import DatabaseAbstract

# Todo: James to create handler
# Must be able to input dictionary into database
# Key must be set and the value will be a dictionary for the record
# Must be able to sync the stored database and the remote database


# Wesley
class DBLocal(DatabaseAbstract):
    # Wesley
    def connect(self, connection=":memory:"):
        """ create object that connects to the local db
            :memory: can be used for a stored db on the ram
            instead of a file/file location"""
        self.connection = connect(connection)
        self.cursor = self.connection.cursor()

    #Sam
    def insert_byte_stream(self, byte_stream):
        """Stores the pickled row as a byte stream in the DB"""
        record = byte_stream
        self.cursor.execute("insert into employee values(null, ?)", record)

    # Wesley
    def delete_record(self, key):
        """Delete a single record that matches the key"""
        self.cursor.execute("delete from employee where key = ?", key)

    # Wesley
    def update_record(self, key, value):
        """Rewrite a record that already exists"""
        record = (value, key)
        self.cursor.execute("update employee set personal = ? where key = ?", record)

#  old method  # Wesley
#    def insert_record(self, key, value):
#        """Insert a single record into the local database"""
#        record = (key, value)
#        self.cursor.execute("insert into employee values(?, ?)", record)

# =====================================================================================================================
# =====================================================================================================================
#                                        LOCAL AND REMOTE SEPERATOR
# =====================================================================================================================
# =====================================================================================================================


# Wesley
class DBRemote(DatabaseAbstract):
    # sadly, Wesley, even I don't like this, breaks my soul
    # The default values need to be set so the ABC can still run
    def connect(self, host=None, user=None, password=None, db=None):
        """Use a list to connect to the remote server
            :param host is the host parameter for the remote server
            :param user is the user parameter for the remote server
            :param password is the needed password for the remote server
            :param db selects the database to be used
            This will connect to the remote server and allow access to read/write
            into the database"""
        try:
            self.connection = remote_connect(host=host,
                                             user=user,
                                             password=password,
                                             db=db,
                                             charset='utf8mb4',
                                             cursorclass=remote_cursor.DictCursor)
        except ValueError:
            print("oops")

        self.cursor = self.connection.cursor()

    #Sam
    def insert_byte_stream(self, byte_stream):
        """Stores the pickled row as a byte stream in the DB"""
        record = byte_stream
        self.cursor.execute("insert into employee values(null, %s)", record)

    # Wesley
    def delete_record(self, key):
        """Delete a single record that matches the key"""
        self.cursor.execute("delete from employee where key = %s", key)

    # Wesley
    def update_record(self, key, value):
        """Rewrite a record that already exists"""
        record = (value, key)
        self.cursor.execute("update employee set personal = %s where key = %s", record)

#    # Wesley
#    def insert_record(self, key, value):
#        """Insert a single record into the local database"""
#        record = (key, value)
#        self.cursor.execute("insert into employee values(%s, %s)", record)
