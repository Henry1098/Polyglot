from konlpy.tag import Kkma
from spacy.tokens import Doc
from class_.korean import Korean as Kor
class KoreanTokenizer:
    ListeOfTokens = []

    def __init__(self, vocab):
        self.vocab = vocab
        self._tokenizer = Kkma()

    def __call__(self, text):
        tokens = self._tokenizer.pos(text)
        words = []
        spaces = []
        ko = Kor()
        self.ListeOfTokens=ko.KorSpace(text,tokens)
        for elements in self.ListeOfTokens:
            if elements[1] != 'SPACE':
                words.append(elements[0])
                spaces.append(False)
            else:
                spaces.append(True)
        return Doc(self.vocab, words=words, spaces=spaces)
