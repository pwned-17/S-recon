from tinydb import TinyDB,Query

class DB(object):

    def __init__(self,table):
        self.query=Query()
        self.db=TinyDB("output.json")
        self.table=self.db.table(table)

    def insert(self,data):
        self.table.insert(data)

    def truncate(self):
        self.db.drop_tables()

    def search(self,query):
        return self.table.search(query)
