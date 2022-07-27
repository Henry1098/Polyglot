import os
import spacy
import json
from pathlib import Path
from bs4 import BeautifulSoup
from spacy import displacy
from collections import defaultdict
from spacy.matcher import PhraseMatcher
from .util.class_.english import English as eng
from .util.class_.french import French as french
from .util.class_.spanish import Spanish as spa
from .util.class_.italian import Italian as ita
from .util.class_.japanese import Japanese as jap1
from .util.class_.chinese import Chinese as chin
from .util.class_.clause import Clause
from .util.class_.thai import Thai as th
from spacy.tokens import Token
from spacy.tokens import Token
from konlpy.tag import Kkma
import spacy_thai
from underthesea import pos_tag
import stanza
import spacy_stanza
import suparkanbun
import unidic2ud.spacy
import spacy_udpipe

# stanza.download("la")
# stanza.download("grc")
# stanza.download("eu") #Euskara Basque
# stanza.download("ar")
# stanza.download("he")
# # stanza.download("hi")
# stanza.download("ga")
# stanza.download("id")
# stanza.download("hy")
# stanza.download("be")
# stanza.download("fi")
# stanza.download("nn")
# stanza.download("fro")
# stanza.download("orv")
# stanza.download("sv")
# stanza.download("tr")
# stanza.download("fa")

class Utilities:

    listelangues = []
    idioms = []
    proverbs = []


    def lang(self,lang,textstr):
        langswitch={


        }
        return langswitch.get(lang,"Error language not available")
        
    def findProverbs(self,fileStr,textstr,langue):  
        listeProverbs = []  
        nlp = spacy.load(langue)
        textstr = textstr.strip()
        with open('proverbs/'+fileStr,'r',encoding="utf-8") as f:
            idioms_list= f.readlines()
        phrase_matcher = PhraseMatcher(nlp.vocab,attr="LOWER")
        patterns = [nlp(text.strip()) for text in idioms_list]
        phrase_matcher.append('Proverbs', None, *patterns)
        sentences = self.treat_text_to_sentences(textstr)
        for txt in sentences:
            sentence = nlp (txt)
            matched_phrases = phrase_matcher(sentence)
            for match_id, start, end in matched_phrases:
                listeProverbs.append(sentence[start:end])
        return listeProverbs
    
    

    

    #traitement du japonais classique
    def jap2(self,textstr):
        nlp = unidic2ud.spacy.load("qkana")
        nlp2 = unidic2ud.spacy.load("gendai")
        nlp3 = unidic2ud.spacy.load("spoken")
        nlp4 = unidic2ud.spacy.load("kindai")
        nlp5 = unidic2ud.spacy.load("kinsei")
        nlp6 = unidic2ud.spacy.load("wakan")
        nlp7 = unidic2ud.spacy.load("wabun")
        nlp8 = unidic2ud.spacy.load("manyo")
        doc = nlp(textstr)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop,list(token.morph))
        return "Japanesehello"

    #traitement du wolof
    def wo(self,textstr):
        nlp = spacy_udpipe.load_from_path(lang="wo",
                                    path=Path(os.getcwd()+"\\texts\\util\\datas\\Wolof.udpipe"),
                                    meta={"description": "Custom 'wo' model"})
        text = textstr

        doc = nlp(text)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.dep_)
        return "Wolofhello"
        
    #traitement de l'amharique
    def am(self,textstr):

        nlp = spacy.load(Path(os.getcwd()+"\\texts\\util\\datas\\Amharic\\model-best"))
        text = textstr

        doc = nlp(text)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.dep_)
        return "Amharichello"


    #traitement du farsi
    def fa(self,textstr):
        nlp = spacy_stanza.load_pipeline("fa")
        doc = nlp(textstr)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)
        return "Farsihello"

    #traitement du turque
    def tr(self,textstr):
        nlp = spacy_stanza.load_pipeline("tr")
        doc = nlp(textstr)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)
        return "Suedehello"

    #traitement du suédois
    def sv(self,textstr):
        nlp = spacy_stanza.load_pipeline("sv")
        doc = nlp(textstr)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)
        return "Suedehello"

    #traitement du vieux français
    def fro(self,textstr):
        nlp = spacy_stanza.load_pipeline("fro")
        doc = nlp(textstr)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)
        return "Fraoldhello"

    #traitement du norvege nynorsk
    def nn(self,textstr):
        nlp = spacy_stanza.load_pipeline("nn")
        doc = nlp(textstr)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)
        return "Nyorskhello"

    #traitement du finnois
    def fin(self,textstr):
        nlp = spacy_stanza.load_pipeline("fi")
        doc = nlp(textstr)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)
        return "Finnishhello"

    #traitement du belarusse
    def bel(self,textstr):
        nlp = spacy_stanza.load_pipeline("be")
        doc = nlp(textstr)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)
        return "Belarussianianhello"

    #traitement de l'armenien
    def arm(self,textstr):
        nlp = spacy_stanza.load_pipeline("hy")
        doc = nlp(textstr)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)
        return "Armenianianhello"

    #traitement de l'indonesien
    def ind(self,textstr):
        nlp = spacy_stanza.load_pipeline("id")
        doc = nlp(textstr)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)
        return "Indonesianhello"


    #traitement du l'irlandais
    def ga(self,textstr):
        nlp = spacy_stanza.load_pipeline("ga")
        doc = nlp(textstr)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)
        return "Irishhello"

    #traitement du basque
    def eus(self,textstr):
        nlp = spacy_stanza.load_pipeline("eu")
        doc = nlp(textstr)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)
        return "Euskarahello"

    #traitement de l'arabe
    def ar(self,textstr):
        nlp = spacy_stanza.load_pipeline("ar")
        doc = nlp(textstr)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)
        return "Arabichello"

    #traitement du latin
    def latin(self,textstr):
        nlp = spacy_stanza.load_pipeline("la")
        doc = nlp(textstr)
        for token in doc:
            print("Text: "+token.text, "Lemma: " +token.lemma_,"Pos: "+token.pos_,"Tag: "+token.tag_,"Dep:"+token.dep_,"Shape: "+token.shape_, "Alpha: "+str(token.is_alpha), "Stop:"+str(token.is_stop))
        return "Latinhello"

    #traitement du grec ancien
    def grc(self,textstr):
        nlp = spacy_stanza.load_pipeline("grc")
        doc = nlp(textstr)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)
        return "grchello"


    #traitement du chinois classique
    def lzh(self,textstr):
        nlp=suparkanbun.load(BERT="guwenbert-large")
        print(nlp._path)
        doc=nlp("長吉顧逋翁于白樂天是也夫中郎茂先郎于王仲宣張茂先于二陸韓退之于李類假文章鉅公片言以定其聲價若蔡中其名者蓋以古來魁閎絶特掉鞅詞壇者林君産於魯客於楚魯楚之間未有豔道近來海內詩人未有如林君之工且敏者偶存草詩序")
        for token in doc:
            print(token.text,token.pos_,token.lemma_)

        return "lzhhello"


    #traitement du hongrois
    def magyar(self,textstr):
        nlp = spacy.load("hu_core_news_lg")
        doc = nlp(textstr)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)
        return "Magyarhello"

    #traitement du breton
    def breton(self,textstr):
        nlp = spacy.blank(Path(os.getcwd()+"\\texts\\util\\datas\\Breton\\model-best"))
        doc = nlp(textstr)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)
        return "Bretonhello"

    #traitement du thai
    def thai(self,textstr):
        thai=th()
        nlp = spacy_thai.load()
        doc = nlp(textstr)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)
        thai.Gram(textstr)
        return "Thaihello"

    #traitement du vietnamien
    def viet(self,textstr):
        doc = pos_tag(textstr)
        print(doc)
        return "Viethello"

    #traitement du korean
    def ko(self,textstr):
        Liste = ""
        Str = ""
        kkma = Kkma()
        print(kkma.pos(textstr))
        for el in kkma.pos(textstr):
            Liste += "<ruby>"+el[0]+"<rp>(</rp><rt>"+el[1]+"</rt><rp>)</rp></ruby>&nbsp;&nbsp;&nbsp;&nbsp;"
        Str = "Korean Kkma: "+Liste
        return Str


    #traitement de l'anglais
    def english(self,textstr):    
        data = {}
        aux = Token
        aux2 = False
        sent=self.treat_text_to_sentences(textstr)
        nlp = spacy.load("en_core_web_sm")
        for phrase,index in zip(sent,range(0,len(sent))):
            doc = nlp(phrase)
        for ix,token in zip(range(0,len(doc)),doc):
            print(token.text,list(token.morph), token.pos_,token.dep_)
            if token.pos_ == "VERB":
                print(aux)
            if token.pos_ == "AUX":
                if token.pos_ == "AUX" and doc[ix+1].pos_ == "AUX":
                    aux =  [token,doc[ix+1]]
                    print("True")
                    aux2 = True
                else:
                    if aux2 == True:
                        continue
                    else:
                        aux = token
                        print("False")
                        aux2 = False

        json_data = json.dumps(data,ensure_ascii=False)
        print("ed")
        return "englishHello"




    #traitement du tibetan
    def tib(self,textstr):    
        nlp = spacy.load(Path(os.getcwd()+"\\texts\\util\\datas\\ModernTibetan\\model-best"))
        doc = nlp(textstr)
        data = {}
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                token.shape_, token.is_alpha, token.is_stop)
            data['text']=token.text
            data['lemma']=token.lemma_
            data['pos']=token.pos_
        return "Tibetan\n"+json.dumps(data,ensure_ascii=False)

    #traitement du vieux tibetan
    def otib(self,textstr):    
        nlp = spacy.load(Path(os.getcwd()+"\\texts\\util\\datas\\OldTibetan\\model-best"))
        doc = nlp(textstr)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                token.shape_, token.is_alpha, token.is_stop)
        return "OldTibetan"

    #traitement du tibetan classique
    def xtib(self,textstr):    
        nlp = spacy.load(Path(os.getcwd()+"\\texts\\util\\datas\\ClassicalTibetan\\model-best"))
        doc = nlp(textstr)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                token.shape_, token.is_alpha, token.is_stop)
        return "ClassicalTibetan"

    #traitement du Corse
    def corse(self,textstr):    
        nlp = spacy.load(Path(os.getcwd()+"\\texts\\util\\datas\\Corse\\model-best"))
        doc = nlp(textstr)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                token.shape_, token.is_alpha, token.is_stop)
        return "Corse"


    #traitement du chinois
    def zh(self,textstr):    
        data = {}
        aux = Token
        aux2 = False
        chi = chin()
        sent=self.treat_text_to_sentences(textstr)
        chi.Grammar(textstr)
        nlp = spacy.load("zh_core_web_trf")
        doc = nlp(textstr)
        for token in doc:
            print(token.text,list(token.morph), token.pos_,token.dep_,token.lemma_)
        return "hello"



    #traitement du français
    def fra_(self,textstr):    
        TempsVerbe = ""
        aux = Token
        data =  {}
        sdict = defaultdict(list)
        listel = list()
        sent = []
        fra = french()
        aux2 = False
        nlp = spacy.load("fr_dep_news_trf")
        sent=self.treat_text_to_sentences(textstr)
        clause_ = Clause()
        # data['idioms'] =findIdioms("fr_dep_news_trf","idioms_fr.txt",textstr)
        # data['proverbs'] = findProverbs("proverbs_fr.txt",textstr,"fr_dep_news_trf")
        # pr=fra.NamedEntities(textstr)
        # for x in pr:
        #     print(x.text, x.start_char, x.end_char, x.label_)
        print(textstr)
        for phrase,index in zip(sent,range(0,len(sent))):
            data['phrase'+str(index)] = {"Phrase":phrase}
            # print(fra.IsPassive(phrase))
            doc = nlp(phrase)
            for ix,token in zip(range(0,len(doc)),doc):
                print("Text: "+token.text, "Lemma: " +token.lemma_,"Pos: "+token.pos_,"Tag: "+token.tag_,"Dep:"+token.dep_,"Shape: "+token.shape_, "Alpha: "+str(token.is_alpha), "Stop:"+str(token.is_stop))
        #         data[token.text] = {"pos":token.pos_}
        #         listel.append(token.text)
        #         if token.text in listel:
        #             sdict[token.text].append(data[token.text])
        #         else:
        #             sdict[token.text]=data[token.text]
        #         if token.pos_ == "VERB":
        #             Subject= get_subject("fr_dep_news_trf",phrase)
        #             Tense=token.morph.get("Tense")
        #             Person= token.morph.get("Person")
        #             Number= token.morph.get("Number")
        #             Next = ""
        #             #doc[ix+1].text if doc[ix+1].text != "" else ""
        #             if(token.text.endswith("e") and token.morph.get("Person") == ['1'] and token.morph.get("Number") == ['Sing'] or token.text.endswith("e") and token.morph.get("Person") == ['3'] and token.morph.get("Number") == ['Sing']):
        #                 Infinitive= token.text+"r"
        #             else:    
        #                 Infinitive = token.lemma_
        #             Groupe = fra.groupeVerbe(Infinitive)
        #             IrregularV = fra.irregularverb_(token.lemma_)
        #             VerbForm = token.morph.get("VerbForm")
        #             Mood= token.morph.get("Mood")
        #             print(fra.tempsVerbe(token,Groupe,Tense,Mood,aux))
        #             data[token.text]['VERB']= [phrase,Subject,Tense,Person,Number,Infinitive,Groupe,IrregularV,VerbForm,Mood,Next]
        #             listel.append(token.text)
        #             if token.text in listel:
        #                 sdict[token.text].append(data[token.text]['VERB'])
        #             else:
        #                 sdict[token.text]=data[token.text]['VERB']
        #         if token.pos_ == "NOUN":
        #             Gender = token.morph.get("Gender")
        #             Number = token.morph.get("Number")
        #             IrregularN= fra.irregularnoun_(token.text)
        #             Next = doc[ix+1].text if doc[ix+1].text != "" else ""
                    
        #             data[token.text]['NOUN'] = [phrase,Gender,Number,IrregularN,Next]
        #             listel.append(token.text)
        #             if token.text in listel:
        #                 sdict[token.text].append(data[token.text]['NOUN'])
        #             else:
        #                 sdict[token.text]=data[token.text]['NOUN']
        #         if token.pos_ == "ADJ":
        #             Gender = token.morph.get("Gender")
        #             Number = token.morph.get("Number")
        #             Noun = doc[ix-1].text if doc[ix-1].pos_ == "NOUN" or doc[ix-1].pos_ == "PROPN" else doc[ix+1].text
        #             IrregularADJ = fra.irregularadj_(token.text)
        #             Next = doc[ix+1].text if doc[ix+1].text != "" else ""
                    
        #             data[token.text]['ADJ'] = [phrase,Gender,Number,Noun,IrregularADJ,Next]
        #             listel.append(token.text)
        #             if token.text in listel:
        #                 sdict[token.text].append(data[token.text]['ADJ'])
        #             else:
        #                 sdict[token.text]=data[token.text]['ADJ']
        #         if token.pos_ == "ADV":
        #             IrregularADV = fra.irregularadverb_(token.text)
        #             Next = doc[ix+1].text if doc[ix+1].text != "" else ""
        #             data[token.text]['ADV'] = [phrase,IrregularADV,Next]
        #             listel.append(token.text)
        #             if token.text in listel:
        #                 sdict[token.text].append(data[token.text]['ADV'])
        #             else:
        #                 sdict[token.text]=data[token.text]['ADV']
        #         if token.pos_ == "DET":
        #             Type = fra.determiner(token.text.lower())
        #             if token.morph.get("Gender") != []:
        #                 Gender = token.morph.get("Gender") 
        #             else:
        #                 Gender = doc[ix+1].morph.get("Gender")
        #             Number = token.morph.get("Number")
        #             PronType = token.morph.get("PronType")
        #             Poss = token.morph.get("Poss")
        #             Next = doc[ix+1].text if doc[ix+1].text != "" else ""
        #             data[token.text]['DET'] = [phrase,Type,Gender,Number,PronType,Poss,Next]
        #             listel.append(token.text)
        #             if token.text in listel:
        #                 sdict[token.text].append(data[token.text]['DET'])
        #             else:
        #                 sdict[token.text]=data[token.text]['DET']
        #         if token.pos_ == "PRON":
        #             Person = token.morph.get("Person")
        #             DEP = token.dep_
        #             Reflex = token.morph.get("Reflex")
        #             Next = ""
        #             #doc[ix+1].text if doc[ix+1].text != "" else ""
        #             data[token.text]['PRON'] = [phrase,Person,DEP,Reflex,Next]
        #             listel.append(token.text)
        #             if token.text in listel:
        #                 sdict[token.text].append(data[token.text]['PRON'])
        #             else:
        #                 sdict[token.text]=data[token.text]['PRON']
        #         if token.pos_ == "AUX":
        #             if token.pos_ == "AUX" and doc[ix+1].pos_ == "AUX":
        #                 aux =  [token,doc[ix+1]]
        #                 print("True")
        #                 aux2 = True
        #             else:
        #                 if aux2 == True:
        #                     continue
        #                 else:
        #                     aux = token
        #                     print("False")
        #                     aux2 = False
                    
        # json_data = json.dumps(dict(sdict),ensure_ascii=False)
        # print(sdict)
        # print(TempsVerbe)
        return "Français! :"
        # +json_data



    #traitement de l'allemand
    def de(self,textstr):    
        data = {}
        Case = []
        Gender=[]
        Number = []
        nlp = spacy.load("de_dep_news_trf")
        doc = nlp(textstr)
        for token in doc:
            if token.pos_ == "NOUN":
                    Case=token.morph.get("Case")
                    Gender= token.morph.get("Gender")
                    Number = token.morph.get("Number")
            print(Case,Gender,Number)
            print(token.text+" "+token.pos_)
        json_data = json.dumps(data,ensure_ascii=False)
        print(json_data)
        return json_data


    #traitement de l'italien
    def it(self,textstr):    
        data = {}
        ita_ = ita()
        nlp = spacy.load("it_core_news_lg")
        sent=self.treat_text_to_sentences(textstr)
        # data['idioms'] =findIdioms("it_core_news_lg","idioms_it.txt",textstr)
        # data['proverbs'] = findProverbs("proverbs_it.txt",textstr,"it_core_news_lg")
        for phrase,index in zip(sent,range(0,len(sent))):
            data['phrase'+str(index)] = {"Phrase":phrase}
            doc = nlp(phrase)
            for token in doc:
                data[token.text] = {"pos":token.pos_}
                if token.pos_ == "VERB":
                    data[token.text]['Subject']= self.get_subject("it_core_news_lg",phrase)
                    data[token.text]['Tense']=token.morph.get("Tense")
                    data[token.text]['Infinitive'] = token.lemma_
                    data[token.text]['Irregular'] = ita_.irregularverb_(token.text)
                if token.pos_ == "NOUN":
                    data[token.text]['Gender'] = token.morph.get("Gender")
                    data[token.text]['Number'] = token.morph.get("Number")
                    data[token.text]['IrregularNoun'] = ita_.irregularnoun_(token.text)

        json_data = json.dumps(data,ensure_ascii=False)
        print(json_data)
        return json_data

    #traitement du japonais
    def jap(self,textstr):    
        jap_ = jap1()
        data = {}
        gyarumoji = {'ぁ': 'あ', 'ァ': 'あ', '了': 'あ', 'ぃ': 'い', 'ィ': 'い', 'ﾚヽ': 'い', 'ﾚ丶': 'い', 'レ）': 'い', 'ﾚ`': 'い', 'L丶': 'い', 'L1': 'い', 'ﾚl': 'い', 'ぅ': 'う', 'ゥ': 'う', '宀': 'う', 'ヴ': 'ふ', 'ウ': 'う', 
    'ぇ': 'え', 'ェ': 'え', '之': 'え', '工': 'I', 'ヱ': 'え', 'ぉ': 'お', 'ォ': 'お', '才': 'お', 'ｶゝ': 'か', 'ｶ丶': 'か', 'ｶヽ': 'か', 'ヵゝ': 'か', 'ｶ`': 'か', 'ｶゞ': 'か', 'カ': 'か', 'ヵゞ': 'が', 'カ゛': 
    'ガ', '力゛': 'ガ', '(ｷ': 'き', '(≠': 'き', 'L≠': 'き', 'ｷ':'き','‡': 'き',"(ｷ\"\"": "ぎ", "(≠\"": "ぎ", "L≠\"": "ぎ", "ｷ\"":"ぎ","‡\"": "ぎ", '＜': 'く', '〈': 'く', '勹': 'く', 'ヶ': 'け', '(ﾅ': 'け', 'ﾚ†': 'け', 'ﾚﾅ': 'け', '|ナ': 'け', 'l+': 'け', 'Iﾅ': 'け',"＜\"": "ぐ", "〈\"": "ぐ", "勹\"": "ぐ", "ヶ\"": "げ", "(ﾅ\"": "げ", "ﾚ†\"": "げ", "ﾚﾅ\"": "げ", "|ナ\"": "げ", "l+\"": "げ", "Iﾅ\"": "げ", '〓': 'こ', '=': 'こ', ']': 'こ', '⊃': 'こ', '⊇': 'こ',"〓\"": "ご", "=\"": "ご", "]\"": "ご", "⊃\"": "ご", "⊇\"": "ご", '廾': 'さ', '±': 'さ', '(十': 'さ', 'L+': 'さ', '(+': 'さ', '､ﾅ': 'さ', 'ι': 'し', '∪': 'し', 'U': 'し', '￡': 'す', 'ﾌ､': 'す', '世': 'せ', 'ξ': 'そ', 'ζ': 'ら', '`ﾉ': 'そ', '丶/': 'そ', 'ヽ丿': 'そ', 'ﾅ=': 'た', '+=': 'た', '†ﾆ': 'た', 'ﾅﾆ': 'た', '十こ': 'た', '†こ': 'た', 'ﾅ⊇': 'た', 'T=': 'た', '十=': 'た', '夕': 'た', '干': 'ち', '千': 'ち', '于': 'ち', 'ろ＋': 'ち', 'っ': 'つ', 'ッ': 'つ', 'ﾂ【っ】': 'つ', '廾"': 'ざ', '±"': 'ざ', '(十"': 'ざ', 'L+"': 'ざ', '(+"': 'ざ', '､ﾅ"': 'ざ', 'ι"': 'じ', '∪"': 'じ', 'U"': 'じ', '￡"': 'ず', 'ﾌ､"': 'ず', '世"': 'ぜ', 'ξ"': 'ぞ', 'ζ"': 'ぞ', '`ﾉ"': 'ぞ', '丶/"': 'ぞ', 'ヽ丿"': 'ぞ', 'ﾅ="': 'だ', '+="': 'だ', '†ﾆ"': 'だ', 'ﾅﾆ"': 'だ', '十こ"': 'だ', '†こ"': 'だ', 'ﾅ⊇"': 'だ', 'T="': 'だ', '十="': 'だ', '夕"': 'だ', 'っ"': 'づ', 'ッ"': 'づ', 'ﾂ【っ】"': 'づ', '⊃"':'づ','⊃':'つ','干"': 'ぢ', '千"': 'ぢ', '于"': 'ぢ', 'ろ＋"': 'ぢ','τ': 'て', '〒': 'て', 'z': 'て', '乙': 'て', '┠': 'と', '┝': 'と', '┣': 'と', '├': 'と', '`⊂': 'と', '卜': 'と', '`c': 'と',"τ\"": 'で', 'z"': 'で', '乙"': 'で', '┠"': 'ど', '┝"': 'ど', '┣"': 'ど', '├"': 'ど', '`⊂"': 'ど', '卜"': 'ど', '`c"': 'ど', 'ﾅょ': 'な', '十ょ': 'な', '†ょ': 'な', 'ﾅg': 'な', '†ょゝ': 'な', '十': 'な', '(ﾆ': 'に', '|=': 'に', '丨ﾆ': 'に', 'L=': 'に', 'I=': 'に', '（⊇': 'に', 
    'レこ': 'に', '(二': 'に', 'ﾚﾆ': 'に', 'йu': 'ぬ', 'ゐ': 'み', 'йё': 'ね', '/': 'の', '丿': 'の', 'σ': 'の', '⊂n': 'の', '＠': 'の', "'`": 'は', '八': 'は', 'l￡': 'は', '(￡': 'は', 'ﾉ|': 'は', 'ﾉl': 'は', 'ﾚ￡': 'は', 'ﾚよ': 'は', 'ﾊ〃': 'バ', 'ﾊo': 'パ', '匕': 'ひ', 'ﾋ〃': 'ビ', 'ﾋo': 'ピ', ',ζ,':  
    'ふ', 'ﾌ〃': 'ブ', 'ﾌo': 'プ', '〜': 'へ', '∧': 'へ', 'ﾍ〃': 'べ', 'ﾍo': 'ペ', '朮': 'ほ', 'ﾚま': 'ほ', 'ﾎ〃': 'ボ', 'ﾎo': 'ポ', 'ма': 'ま', 'мα': 'ま', '彡': 'み', '￡′': 'む', '厶': 'む', '×': 'め', 'x': 'め', 'χ': 'X', '乂': 'X', '〆': 'め', 'м○': 'も', 'мσ': 'も', '=し': 'も', '=L': 'も', 'ゃ': 
    'や', 'ャ': 'や', 'ゅ': 'ゆ', 'ュ': 'ゆ', 'ょ': 'よ', 'ョ': 'よ', '∋': 'よ', 'чo': 'よ', '∃': 'よ', 'яа': 'ら', 'b`': 'ら', 'L|': 'り', 'l)': 'り', 'ﾚ｣': 'り', 'ﾚ)': 'り', '┗』': 'り', '└丿': 'り', 'v)': 'り', '丶)': 'り', 'ゐ': 'る', 'ゑ': 'る', '儿': 'る', 'lﾚ': 'る', '｣レ': 'る', '｜ﾚ': 'る', 'ﾉﾚ': 'る', '/ﾚ': 'る', 'яё': 'れ', 'з': 'ろ', 'З': 'ろ', '回': '口', 'ゎ': 'わ', 'ヮ': 'わ', 'wα': 'わ', 'щo': 'お', 'ε': 'お', 'ω': 'ん', '冫': 'ん', 'w': 'ん', 'h': 'ん', 'ﾝ': 'ん', 'ｿ': 'ん', '〃': '濁点', '”': '濁点', '¨': '濁点', '→': 'ー', '⇒': 'ー', 'o': '。', '○': '。', 'まぢ': 'まじ', 'ッ塚': 'てゆうか', 'ッ乙ゆｳねぇ': 'て言っていて', '王見': '現', '禾斗': '科', '禾ﾑ': '私', 'ﾛ十': '叶', 'ﾃ殳': '役', 'ｲ歹ﾘ': '例', '辶斤': '近', 'ｲ廴聿': '健', 'ﾅ月': '有', 'ﾀ。': '名', '⊃i⊂': '氷', 'ﾗ|＜': '氷', '无': '天', '夲': '本', '來': '来', 'ﾈ申': '神', '走召': '超', '木木': '林', '木交': '校', '糸色': '絶', '糸及': '級', '金失': '鉄', '金矢': '鉄', '木市': '柿', 'ｲ子': '仔', '愛ιτゑ': '愛してる', '愛Uτゑ': '愛してる', '人㊥ょU': '仲良し', 'イ㊥夜歹ﾋ': '仲良し', '言身寸': '謝', '糸冬': '終', '文寸': '対', 'イ更戸斤': '便所', '木圭哥欠丈乙': '桂歌丸', '因': '大', '囚': '人', '困': '木', '圏': '巻', '圉': '幸', '囦': '水', '囝': '子', '囡': '女', '団': '寸', '囲': '井', '囮': '化', '园': '元', '図': '爪', '囨': '不', '固': '古', '囶': '八土', '国': '玉', '囹': '令', '4ほぅ圀': '四方八方', '囿': '有', '圕': '書', '圓': '員', '仲仔': '仲良し', 'Θ': '日', '曰': '日', 'Φ': '中', '㊥': '中', '升': 'チート', 'ﾃﾃ': '行', '〒〒': '行', '糸合米斗': '給料', '京尤シ舌': '就活', 'ｲ士': '仕', 'ｲ木': '休', 'ﾈ兄': '祝', '言売': '読', '谷欠': '欲', '原頁': '願', '月月': '朋', '言吾': '語', '言忍': '認', '糸売': '続', 'ｲ吏': '使', 'ﾀﾋ': '死', '㊤': '上', '㊦': '下', '㊧': '左', 'ﾅｪ': '左', '㊨': '右', '㊞': '印', 'E卩': '印'}
        testd= {'闩': 'A', '月': 'A', 'Д': 'A', 'д': 'A', '＠': 'A', 'Å': 'A', '∀': 'A', '吕': 'B', '官': 'B', '♭': 'B', 'в': 'B', 'ь': 'B', '匚': 'C', '匸': 'C', '￠': 'C', '⊂': 'C', '℃': 'C', '囙': 'D', 'ヨ': 'E', '巨': 'E', '臣': 'E', '巳': 'E', 'ㅌ': 'E', 'ё': 'E', '孒': 'F', '下': 'F', '⊂┐': 'G', 'C┐': 'G', '丩': 'H', 'н': 'H', '｜': 'L', 'し': 'J', '」': 'J', '』': 'J', '|く': 'K', 'κ': 'K', '└': 'L', '从': 
    'M', 'ﾍﾍ': 'M', '川': 'M', '瓜': 'M', 'м': 'M', '冂': 'N', '∩': 'N', 'и': 'N', 'И': 'N', '口': 'O', '○': 'O', 'ο': 'O', '尸': 'P', 'ρ': 'P', '电': 'Q', 'O、': 'Q', '尺': 'R', 'γ': 'R', 'я': 'R', 'Я': 'R', '丂': 'S', '＄': 'S', '∫': 'S', '丁': 'T', 'て': 'T', '十': 'T', 'т': 'T', '凵': 'U', 'ц': 'U', 'レ': 'V', '∨': 'V', '山': 'W', 'ш': 'W', 'щ': 'W', 'Ш': 'W', 'Щ': 'W', '×': 'X', 'ソ': 'Y', '￥': 'Y', 'ч': 'Y', 'Ч': 'Y', '乙': 'Z','≠':'き','≠″':'ぎ','ｬ':'や','｣ﾚ':'る','∪゛':'じ'}    

        new_d = {}
        nlp = spacy.load("ja_core_news_trf")
        print(nlp._path)
        # for k in sorted(gyarumoji, key=len, reverse=True):
        #     new_d[k] = gyarumoji[k]
        # for el,it in new_d.items(): 
        #     if el in textstr:
        #         break
        # for ele1,ele2 in zip(textstr,textstr[1:]):
        #             val = gyarumoji.get(ele1)
        #             val2 = gyarumoji.get(ele1+ele2)
        #             if val != None and val2 == None:
        #                 textstr = textstr.replace(ele1,new_d.get(ele1).strip())
        #             if val == None and val2 != None:
        #                 textstr = textstr.replace(ele1+ele2,new_d.get(ele1+ele2))
        #             if val != None and val2 != None:
        #                 textstr = textstr.replace(ele1+ele2,new_d.get(ele1+ele2))
        #             if val == None and val2 == None:
        #                 continue
        # print(textstr)

        
        sent=self.treat_text_to_sentences(textstr)
        # data['idioms'] =findIdioms("ja_core_news_trf","idioms_it.txt",textstr)
        # data['proverbs'] = findProverbs("proverbs_it.txt",textstr,"ja_core_news_trf")
        for phrase,index in zip(sent,range(0,len(sent))):
            data['phrase'+str(index)] = {"Phrase":phrase}
            jap_.test(phrase) #Grammar points
            # jap_.test2(phrase) # idioms
            jap_.test3(phrase) # Verbs
            # jap_.test4(phrase) # Technical jargon
            # jap_.test5(phrase) # Slang
            doc = nlp(phrase)
            for ix,token in zip(range(0,len(doc)),doc):
                print(token.text,list(token.morph), token.pos_,token.dep_)
                data[token.text] = {"pos":token.pos_}
                # if token.pos_ == "VERB":
                #     strV += token.text
                #     if doc[ix+VerbCount].pos_ == "SCONJ" or doc[ix+VerbCount].pos_ == "AUX" or doc[ix+VerbCount].pos_ == "VERB":
                #         strV += doc[ix+VerbCount].text
                #         VerbCount += 1
                #     else:
                #         break
                #     print(strV)
                #     data[token.text]['Subject']= get_subject("ja_core_news_trf",phrase)
                #     data[token.text]['Tense']=token.morph.get("Tense")
                #     data[token.text]['Infinitive'] = token.lemma_
                #     data[token.text]['Groupe']= jap_.groupeVerbe("".join(token.morph.get("Inflection")),doc[ix+1].lemma_)
                # if token.pos_ == "NOUN":
                #     data[token.text]['Number'] = token.morph.get("Number")
                #     if token.dep_ == "compound":
                #         print(token.text+doc[ix+1].text)
            
            strV = ""
        json_data = json.dumps(data,ensure_ascii=False)
        print(json_data)
        return json_data


    #traitement du portugais du portugal
    def pt(self,textstr):    
        data = {}
        nlp = spacy.load("pt_core_news_lg")
        sent=self.treat_text_to_sentences(textstr)
        # data['idioms'] =findIdioms("pt_core_news_lg","idioms_pt.txt",textstr)
        # data['proverbs'] = findProverbs("proverbs_pt.txt",textstr,"pt_core_news_lg")
        for phrase in sent:
            doc = nlp(phrase)
            for token in doc:
                print(token.text,list(token.morph), token.pos_,token.dep_)
        json_data = json.dumps(data,ensure_ascii=False)
        print(json_data)
        return json_data


    #traitement du russe
    def ru(self,textstr):    
        data = {}
        nlp = spacy.load("ru_core_news_lg")
        doc = nlp(textstr)
        for token in doc:
            print(token.text,list(token.morph), token.pos_,token.dep_)
            if token.pos_ == "VERB":
                if token.lemma_.endswith(("ю","у","ешь","ет","ем","ете","ют","ут")):
                    print(token.lemma_+" 1")
                else:
                    print(token.lemma_+" 2")
            if token.pos_ == "NOUN":
                print(token.morph.get("Case"))

        json_data = json.dumps(data,ensure_ascii=False)
        print(json_data)
        return json_data

    #traitement de l'espagnol
    def es(self,textstr):
        sdict = defaultdict(list)
        listel = list()    
        aux = Token
        aux2 = False
        data = {}
        sp = spa()
        nlp = spacy.load("es_dep_news_trf")
        sent=self.treat_text_to_sentences(textstr)
        # data['idioms'] =findIdioms("es_dep_news_trf","idioms_es.txt",textstr)
        # data['proverbs'] = findProverbs("proverbs_es.txt",textstr,"es_dep_news_trf")
        for phrase,index in zip(sent,range(0,len(sent))):
            data['phrase'+str(index)] = {"Phrase":phrase}
            # print(fra.IsPassive(phrase))
            doc = nlp(phrase)
            for ix,token in zip(range(0,len(doc)),doc):
                # print(token.text,list(token.morph), token.pos_,token.dep_)
                data[token.text] = {"pos":token.pos_}
                listel.append(token.text)
                if token.text in listel:
                    sdict[token.text].append(data[token.text])
                else:
                    sdict[token.text]=data[token.text]
                if token.pos_ == "VERB":
                    Subject= self.get_subject("es_dep_news_trf",phrase)
                    Tense=token.morph.get("Tense")
                    Person= token.morph.get("Person")
                    Number= token.morph.get("Number")
                    Next = doc[ix+1].text if doc[ix+1].text != "" else ""
                    if(token.text.endswith("e") and token.morph.get("Person") == ['1'] and token.morph.get("Number") == ['Sing'] or token.text.endswith("e") and token.morph.get("Person") == ['3'] and token.morph.get("Number") == ['Sing']):
                        Infinitive= token.text+"r"
                    else:    
                        Infinitive = token.lemma_
                    Groupe = sp.groupeVerbe(Infinitive)
                    IrregularV = sp.irregularverb_(token.lemma_)
                    VerbForm = token.morph.get("VerbForm")
                    Mood= token.morph.get("Mood")
                    print(sp.tempsVerbe(token,Groupe,Tense,Mood,aux))
                    data[token.text]['VERB']= [phrase,Subject,Tense,Person,Number,Infinitive,Groupe,IrregularV,VerbForm,Mood,Next]
                    listel.append(token.text)
                    if token.text in listel:
                        sdict[token.text].append(data[token.text]['VERB'])
                    else:
                        sdict[token.text]=data[token.text]['VERB']
                if token.pos_ == "NOUN":
                    Gender = token.morph.get("Gender")
                    Number = token.morph.get("Number")
                    IrregularN= sp.irregularnoun_(token.text)
                    Next = doc[ix+1].text if doc[ix+1].text != "" else ""
                    
                    data[token.text]['NOUN'] = [phrase,Gender,Number,IrregularN,Next]
                    listel.append(token.text)
                    if token.text in listel:
                        sdict[token.text].append(data[token.text]['NOUN'])
                    else:
                        sdict[token.text]=data[token.text]['NOUN']
                if token.pos_ == "ADJ":
                    Gender = token.morph.get("Gender")
                    Number = token.morph.get("Number")
                    Noun = doc[ix-1].text if doc[ix-1].pos_ == "NOUN" or doc[ix-1].pos_ == "PROPN" else doc[ix+1].text
                    IrregularADJ = sp.irregularadjSup_(token.text)
                    Next = doc[ix+1].text if doc[ix+1].text != "" else ""
                    
                    data[token.text]['ADJ'] = [phrase,Gender,Number,Noun,IrregularADJ,Next]
                    listel.append(token.text)
                    if token.text in listel:
                        sdict[token.text].append(data[token.text]['ADJ'])
                    else:
                        sdict[token.text]=data[token.text]['ADJ']
                if token.pos_ == "ADV":
                    Next = doc[ix+1].text if doc[ix+1].text != "" else ""
                    data[token.text]['ADV'] = [phrase,Next]
                    listel.append(token.text)
                    if token.text in listel:
                        sdict[token.text].append(data[token.text]['ADV'])
                    else:
                        sdict[token.text]=data[token.text]['ADV']
                if token.pos_ == "DET":
                    Type = ""
                    if token.morph.get("Gender") != []:
                        Gender = token.morph.get("Gender") 
                    else:
                        Gender = doc[ix+1].morph.get("Gender")
                    Number = token.morph.get("Number")
                    PronType = token.morph.get("PronType")
                    Poss = token.morph.get("Poss")
                    Next = doc[ix+1].text if doc[ix+1].text != "" else ""
                    data[token.text]['DET'] = [phrase,Type,Gender,Number,PronType,Poss,Next]
                    listel.append(token.text)
                    if token.text in listel:
                        sdict[token.text].append(data[token.text]['DET'])
                    else:
                        sdict[token.text]=data[token.text]['DET']
                if token.pos_ == "PRON":
                    Person = token.morph.get("Person")
                    DEP = token.dep_
                    Reflex = token.morph.get("Reflex")
                    Next = doc[ix+1].text if doc[ix+1].text != "" else ""
                    data[token.text]['PRON'] = [phrase,Person,DEP,Reflex,Next]
                    listel.append(token.text)
                    if token.text in listel:
                        sdict[token.text].append(data[token.text]['PRON'])
                    else:
                        sdict[token.text]=data[token.text]['PRON']
                if token.pos_ == "AUX":
                    if token.pos_ == "AUX" and doc[ix+1].pos_ == "AUX":
                        aux =  [token,doc[ix+1]]
                        print("True")
                        aux2 = True
                    else:
                        if aux2 == True:
                            continue
                        else:
                            aux = token
                            print("False")
                            aux2 = False
        
        json_data = json.dumps(data,ensure_ascii=False)
        print(json_data)
        return json_data


    #traitement du catalan
    def cat(self,textstr):
        nlp = spacy.load("ca_core_news_trf")
        doc = nlp(textstr)
        for token in doc:
            print(token.text,list(token.morph), token.pos_,token.dep_,token.lemma_)
        return "hello"

    #traitement du danois
    def dan(self,textstr):
        nlp = spacy.load("da_core_news_trf")
        doc = nlp(textstr)
        for token in doc:
            print(token.text,list(token.morph), token.pos_,token.dep_,token.lemma_)
        return "hello"

    #traitement du hollandais
    def nl(self,textstr):
        nlp = spacy.load("nl_core_news_lg")
        doc = nlp(textstr)
        for token in doc:
            print(token.text,list(token.morph), token.pos_,token.dep_,token.lemma_)
        return "hello"

    #traitement du grec moderne
    def el(self,textstr):
        nlp = spacy.load("el_core_news_lg")
        doc = nlp(textstr)
        for token in doc:
            print(token.text,list(token.morph), token.pos_,token.dep_,token.lemma_)
        return "hello"

    #traitement du lithuanien
    def lt(self,textstr):
        nlp = spacy.load("lt_core_news_lg")
        doc = nlp(textstr)
        for token in doc:
            print(token.text,list(token.morph), token.pos_,token.dep_,token.lemma_)
        return "hello"

    #traitement du macédonien
    def mk(self,textstr):
        nlp = spacy.load("mk_core_news_lg")
        doc = nlp(textstr)
        for token in doc:
            print(token.text,list(token.morph), token.pos_,token.dep_,token.lemma_)
        return "hello"

    #traitement du polonais
    def pl(self,textstr):
        nlp = spacy.load("pl_core_news_lg")
        doc = nlp(textstr)
        for token in doc:
            print(token.text,list(token.morph), token.pos_,token.dep_,token.lemma_)
        return "hello"

    #traitement du roumain
    def ro(self,textstr):
        nlp = spacy.load("ro_core_news_lg")
        doc = nlp(textstr)
        for token in doc:
            print(token.text,list(token.morph), token.pos_,token.dep_,token.lemma_)
        return "hello"

    def treat_text_to_sentences(self,textstr):
        tokens = textstr.split(" ")
        return tokens

    #creer un graphe de dependances pour le français, anglais, allemand, italien, portugais et espagnol
    def gep_tree(self,phrase,langue):
        nlp = spacy.load(langue)
        sentences = self.treat_text_to_sentences(phrase,langue)
        for sent in sentences:
            doc = nlp(sent)
            html = displacy.render(doc, style="dep", page=True)
            soup = BeautifulSoup(html, 'html.parser')
            list = soup.find_all('textpath') #for the arrows
            list2 = soup.find_all("tspan", {"class": "displacy-tag"}) # for the pos below a word
        for v in list:
            valeur = v.get_text()
            res = dict.get(valeur)
            v.string.replace_with(res)
        for b in list2:
            valeur2 = b.get_text()
            res2 = dict.get(valeur2)
            b.string.replace_with(res2)
        file_name = '-'.join([w.text for w in doc if not w.is_punct]) + ".html"
        output_path = Path(file_name)
        output_path.open("w", encoding="utf-8").write(soup.prettify())

    def findIdioms(self,langue,file,textstr):
        liste = []
        idiom_lemmata_list = []
        sentences_lemmata_list = []
        nlp = spacy.load(langue)
        with open('idioms/'+file,'r',encoding="utf-8") as f:
            idioms_list= f.readlines()
        textstring = self.treat_text_to_sentences(textstr)
        for txt in textstring:
            doc = nlp(txt)    
            strText=" ".join(sentence.lemma_.lower() for sentence in doc.sents)
            sentences_lemmata_list.append(strText)
        for idiom in idioms_list:
            doc2 = nlp(idiom)
            strIdiom=" ".join(idiom.lemma_.lower() for idiom in doc2.sents)
            idiom_lemmata_list.append(strIdiom)

        for index in range(0,len(sentences_lemmata_list)):
            strsent=sentences_lemmata_list[index]   
            for index_ in range(0,len(idiom_lemmata_list)):
                if idiom_lemmata_list[index_] in strsent:
                    if liste.count(idioms_list[index_]) == 0:
                        liste.append(idioms_list[index_].strip())
        return liste


    #obtenir le sujet d'une phrase
    def get_subject(lang,sentence):
        nlp = spacy.load(lang)
        doc = nlp(sentence)
        sentence = next(doc.sents) 
        for word in sentence:
            if word.dep_ == "nsubj":
                return word.text