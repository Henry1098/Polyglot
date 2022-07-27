import spacy
from spacy.matcher import Matcher
from collections import defaultdict
import collections
from spacy.tokens import Span

class Chinese:

    def Grammar(self,text):
        nlp = spacy.load("zh_core_web_trf")
        matcher = Matcher(nlp.vocab)

        HSK_Level1_PHRASE_什么 = [
            [{"OP":"+"},{"ORTH":"什么"}]
        ]
        
        HSK_Level1_PHRASE_什么_NOUN = [
            [{"OP":"+"},{"ORTH":"什么"},{"POS":"NOUN"}],
            [{"OP":"+"},{"ORTH":"什么"},{"POS":"PROPN"}],
            [{"OP":"+"},{"ORTH":"什么"},{"POS":"PRON"}]
        ]
        HSK_Level1_OP_不是_OP =[
            [{"OP":"+"},{"ORTH":"不是"},{"OP":"+"}]
        ]
        HSK_Level1_OP_是_OP =[
            [{"OP":"+"},{"ORTH":"是"},{"OP":"+"}]
        ]
        HSK_Level_PHRASE_吗 = [
            [{"OP":"+"},{"ORTH":"吗"}]
        ]
        HSK_Level_PHRASE_谁  = [
            [{"OP":"+"},{"ORTH":"谁"}]
        ]
                
        matcher.add("HSK_Level1_PHRASE_什么",HSK_Level1_PHRASE_什么)
        matcher.add("HSK_Level1_PHRASE_什么_NOUN",HSK_Level1_PHRASE_什么_NOUN)
        matcher.add("HSK_Level1_OP_不是_OP",HSK_Level1_OP_不是_OP)
        doc = nlp(text)
        matches = matcher(doc)
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]  # "HelloWorld"
            spans =doc[start:end]
            print("Matches -------------------------------")
            print(spans)
            print(string_id)
