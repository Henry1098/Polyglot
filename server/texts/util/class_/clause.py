import spacy
import re

class Clause:
    liste = ["auquel","auxquels","à laquelle","laquelle","auxquelles","desquels","de laquelle","desquelles","ce à quoi","ce que","ce qui","c’que","c’qui","de quoi","dont","dont auquel","duquel","lequel","où","que","qui","qui que c’est que","quiconque","quoi"]

    def ClauseSub(self,phrase):
        counterV = 0
        counteret = 0
        counterM = 0
        startM = 0
        startV = 0
        listeMatches = []
        strMain = ""
        strTemp = ""
        tmpList = []
        countMatch = 0
        counterpart = 0
        listeMain = []
        listeSub = []
        nlp = spacy.load("fr_dep_news_trf")
        for token in nlp(phrase):
            if token.text == ",":
                counterV = counterV + 1
            if token.text == "et":
                counteret = counteret + 1
            if token.pos_ == "VERB" and token.text[-3:] == "ant":
                counterpart = counterpart + 1
                startV = token.idx
        for el in self.liste:
          for match in re.finditer(el, phrase):
            counterM = counterM + 1
            listeMatches.append(match)
            startM = match.start()


        return [startV,startM]