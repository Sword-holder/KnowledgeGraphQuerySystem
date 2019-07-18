import stanfordnlp
from node_mapper import NodeMapper
from interacter import Interactor

class ParserTree(object):
    
    def __init__(self, query):
        self.query = query

    def parse(self):
        nlp = stanfordnlp.Pipeline(lang='zh')
        doc = nlp(self.query)
        doc.sentences[0].print_dependencies()

    def handleAmbiguity(self):
        while True:
            ambiguity = self.getAmbiguity()
            if ambiguity is None:
                break
            interacter = Interactor(ambiguity)
            choice = interacter.interact()
            self.adjust(choice)

    def getAmbiguity(self):
        return None

    def adjust(self, choice):
        pass


#####################################
#              测试程序              #
#####################################
def test():
    tree = ParserTree('周星驰导演过哪些电影')

if __name__ == '__main__':
    test()