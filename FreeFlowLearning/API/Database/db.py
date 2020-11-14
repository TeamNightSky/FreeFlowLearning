import sqlite3 as sq
from sqlite3 import Error as sqError

from FreeFlowLearning.API.Errors import Error
from FreeFlowLearning.API.Utils.utils import attempt


class DatabaseManager:
    def __init__(self, db_path):
        try:
            self.connection = sq.connect(db_path)
            self.cursor = self.connection.cursor()
        except sqError as e:
            Error('A connection error ocurred ' + e, 3)
    
    def _exec_query(self, query):
        try:
            self.cursor.execute(query)
        except sqError as e:
            Error('Query execute error has ocurred ' + e, 2)



if __name__ == '__main__':
    DatabaseManager('Database/freeflowlearning.db')
