from parser import ParserTree

class Nql2cql(object):

    def __init__(self):
        pass

    def receiveQuestion(self):
        # self.question = input('Please input your question:\n')
        self.question = '周星驰导演过几部电影？'

    def getResult(self):
        parserTree = ParserTree(self.question)
        parserTree.parse()


if __name__ == '__main__':
    nql2cql = Nql2cql()
    nql2cql.receiveQuestion()
    nql2cql.getResult()
