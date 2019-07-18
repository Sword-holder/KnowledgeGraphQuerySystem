from neo4j import GraphDatabase

class Proxy(object):

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.cql = None

    def generateCQL(self):
        self.cql = "MATCH (n1:Person{name:'周星驰'})-[:DIRECTED]->(m:Movie)<-[:ACTED_IN]-(n2:Person{name:'黄渤'}) RETURN m.name"

    def executeQuery(self):
        with self.driver.session() as session:
            session.read_transaction(self._doExecute)
    
    def _doExecute(self, tx):
        for record in tx.run(self.cql):
            print(record)


if __name__ == '__main__':
    proxy = Proxy(uri='bolt://localhost:7687', user='neo4j', password='123456')
    proxy.generateCQL() 
    proxy.executeQuery() 
