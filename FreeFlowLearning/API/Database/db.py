import sqlite3 as sq
from sqlite3 import Error as sqError

from FreeFlowLearning.API.Errors import Error
from FreeFlowLearning.API.Utils.utils import attempt

from .template import QueryTemplate


class DatabaseManager:
    def __init__(self, db_path):
        try:
            self.connection = sq.connect(db_path)
            self.cursor = self.connection.cursor()
            self.templates = {}
        except sqError as e:
            Error('A connection error ocurred ' + str(e), 3)
    
    def _exec_query(self, query):
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute(query)
            self.connection.commit()
        except sqError as e:
            Error('Query execute error has ocurred ' + str(e), 2)

    def add_template(self, *args, **kwargs):
        """
        add_template adds a QueryTemplate to 
        self.templates to be used and executed later
        """
        try:
            template = QueryTemplate(*args, **kwargs)
            self.templates[template.name] = template
        except Exception as e:
            Error('Template creation/storage error ' + str(e), 2)

    def establish_templates(self):
        """
        .establish_templates() will commit 
        templates to the database to ensure
        that the tables exist
        """
        try:
            for template in self.templates.values():
                self._exec_query(template.create_query())
        except Exception as e:
            Error('Template save to database error ' + str(e), 2)
