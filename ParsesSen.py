class ParsesSen:
    def __init__(self, parses_sen):
        self.__parses_sen: list = parses_sen

    def __len__(self):
        return len(self.__parses_sen)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return None
        return self.__parses_sen[item]

    def __add__(self, other):
        if isinstance(other, VariationsParse):
            self.__parses_sen.append(other)
            return self
        raise ValueError("СЮДА НУЖНО VARIATIONSPARSE АУТИСТ")

    def __sub__(self, other):
        if isinstance(other, VariationsParse):
            try:
                self.__parses_sen.pop(self.__parses_sen.index(VariationsParse))
                return self
            except ValueError:
                pass
        raise ValueError("СЮДА НУЖНО VARIATIONSPARSE АУТИСТ")

    def append(self, other):
        if isinstance(other, VariationsParse):
            self.__parses_sen.append(other)
        raise ValueError("СЮДА НУЖНО VARIATIONSPARSE АУТИСТ")

    def remove(self, other):
        if isinstance(other, VariationsParse):
            try:
                self.__parses_sen.pop(self.__parses_sen.index(VariationsParse))
            except ValueError:
                pass
        raise ValueError("СЮДА НУЖНО VARIATIONSPARSE АУТИСТ")

    def index(self, other):
        for i in range(len(self.__parses_sen)):
            if self.__parses_sen[i].index(other) != -1:
                return i
        return -1


class VariationsParse:
    def __init__(self, vari):
        self.__vari: list = vari

    def __iter__(self):
        return iter(self.__vari)

    def __add__(self, other):
        if isinstance(other, list):
            for el in other:
                self.__vari.append(el)
        self.__vari.append(other)
        return self

    def __sub__(self, other):
        if self.__vari.index(other) != -1:
            self.__vari.pop(self.__vari.index(other))
            return self

    def __getitem__(self, item):
        return self.__vari[item]

    def append(self, other):
        self.__vari.append(other)

    def remove(self, other):
        try:
            self.__vari.pop(self.__vari.index(other))
        except ValueError:
            pass

    def index(self, other):
        try:
            return self.__vari.index(other)
        except ValueError:
            return -1
