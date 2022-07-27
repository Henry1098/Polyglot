import spacy
import spacy_stanza
from spacy.matcher import Matcher
from collections import defaultdict
import collections

class Korean:
    def test1(self,textstr):
        TOPIK_Korean_Level1_NOUN_은 = [
    [{"POS":"NOUN","TEXT":{"REGEX":"은$"}}],
    [{"POS":"PROPN","TEXT":{"REGEX":"은$"}}],
    [{"POS":"PRON","TEXT":{"REGEX":"은$"}}],

]

        TOPIK_Korean_Level1_NOUN_는 = [
    [{"POS":"NOUN","TEXT":{"REGEX":"는$"}}],
    [{"POS":"PROPN","TEXT":{"REGEX":"는$"}}],
    [{"POS":"PRON","TEXT":{"REGEX":"는$"}}],
]

        TOPIK_Korean_Level1_NOUN_이 = [
    [{"POS":"NOUN","TEXT":{"REGEX":"이$"}}],
    [{"POS":"PROPN","TEXT":{"REGEX":"이$"}}],
    [{"POS":"PRON","TEXT":{"REGEX":"이$"}}],
]

        TOPIK_Korean_Level1_NOUN_가 = [
    [{"POS":"NOUN","TEXT":{"REGEX":"가$"}}],
    [{"POS":"PROPN","TEXT":{"REGEX":"가$"}}],
    [{"POS":"PRON","TEXT":{"REGEX":"가$"}}],
]

        #object particle
        TOPIK_Korean_Level1_NOUN_을 = [
    [{"POS":"NOUN","TEXT":{"REGEX":"을$"}}],
    [{"POS":"PROPN","TEXT":{"REGEX":"을$"}}],
    [{"POS":"PRON","TEXT":{"REGEX":"을$"}}],
]

        #object particle
        TOPIK_Korean_Level1_NOUN_를 = [
    [{"POS":"NOUN","TEXT":{"REGEX":"를$"}}],
    [{"POS":"PROPN","TEXT":{"REGEX":"를$"}}],
    [{"POS":"PRON","TEXT":{"REGEX":"를$"}}],
]

        #possessive particle
        TOPIK_Korean_Level1_NOUN_의 = [
    [{"POS":"NOUN","TEXT":{"REGEX":"의$"}}],
    [{"POS":"PROPN","TEXT":{"REGEX":"의$"}}],
    [{"POS":"PRON","TEXT":{"REGEX":"의$"}}],
]



        nlp = spacy_stanza.load_pipeline("ko")
        matcher = Matcher(nlp.vocab)
        matcher.add("TOPIK_Korean_Level1_NOUN_은",TOPIK_Korean_Level1_NOUN_은)
        matcher.add("TOPIK_Korean_Level1_NOUN_는",TOPIK_Korean_Level1_NOUN_는)
        matcher.add("TOPIK_Korean_Level1_NOUN_이",TOPIK_Korean_Level1_NOUN_이)
        matcher.add("TOPIK_Korean_Level1_NOUN_가",TOPIK_Korean_Level1_NOUN_가)
        matcher.add("TOPIK_Korean_Level1_NOUN_을",TOPIK_Korean_Level1_NOUN_을)
        matcher.add("TOPIK_Korean_Level1_NOUN_를",TOPIK_Korean_Level1_NOUN_를)
        matcher.add("TOPIK_Korean_Level1_NOUN_의",TOPIK_Korean_Level1_NOUN_의)
        doc = nlp(textstr)
        matches = matcher(doc)

        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]  # "HelloWorld"
            spans =doc[start:end]
            print("Matches -------------------------------")
            print(spans)
            print(string_id)

    
    def KorSpace(self,original_text,List):
        SplitList =str.split()
        for word in SplitList:
            strTemp = word[-1]
            for elementinList,idx in zip(List,range(0,len(List))):
                if strTemp in elementinList[0] or elementinList[0] == strTemp:
                    List.insert(idx+1,(' ','SPACE'))
        print(List)
        return List