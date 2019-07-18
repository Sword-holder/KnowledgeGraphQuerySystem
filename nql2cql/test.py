# 命名实体识别分为7大类：Location, Person, Organization, Money, Percent, Date, Time

from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP('stanfordcorenlp/stanford-corenlp-full-2018-10-05/', lang='zh')

sentence = '周星驰导演过哪些电影？'

print(nlp.word_tokenize(sentence))
print(nlp.pos_tag(sentence))
print(nlp.ner(sentence))
print(nlp.parse(sentence))
print(nlp.dependency_parse(sentence))
