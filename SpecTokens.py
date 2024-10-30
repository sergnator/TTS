import pymorphy3
from fuzzywuzzy import process, fuzz

from ParsesSen import *


class DictionaryTokens:
    def __init__(self):
        self.__dict_spec_word = {}
        self.__morh = pymorphy3.MorphAnalyzer(lang="ru")
        self.__parses = None

    def __create_spec_token(self, normal_form_word, func):
        self.__dict_spec_word[normal_form_word] = func

    def analyse(self, sen: list[str]):
        parses_sen = self.__morhfil(sen)
        self.__parses = parses_sen
        for i in range(len(parses_sen)): # ЛУЧШИЙ ЯЗЫК В МИРЕ
            for p in parses_sen[i]:
                word_and_prec = process.extractOne(p.normal_form, list(self.__dict_spec_word.keys()))
                if word_and_prec[1] > 60:
                    self.__parses = parses_sen
                    self.__dict_spec_word[word_and_prec[0]](parses_sen, sen, i)

    def spec_token(self, normal_form): # декоратор, который добавляет специальную команду
        def wrapper(func):
            self.__create_spec_token(normal_form, func)
            return func

        return wrapper

    def __morhfil(self, text: list[str]) -> ParsesSen:
        res = []
        for word in text:
            p = self.__morh.parse(word)
            if p[0].score > 0.6:
                res.append(VariationsParse([p[0]]))
                continue
            else:
                res.append(VariationsParse(p))

        return ParsesSen(res)

    def search_first(self, search, tags=None): # ищет слово в предложении
        tags = [] if tags is None else tags
        for i in range(len(self.__parses)):
            for p in self.__parses[i]:
                if all([tag in p.tag for tag in tags]):
                    prec = fuzz.ratio(p.normal_form, search)
                    if prec > 50:
                        return p

    def searchs_first(self, searchs, tags=None, all_=False):  # ищет слова в предложении, all_ ищет все совпадения
        r = []
        tags = [] if tags is None else tags
        for i in range(len(self.__parses)):
            for p in self.__parses[i]:
                if all([tag in p.tag for tag in tags]):
                    word_and_prec = process.extractOne(p.normal_form, searchs)
                    if word_and_prec[1] > 60:
                        if all_:
                            r.append(word_and_prec[0])
                            continue
                        return [word_and_prec[0]]
        return r


