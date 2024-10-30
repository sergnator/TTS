from SpecTokens import DictionaryTokens

import os

d = DictionaryTokens()

dict_of_programs = {"блокнот": r"C:\WINDOWS\system32\notepad.exe", "слово": r"C:\WINDOWS\system32\notepad.exe",
                    "калькулятор": "calc.exe"}


@d.spec_token("открыть")
def open_program(parses, text, i):
    keys = list(dict_of_programs.keys())
    key = d.searchs_first(keys, all_=True)
    [os.startfile(dict_of_programs[k]) for k in key]


d.analyse(input().split())
