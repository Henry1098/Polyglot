import spacy_thai
from spacy.matcher import Matcher

class Thai:
    def Gram(self,textstr):
        THAI_ôæÄ_NOUN = [
        [{"TEXT":{"REGEX":"^ôæÄ"}}]
    ]

        nlp = spacy_thai.load()
        matcher = Matcher(nlp.vocab)
        matcher.add("THAI_ôæÄ_NOUN",THAI_ôæÄ_NOUN)
        doc = nlp(textstr)
        matches = matcher(doc)
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]  # "HelloWorld"
            spans =doc[start:end]
            print("Matches -------------------------------")
            print(spans)
            print(string_id)