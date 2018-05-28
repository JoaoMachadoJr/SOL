from SOL_TWITTER.entities import Entities
from SOL_TWITTER.media import Media, Size
from SOL_TWITTER.place import Place, PlaceAttributes, BoundingBox
from SOL_TWITTER.tweet import Tweet
from SOL_TWITTER.user import User


def criaclasse(obj):
    dic = obj.__dict__
    lista = list()
    for aKey in dic.keys():
        novo_dict = dict()
        novo_dict["campo"] = aKey
        novo_dict["str"] = (dic[aKey] == "") or (aKey=="id")
        lista.append(novo_dict)
    for i in lista:
        if i["str"]:
            print("        self.__"+i["campo"]+" = \"\"")
        else:
            print("        self.__"+i["campo"]+" = None")
    print("")
    print("")
    for i in lista:
        if i["str"]:
            print("    @property")
            print("    def "+i["campo"]+"(self) -> str:")
            print("        \"\"\"Descricao\"\"\"")
            print("        return self.__"+i["campo"]+"")
            print("")
            print("    @"+i["campo"]+".setter")
            print("    def "+i["campo"]+"(self, val: str):")
            print("        self.__"+i["campo"]+" = val")
        else:
            print("    @property")
            print("    def " + i["campo"] + "(self) -> Obj:")
            print("        \"\"\"Descricao\"\"\"")
            print("        return self.__" + i["campo"] + "")
            print("")
            print("    @" + i["campo"] + ".setter")
            print("    def " + i["campo"] + "(self, val: Obj):")
            print("        self.__" + i["campo"] + " = val")


criaclasse(User())
