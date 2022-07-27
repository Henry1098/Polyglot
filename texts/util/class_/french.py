from bs4 import element
from spacy.tokens import Token
import spacy
import re
from nltk.tokenize import sent_tokenize
from spacy.matcher import Matcher
from spacy.lang.fr import French

class French:
    verbe3 = []
    irregularadj = []
    irregularverb = []
    irregularnouns = []
    irregularadverb = []
    conjunctions = []
    interjection =[]
    multiwords = []
    phrases = []
    nlp = French()
    
    conjugaisonV1 = {
    "e":"Présent",
    "es":"Présent",
    "ons": "Présent",
    "ez": "Présent",
    "ent":"Présent",
    "ais":"Imparfait",
    "ait":"Imparfait",
    "ions":"Imparfait",
    "iez":"Imparfait",
    "aient":"Imparfait",
    "erai":"Le futur simple",
    "eras":"Le futur simple",
    "era":"Le futur simple",
    "eront":"Le futur simple",
    "erez":"Le futur simple",
    "eront":"Le futur simple",
    "ai":"Passé simple",
    "as":"Passé simple",
    "a":"Passé simple",
    "âmes":"Passé simple",
    "âtes":"Passé simple",
    "èrent":"Passé simple",
    "rai":"Conditionnel",
    "ras":"Conditionnel",
    "ra":"Conditionnel",
    "rons":"Conditionnel",
    "rez":"Conditionnel",
    "ront":"Conditionnel",
    "sse":"Imparfait du Subjonctif",
    "sses":"Imparfait du Subjonctif",
    "ât":"Imparfait du Subjonctif",
    "ssions":"Imparfait du Subjonctif",
    "ssiez":"Imparfait du Subjonctif",
    "ssent":"Imparfait du Subjonctif",
    "é":"Participe Passé",
    "ée":"Participe Passé",
    "és":"Participe Passé",
    "ées":"Participe Passé"

    }

    conjugaisonV2 = {
    "is":"Présent",
    "it":"Présent",
    "issons":"Présent",
    "issez":"Présent",
    "issent":"Présent",
    "ais":"Imparfait",
    "ait":"Imparfait",
    "ions":"Imparfait",
    "iez":"Imparfait",
    "aient":"Imparfait",
    "irai":"Le futur simple",
    "iras":"Le futur simple",
    "ira":"Le futur simple",
    "iront":"Le futur simple",
    "irez":"Le futur simple",
    "iront":"Le futur simple",
    "îmes":"Passé simple",
    "îtes":"Passé simple",
    "irent":"Passé simple",
    "rai":"Conditionnel",
    "ras":"Conditionnel",
    "ra":"Conditionnel",
    "rons":"Conditionnel",
    "rez":"Conditionnel",
    "ront":"Conditionnel",
    "sse":"Imparfait du Subjonctif",
    "sses":"Imparfait du Subjonctif",
    "ît":"Imparfait du Subjonctif",
    "ssions":"Imparfait du Subjonctif",
    "ssiez":"Imparfait du Subjonctif",
    "ssent":"Imparfait du Subjonctif",
    "ïssons":"Présent",
    "ïssez":"Présent",
    "ïssent":"Présent",
    "i":"Participe Passé",
    "ie":"Participe Passé",
    "is":"Participe Passé",
    "ies":"Participe Passé"
    }

    conjugaisonV3 = {
    "s":"Présent",
    "ds":"Présent",
    "ds":"Présent",
    "d":"Présent",
    "x":"Présent",
    "x":"Présent",
    "t":"Présent",
    "is":"Présent",
    "it":"Présent",
    "ons": "Présent",
    "ez": "Présent",
    "ent":"Présent",
    "ais":"Imparfait",
    "ait":"Imparfait",
    "ions":"Imparfait",
    "iez":"Imparfait",
    "aient":"Imparfait",
    "rai":"Le futur simple",
    "ras":"Le futur simple",
    "ra":"Le futur simple",
    "ront":"Le futur simple",
    "rez":"Le futur simple",
    "ront":"Le futur simple",
    "îmes":"Passé simple",
    "îtes":"Passé simple",
    "irent":"Passé simple",
    "ûtes":"Passé simple",
    "urent":"Passé simple",
    "ûs":"Passé simple",
    "ût":"Passé simple",
    "ûmes":"Passé simple",
    "ûtes":"Passé simple",
    "ûrent":"Passé simple",
    "ins":"Passé simple",
    "int":"Passé simple",
    "înmes":"Passé simple",
    "întes":"Passé simple",
    "inrent":"Passé simple",
    "rai":"Conditionnel",
    "ras":"Conditionnel",
    "ra":"Conditionnel",
    "rons":"Conditionnel",
    "rez":"Conditionnel",
    "ront":"Conditionnel",
    "sse":"Imparfait du Subjonctif",
    "sses":"Imparfait du Subjonctif",
    "ît":"Imparfait du Subjonctif",
    "înt":"Imparfait du Subjonctif",
    "ssions":"Imparfait du Subjonctif",
    "ssiez":"Imparfait du Subjonctif",
    "ssent":"Imparfait du Subjonctif",
    "i":"Participe Passé",
    "ie":"Participe Passé",
    "is":"Participe Passé",
    "ies":"Participe Passé",
    "u":"Participe Passé",
    "ue":"Participe Passé",
    "us":"Participe Passé",
    "ues":"Participe Passé",
    "s":"Participe Passé",
    "se":"Participe Passé",
    "ses":"Participe Passé",
    "t":"Participe Passé",
    "te":"Participe Passé",
    "ts":"Participe Passé",
    "tes":"Participe Passé",
    "dû":"Participe Passé"
    }



    
    typearticle = {
    "le":"Definite article (Male)",
    "la":"Definite article (Female)",
    "l": "Definite article (Male/Female before Vowel or h muet)",
    "les":"Definite article plural (Male/Female)",
    "un":"Indefinite article (Male)",
    "une":"Indefinite article (Female)",
    "des":"Indefinite/Partitive article plural (Male/Female)",
    "du":"Partitive article (Male)",
    "de la": "Partitive article (Female)",
    "de l":"Partitive article (before Vowel or h muet)",
    }

    avoir = {
    "avoir":"infinitive",
    "ai":"Présent",
    "as":"Présent",
    "a":"Présent",
    "avons":"Présent",
    "avez":"Présent",
    "ont":"Présent",
    "avais":"Imparfait",
    "avais":"Imparfait",
    "avait":"Imparfait",
    "avions":"Imparfait",
    "aviez":"Imparfait",
    "avaient":"Imparfait",
    "eus":"Passé simple",
    "eut":"Passé simple",
    "eûmes":"Passé simple",
    "eûtes":"Passé simple",
    "eurent":"Passé simple",
    "aurai":"Futur simple",
    "auras":"Futur simple",
    "aura":"Futur simple",
    "aurons":"Futur simple",
    "aurez":"Futur simple",
    "auront":"Futur simple",
    "aurais":"Conditionnel",
    "aurait":"Conditionnel",
    "aurions":"Conditionnel",
    "auriez":"Conditionnel",
    "auraient":"Conditionnel",
    "aie":"Subjonctif Présent",
    "aies":"Subjonctif Présent",
    "ait":"Subjonctif Présent",
    "ayons":"Subjonctif Présent",
    "ayez":"Subjonctif Présent",
    "aient":"Subjonctif Présent",
    "eusse":"Imparfait du Subjonctif",
    "eusses":"Imparfait du Subjonctif",
    "eût":"Imparfait du Subjonctif",
    "eussions":"Imparfait du Subjonctif",
    "eussiez":"Imparfait du Subjonctif",
    "eussent":"Imparfait du Subjoncitf",
    "ai_eu":"Passé Composé",
    "as_eu":"Passé Composé",
    "a_eu":"Passé Composé",
    "avons_eu":"Passé Composé",
    "avez_eu":"Passé Composé",
    "ont_eu":"Passé Composé",
    "avais_eu":"Plus-que-parfait",
    "avait_eu":"Plus-que-parfait",
    "avions_eu":"Plus-que-parfait",
    "aviez_eu":"Plus-que-parfait",
    "avaient_eu":"Plus-que-parfait",
    "eus_eu":"Passé Antérieur",
    "eut_eu":"Passé Antérieur",
    "eûmes_eu":"Passé Antérieur",
    "eûtes_eu":"Passé Antérieur",
    "eurent_eu":"Passé Antérieur",
    "aurai_eu":"Futur Antérieur",
    "auras_eu":"Futur Antérieur",
    "aura_eu":"Futur Antérieur",
    "aurons_eu":"Futur Antérieur",
    "aurez_eu":"Futur Antérieur",
    "auront_eu":"Futur Antérieur",
    "eusse_eu":"Plus-que-parfait",
    "eusses_eu":"Plus-que-parfait",
    "eût_eu":"Plus-que-parfait",
    "eussions_eu":"Plus-que-parfait",
    "eussiez_eu":"Plus-que-parfait",
    "eussent_eu":"Plus-que-parfait",
    "aie_eu":"Passé Antérieur",
    "aies_eu":"Passé Antérieur",
    "ait_eu":"Passé Antérieur",
    "ayons_eu":"Passé Antérieur",
    "ayez_eu":"Passé Antérieur",
    "aient_eu":"Passé Antérieur",
    "aurais_eu":"Conditionnel",
    "aurait_eu":"Conditionnel",
    "aurions_eu":"Conditionnel",
    "auriez_eu":"Conditionnel",
    "auraient_eu":"Conditionnel",
    "ayant_eu":"Participe Passé Composé",
    "eu":"Participe Passé",
    "eus":"Participe Passé",
    "eue":"Participe Passé",
    "eues":"Participe Passé",
    "aie_eu":"Impératif Passé",
    "ayons_eu":"Impératif Passé",
    "ayez_eu":"Impératif Passé",
    "avoir_eu":"Infinitive Passé"
        }

    etre = {
    "être":"Infinitive",
    "suis":"Présent",
    "es":"Présent",
    "est":"Présent",
    "sommes":"Présent",
    "êtes":"Présent",
    "sont":"Présent",
    "étais":"Imparfait",
    "était":"Imparfait",
    "étions":"Imparfait",
    "étiez":"Imparfait",
    "étaient":"Imparfait",
    "fus":"Passé simple",
    "fûmes":"Passé simple",
    "fûtes":"Passé simple",
    "furent":"Passé simple",
    "serai":"Futur simple",
    "seras":"Futur simple",
    "sera":"Futur simple",
    "serons":"Futur simple",
    "serez":"Futur simple",
    "seront":"Futur simple",
    "serais":"Conditionnel",
    "serait":"Conditionnel",
    "serions":"Conditionnel",
    "seriez":"Conditionnel",
    "seraient":"Conditionnel",
    "sois":"Subjonctif Présent",
    "soit":"Subjonctif Présent",
    "soyons":"Subjonctif Présent",
    "soyez":"Subjonctif Présent",
    "soient":"Subjonctif Présent",
    "fusse":"Imparfait du Subjonctif",
    "fusses":"Imparfait du Subjonctif",
    "fût":"Imparfait du Subjonctif",
    "fussions":"Imparfait du Subjonctif",
    "fussiez":"Imparfait du Subjonctif",
    "fussent":"Imparfait du Subjonctif",
    "ai_été":"Passé Composé",
    "as_été":"Passé Composé",
    "a_été":"Passé Composé",
    "avons_été":"Passé Composé",
    "avez_été":"Passé Composé",
    "ont_été":"Passé Composé",
    "avais_été":"Plus-que-parfait",
    "avait_été":"Plus-que-parfait",
    "avions_été":"Plus-que-parfait",
    "aviez_été":"Plus-que-parfait",
    "avaient_été":"Plus-que-parfait",
    "eus_été":"Passé Antérieur",
    "eut_été":"Passé Antérieur",
    "eûmes_été":"Passé Antérieur",
    "eûtes_été":"Passé Antérieur",
    "eurent_été":"Passé Antérieur",
    "aurai_été":"Futur Antérieur",
    "auras_été":"Futur Antérieur",
    "aura_été":"Futur Antérieur",
    "aurons_été":"Futur Antérieur",
    "aurez_été":"Futur Antérieur",
    "auront_été":"Futur Antérieur",
    "esse_été":"Plus-que-parfait",
    "esses_été":"Plus-que-parfait",
    "eût_été":"Plus-que-parfait",
    "essions_été":"Plus-que-parfait",
    "essiez_été":"Plus-que-parfait",
    "essent_été":"Plus-que-parfait",
    "aie_été":"Passé Antérieur",
    "aies_été":"Passé Antérieur",
    "ait_été":"Passé Antérieur",
    "ayons_été":"Passé Antérieur",
    "ayez_été":"Passé Antérieur",
    "aient_été":"Passé Antérieur",
    "aurais_été":"Condtionnel Passé",
    "aurait_été":"Conditionnel Passé",
    "aurions_été":"Conditionnel Passé",
    "auriez_été":"Conditionnel Passé",
    "auraient_été":"Conditionnel Passé",
    "ayant_été":"Participe Passé Composé",
    "été":"Participe Passé",
    "aie_été":"Impératif Passé",
    "ayons_été":"Impératif Passé",
    "ayez_été":"Impératif Passé",
    "avoir_été":"Infinitif Passé"
    }    

    temps={
        ("Conditionnel","Participe Passé"):"Conditionnel Passé",
        ("Futur simple","Participe Passé"):"Futur Antérieure",
        ("Présent","Participe Passé"):"Passé Composé",
        ("Passé simple","Participe Passé"):"Passé Antérieure",
        ("Subjonctif Présent","Participe Passé"):"Subjonctif Passé",
        ("Imparfait","Participe Passé"):"Plus-que-parfait",
        ("Imparfait du Subjonctif","Participe Passé"):"Plus-que-parfait Subjonctif",
        ("Infinitive","Participe Passé"):"Infinitive Passé",
        ("Impératif","Participe Passé"):"Impératif Passé"
    }

    tempsPassive={
        ("Présent","Participe Passé"):"Présent Voix passive",
        ("Futur simple","Participe Passé"):"Futur Voix passive",
        ("Passé simple","Participe Passé"):"Passé simple Voix passive",
        ("Passé Composé","Participe Passé"):"Passé Composé Voix passive",
        ("Imparfait","Participe Passé"):"Imparfait Voix passive",
        ("Plus-que-parfait","Participe Passé"):"Plus-que-parfait Voix passive",
        ("Passé Antérieur","Participe Passé"):"Passé Antérieur Voix passive",
        ("Futur Antérieur","Participe Passé"):"Futur Antérieur Voix passive",
        ("Conditionnel","Participe Passé"):"Conditionnel Voix passive",
        ("Conditionnel Passé","Participe Passé"):"Conditionnel Passé Voix passive",
        ("Subjonctif Présent","Participe Passé"):"Subjonctif Présent Voix passive",
        ("Subjonctif Passé","Participe Passé"):"Subjonctif Passé Voix passive",
        ("Imparfait du Subjonctif","Participe Passé"):"Imparfait du Subjonctif Voix passive",
        ("Plus-que-parfait du Subjonctif","Participe Passé"):"Plus-que-parfait du Subjonctif Voix passive",
        ("Impératif","Participe Passé"):"Impératif Voix passive",
        ("Infinitive","Participe Passé"):"Infinitive Voix passive",
        ("Infinitive Passé","Participe Passé"):"Infinitive Passé Voix passive",
        ("Participe Présent","Participe Passé"):"Participe Présent Voix passive",
        ("Participe Passé","Participe Passé"):"Participe Passé Voix passive",
        ("Gérondif Présent","Participe Passé"):"Gérondif Présent Voix passive",
        ("Gérondif Passé","Participe Passé"):"Gérondif Passé Voix passive"
    }

    DemAdj = {
        "ce":"Adjective démonstrative - Masculine Singulier",
        "cet":"Adjective démonstrative - Masculine Singulier (Avant Voyelle)",
        "cette":"Adjective démonstrative - Feminine Singulier", 
        "ces":"Adjective démonstrative - Masculine/Feminine Pluriel"
    }

    PossPron = {
        "le mien":"Masculine Singulier" ,
"le tien":"Masculine Singulier" ,
"le sien":"Masculine Singulier" ,
"le nôtre":"Masculine Singulier" ,
"le vôtre":"Masculine Singulier" ,
"le leur":"Masculine Singulier" ,
"la mienne": "Féminin Singulier",
"la tienne": "Féminin Singulier",
"la sienne": "Féminin Singulier",
"la nôtre": "Féminin Singulier",
"la vôtre": "Féminin Singulier",
"la leur": "Féminin Singulier",
"les miens": "Masculine Pluriel",
"les tiens": "Masculine Pluriel",
"les siens": "Masculine Pluriel",
"les miennes":"Feminin Pluriel",
"les tiennes":"Feminin Pluriel",
"les siennes":"Feminin Pluriel",
"les nôtres": "Masculine/Feminin Pluriel",
"les vôtres": "Masculine/Feminin Pluriel",
"les leurs": "Masculine/Feminin Pluriel"
    }
    
    compounddemPron = {
        "celui-ci":"Masculin Singulier",
        "celui-là":"Masculin Singulier",
        "celle-ci":"Feminin Singulier",
        "celle-là":"Feminin Singulier",
        "ceux-ci":"Masculin Pluriel",
        "ceux-là":"Masculin Pluriel",
        "celles-ci":"Feminin Pluriel",
        "celles-là":"Feminin Pluriel    "
    }

    pronomrelatif = {
    "duquel":"Maculin Singulier",
    "duquels":"Masculin Pluriel",
    "de laquelle":"Feminin Pluriel",
    "desquelles":"Feminin Pluriel"
}
    
    def __init__(self) -> None:
        with open('other_files/fr/3rdgroupeverbs_fr.txt','r',encoding="utf-8") as f:
            self.verbe3=[i.strip() for i in f.readlines()]
        with open('other_files/fr/conj_fr.txt','r',encoding="utf-8") as f2:
            self.conjunctions=[i.strip() for i in f2.readlines()]
        with open('other_files/fr/interj_fr.txt','r',encoding="utf-8") as f3:
            self.interjection=[i.strip() for i in f3.readlines()]
        with open('other_files/fr/irradj_fr.txt','r',encoding="utf-8") as f4:
            self.irregularadj=[i.strip() for i in f4.readlines()]
        with open('other_files/fr/irradv_fr.txt','r',encoding="utf-8") as f5:
            self.irregularadverb=[i.strip() for i in f5.readlines()]
        with open('other_files/fr/irrnouns_fr.txt','r',encoding="utf-8") as f6:
            self.irregularnouns=[i.strip() for i in f6.readlines()]
        with open('other_files/fr/irrverb_fr.txt','r',encoding="utf-8") as f7:
            self.irregularverb=[i.strip() for i in f7.readlines()]
        with open('other_files/fr/multiw_fr.txt','r',encoding="utf-8") as f8:
            self.multiwords=[i.strip() for i in f8.readlines()]
        with open('other_files/fr/phrases_fr.txt','r',encoding="utf-8") as f9:
            self.phrases=[i.strip() for i in f9.readlines()]
        nlp = spacy.load("fr_dep_news_trf")



    def modify_sent(self,phrase):
        phrase2 =""
        phrase3 =""
        if "te" in phrase:
            phrase2=str.replace(phrase,"te","se")
            self.liste.append("te")
        if "tes" in phrase:
            phrase2=str.replace(phrase,"tes","ses")
            self.liste.append("tes")
        if "me" in phrase:
            phrase2=str.replace(phrase,"me","se")
            self.liste.append("me")
        if "mes" in phrase:
            phrase2=str.replace(phrase,"mes","ses")
            self.liste.append("mes")
        
        for element in range(0, len(phrase2)):
            if phrase2[element] == "'" and phrase2[element-1] == "t":
                phrase3 = phrase2[0:element-1]+'s'+phrase2[element:]
                self.liste.append("t")
            if phrase2[element] == "'" and phrase2[element-1] == "m":
                phrase3 = phrase2[0:element-1]+'s'+phrase2[element:]
                self.liste.append("m")

        return phrase3

    def irregularadj_(self,tokens):
        if tokens in self.irregularadj:
            return "True"
        else:
            return "False"    
    
    def irregularverb_(self,tokens):
        if tokens in self.irregularverb:
            return "True"
        else:
            return "False"   

    def irregularnoun_(self,token):
        if token in self.irregularnouns:
            return "True"
        else:
            return "False"

    def irregularadverb_(self,token):
        if token in self.irregularadverb:
            return "True"
        else:
            return "False"
    
    def determiner(self,token):

        if not token.isalpha():
            if len(token) == 2 and token[0] == "l":
                token = "l"
            if len(token) == 5 and token[0] == "d":
                token = "de l"
    
        if token in self.typearticle:
            return self.typearticle.get(token)
        else:
            return "False"

    def groupeVerbe(self,token_):
        groupeVerbe = 4
        strLemmaF = ""
        strLemmaF = token_[-2:]
        strLemma = token_

        if strLemma == "être" or strLemma == "avoir":
            groupeVerbe = 0
        if strLemma in self.verbe3:
            groupeVerbe = 3
        if strLemmaF == "er" and strLemma != "aller":
            groupeVerbe = 1
        if strLemma not in self.verbe3 and strLemmaF is "ir":
            groupeVerbe = 2
        return groupeVerbe

    def tempsVerbe(self,token,groupe,tense,mood,aux):
        strTemp = ""
        str = token.text
        strFinal = ""
        strT = ""
        if type(aux) is not list:
            strAux = aux.text
            strAuxDep = aux.dep_
        else:
            strAux = ""
        if groupe == 0:
            if str in self.avoir:
                strT = self.avoir.get(str)
            if str in self.etre:
                strT = self.etre.get(str)
            strFinal = strT
        if groupe == 1:
            if str == token.lemma_ and token.lemma_.endswith("er"):
                return "Infinitive"

            for tmps in sorted(self.conjugaisonV1.keys(),key=len,reverse=True):
                if str.endswith(tmps):
                    strTemp=self.conjugaisonV1.get(tmps)
                    break
        if groupe == 2:
            for tmps in sorted(self.conjugaisonV2.keys(),key=len,reverse=True):
                if str.endswith(tmps):
                    strTemp=self.conjugaisonV2.get(tmps)
                    break
        if groupe == 3:            
            for tmps in sorted(self.conjugaisonV3.keys(),key=len,reverse=True):
                if str.endswith(tmps):
                    strTemp=self.conjugaisonV3.get(tmps)
                    break
        if strTemp == "Présent" and tense == ['Past']:
            strTemp = "Passé simple"
        if mood == ['IMP'] and tense == ['Pres']:
            strTemp = "Impératif"

        if strAux != "" and strTemp != "" and type(aux) is not list:
            if strAux in self.avoir:
                strT = self.avoir.get(aux.text)
                strFinal = self.temps.get((strT,strTemp))
            if strAux in self.etre:
                strT = self.etre.get(aux.text)
                if strAuxDep == "aux:pass":
                    strFinal = self.tempsPassive.get((strT,strTemp))
                else:
                    strFinal = self.temps.get((strT,strTemp))
            
        if strAux != "" and strTemp == "" and type(aux) is not list:
            if strAux in self.avoir:
                strT = self.avoir.get(aux.text)
            if strAux in self.etre:
                strT = self.etre.get(aux.text)
            strFinal = strT
        if type(aux) is list:
            str = aux[0].text.strip()+"_"+aux[1].text.strip()
            if aux[1].lemma_ == "avoir":
                strTemp2 = self.avoir.get(str)
            if aux[1].lemma_ == "être":
                strTemp2 = self.etre.get(str)
            strFinal = self.tempsPassive.get((strTemp2,strTemp))
        return strFinal if aux != None else strTemp

    def ImparfaitSubjonctif(self,token):
       for el in self.etre: 
        if token.lemma_ == "être" and token.text == el:
            if self.etre.get(el) == "Imparfait du Subjonctif":
                return True
       for el2 in self.avoir:
        if token.lemma_ == "avoir" and token.text == el2:
            if self.etre.get(el2) == "Imparfait du Subjonctif":
                return True
       return False 

    def Impératif(self,token):
        if token.lemma_ == "être" and token.text == "sois" or token.text == "soyons" or token.text == "soyez":
                return True
        if token.lemma_ == "avoir" and token.text == "aie" or token.text == "ayons" or token.text == "ayez":
                return True
        return False

    def IsPassive(self,phrase):
        count = 0
        doc = self.nlp(phrase)
        print("Number of Sentences = ",len(doc))
        for token in doc:
                if token.pos_ == "NOUN" and token.dep_=="nsubj:pass":
                  count = count + 1
                if token.pos_ == "AUX" and token.lemma_ == "être" and token.dep_ =="aux:pass":
                  count = count + 1
        if count == 2:
            return True
        else:
            return False
    
    def ContainsRefPron(self,phrase):
        Type = ""
        count = 0
        count2 = 0
        doc = self.nlp(phrase)
        sents = list(doc.sents)
        print("Number of Sentences = ",len(sents))
        for sent in doc.sents:
            for token in sent:
                if token.pos_ == "PRON" and token.morph.get("Reflex")== ["Yes"] and token.dep_== "expl:comp":
                    Type = "Verbe Réflechi"
                if token.dep_ == "nsubj" and token.morph.get("Number") == ['Plur']:
                    count = count + 1
                if token.pos_ == "PRON" and token.text.lower() == ("nous","vous","se") and token.morph.get("Reflex") == ['Yes']:
                    count = count + 1
                if token.dep_ == "nsubj" and token.morph.get("Person") == ['3'] and token.morph.get("Number") == ['Sing']:
                    count2 = count2 + 1
                if token.pos_ == "PRON" and token.text.lower() == "se" and token.morph.get("Reflex") == ['Yes'] and token.morph.get("Person") == ['3']:
                    count2 = count2 + 1
                if token.pos_ == "PRON" and token.dep_ == "obj":
                    Type = "Pronom objet direct"
                if token.pos_ == "PRON" and token.dep_ == "iobj":
                    Type = "Pronom objet indirect"
                if token.pos_ == "PRON" and token.dep_ == "iobj" and token.text =="y":
                    Type ="Pronom Y"
                if token.pos_ == "PRON" and token.dep_ == "iobj" and token.text =="en":
                    Type ="Pronom en"
        if count == 2:
            Type = "Verbe récriproque"
        if count2 == 2:
            Type = "Pronominal passive"
            return Type
    
    def SupComp(self,phrase):
        print("Number of Sentences = ",len(phrase))
       
    def AdjDem(self,text):
        if (self.DemAdj.keys()) in text:
            return True
    
    def PossPron(self,phrase):
        for pron in self.PossPron:
            if pron in phrase:
                return True
            else:
                return False