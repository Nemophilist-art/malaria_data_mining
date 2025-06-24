# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

text = '''
每年世界疟疾日都提醒我们，全球还有很多人深受疟疾困扰。虽然中国已经消除了本土疟疾，但出国旅游、出差的朋友仍需注意防蚊、防感染。#世界疟疾日 #健康中国


【一分钟了解疟疾】
疟疾由按蚊传播的疟原虫引起，典型症状包括发冷、发热、出汗、贫血等。全球每年仍有数十万人死于疟疾，主要集中在非洲地区。预防胜于治疗，防蚊灭蚊不能松懈！

今天看到我国援建的非洲疟疾防治中心正式投入使用，真的很感动。中国医生、中国药物在非洲拯救了无数生命，为他们点赞！👏 #中国援非 #全球卫生

去非洲出差第二天就被蚊子咬了，吓得我立刻吃预防药+喷驱蚊液。疟疾真的不是小病，回国前还得检测一遍才放心。希望全球早日无疟！#非洲出差日记 #防蚊提示

'''


from snownlp import normal
from snownlp import seg
from snownlp.summary import textrank


if __name__ == '__main__':
    t = normal.zh2hans(text)
    sents = normal.get_sentences(t)
    doc = []
    for sent in sents:
        words = seg.seg(sent)
        words = normal.filter_stop(words)
        doc.append(words)
    rank = textrank.TextRank(doc)
    rank.solve()
    for index in rank.top_index(5):
        print(sents[index])
    keyword_rank = textrank.KeywordTextRank(doc)
    keyword_rank.solve()
    for w in keyword_rank.top_index(5):
        print(w)