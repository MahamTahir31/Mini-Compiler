Scope_Table = []
Definition_Table = []
Scope_Stack = [0]
highestScope = 0
typeCompatibility = {
    "intint+": "int",
    "intint-": "int",
    "intint*": "int",
    "intint/": "int",
    "intint%": "int",
    "intint=": "int",
    "intint==": " bool",
    "intint!=": "bool",
    "intint<=": "bool",
    "intint<": "bool",
    "intint>": "bool",
    "intint>=": "bool",
    "intfloat+": "float",
    "intfloat-": "float",
    "intfloat*": "float",
    "intfloat/": "float",
    "intfloat=": "int",
    "intfloat==": "bool",
    "intfloat!=": "bool",
    "intfloat<=": "bool",
    "intfloat<": "bool",
    "intfloat>": "bool",
    "intfloat>=": "bool",
    "intchar+": "int",
    "intchar-": "int",
    "intchar*": "int",
    "intchar/": "int",
    "intchar%": "int",
    "intchar=": "int",
    "intchar==": "bool",
    "intchar!=": "bool",
    "intchar<=": "bool",
    "intchar<": "bool",
    "intchar>": "bool",
    "intchar>=": "bool",
    "intbool+": "int",
    "intbool-": "int",
    "intbool*": "int",
    "intbool/": "int",
    "intbool%": "int",
    "intbool=": "int",
    "intbool==":  "bool",
    "intbool!=": "bool",
    "intbool<=": "bool",
    "intbool<": "bool",
    "intbool>": "bool",
    "intbool>=": "bool",
    "floatfloat+": "float",
    "floatfloat-": "float",
    "floatfloat*": "float",
    "floatfloat/": "float",
    "floatfloat=": "float",
    "floatfloat==": "bool",
    "floatfloat!=": "bool",
    "floatfloat<=": "bool",
    "floatfloat<": "bool",
    "floatfloat>": "bool",
    "floatfloat>=": "bool",
    "floatchar+": "float",
    "floatchar-": "float",
    "floatchar*": "float",
    "floatchar/": "float",
    "floatchar%": "float",
    "floatchar=": "float",
    "floatchar==": "bool",
    "floatchar!=": "bool",
    "floatchar<=": "bool",
    "floatchar<": "bool",
    "floatchar>": "bool",
    "floatchar>=": "bool",
    "floatbool+": "float",
    "floatbool-": "float",
    "floatbool*": "float",
    "floatbool/": "float",
    "floatbool=": "bool",
    "floatbool==": "bool",
    "floatbool!=": "bool",
    "floatbool<=": "bool",
    "floatbool<": "bool",
    "floatbool>": "bool",
    "floatbool>=": "bool",
    "stringstring+": "str",
    "stringstring=":  "str",
    "stringstring==": "bool",
    "stringstring!=": "bool",
    "stringstring<=": "bool",
    "stringstring<": "bool",
    "stringstring>": "bool",
    "stringstring>=": "bool",
    "stringint=": "int",
    "stringfloat=": "int",
    "stringchar+": "str",
    "stringchar=": "str",
    "stringbool=": "str",
    "charchar+": "int",
    "charchar-": "int",
    "charchar*": "int",
    "charchar/": "int",
    "charchar%": "int",
    "charchar=": "char",
    "charchar==": "bool",
    "charchar!=": "bool",
    "charchar<=": "bool",
    "charchar<": "bool",
    "charchar>": "bool",
    "charchar>=": "bool",
    "charint+": "char",
    "charint-": "char",
    "charint*": "char",
    "charint/": "char",
    "charint%": "int",
    "charint=": "char",
    "charint==": "bool",
    "charint!=": "bool",
    "charint<=": "bool",
    "charint<": "bool",
    "charint>": "bool",
    "charint>=": "bool",
    "charfloat+": "float",
    "charfloat-": "float",
    "charfloat*": "float",
    "charfloat/": "float",
    "charfloat=": "char",
    "charfloat==": "bool",
    "charfloat!=": "bool",
    "charfloat<=": "bool",
    "charfloat<": "bool",
    "charfloat>": "bool",
    "charfloat>=": "bool",
    "charstring+": "str",
    "charbool+":  "int",
    "charbool-": "int",
    "charbool*": "int",
    "charbool/": "int",
    "charbool%": "int",
    "charbool=": "char",
    "charbool==": "bool",
    "charbool!=": "bool",
    "charbool<=": "bool",
    "charbool<": "bool",
    "charbool>": "bool",
    "charbool>=": "bool",
    "boolbool+": "bool",
    "boolbool-": "bool",
    "boolbool*": "bool",
    "boolbool/": "bool",
    "boolbool%": "bool",
    "boolbool=": "bool",
    "boolbool==": "bool",
    "boolbool!=": "bool",
    "boolbool<=": "bool",
    "boolbool<": "bool",
    "boolbool>": "bool",
    "boolbool>=": "bool",
    "boolbool&&": "bool",
    "boolbool||": "bool",
    "boolint+": "int",
    "boolint-": "int",
    "boolint*": "int",
    "boolint/": "int",
    "boolint%": "int",
    "boolint=": "bool",
    "boolint==": "bool",
    "boolint!=": "bool",
    "boolint<=": "bool",
    "boolint<": "bool",
    "boolint>": "bool",
    "boolint>=": "bool",
    "boolfloat-": "float",
    "boolfloat*": "float",
    "boolfloat/": "float",
    "boolfloat%": "float",
    "boolfloat=": "bool",
    "boolfloat==": "bool",
    "boolfloat!=": "bool",
    "boolfloat<=": "bool",
    "boolfloat<": "bool",
    "boolfloat>": "bool",
    "boolfloat>=": "bool",
    "boolchar+": "int",
    "boolchar-": "int",
    "boolchar*": "int",
    "boolchar/": "int",
    "boolchar%": "int",
    "boolchar=": "bool",
    "boolchar==": "bool",
    "boolchar!=": "bool",
    "boolchar<=": "bool",
    "boolchar<": "bool",
    "boolchar>": "bool",
    "boolchar>=": "bool",
    "char!": "bool",
    "int!": "bool",
    "int++": "int",
    "int--": "int",
    "float!": "bool",
    "bool!": "bool",
    "bool++": "bool",
    "bool--": "bool",
    "char++": "char",
    "char--": "char",
    "float++": "float",
    "float--": "float"
}


class deifinitionTable:
    def __init__(self, name, ofType, typeMod, parent):
        self.name = name
        self.type = ofType
        self.typeMod = typeMod
        self.parent = parent
        self.attrTable = []


class memberTable:
    def __init__(self, name, params, ofType, accessMod, stat, concCond):
        self.name = name
        self.params = params
        self.type = ofType
        self.accessMod = accessMod
        self.stat = stat
        self.concCond = concCond


class scopeTable:
    def __init__(self, name, ofType, scope):
        self.name = name
        self.type = ofType
        self.scope = scope


def lookupDT(name):
    x = next((j for j in Definition_Table if j.name == name), "")
    if (x == ""):
        return False
    # print("\tLookUp Definition Table")
    # print(vars(x))
    return x


def insertDT(name, ofType, typeMod, parent):
    if (lookupDT(name) == False):
        obj = deifinitionTable(name, ofType, typeMod, parent)
        Definition_Table.append(obj)
        # print("\tDefinition Table")
        # for t in Definition_Table:
        #     print(vars(t))
        return True
    return False


def lookupMT(name, paramList, ofName):
    x = lookupDT(ofName)
    if (x != False):
        if (paramList == "void"):
            y = next((j for j in x.attrTable if j.name == name), "")
            if (y == ""):
                return False
            # print("\tLookUp Member Table")
            # print(vars(y))
            return y
        else:
            y = next((j for j in x.attrTable if j.name ==
                     name and j.params == paramList), "")
            if (y == ""):
                return False
            # print("\tLookUp Member Table")
            # print(vars(y))
            return y
    return False


def insertMT(name, params, ofType, accessMod, stat, concCond, ofName):
    if(lookupMT(name, params, ofName) == False):
        for i in Definition_Table:
            if i.name == ofName:
                obj = memberTable(name, params, ofType,
                                     accessMod, stat, concCond)
                i.attrTable.append(obj)
                # print("\tMember Table")
                # for t in i.attrTable:
                #     print(vars(t))
                return True
    return False


def lookupST(name):
    for i in Scope_Stack:
        x = next((j for j in Scope_Table if j.scope ==
                 i and j.name == name), "")
        if (x != ""):
            # print("\tLookUp Scope Table")
            # print(vars(x))
            return x.type
    return False


def insertST(name, ofType, scope):
    if(lookupST(name) == False):
        obj = scopeTable(name, ofType, scope)
        Scope_Table.append(obj)
        # print("\tSope Table")
        # for t in Scope_Table:
        #     print(vars(t))
        return True
    return False


def Create_Scope():
    global highestScope
    highestScope += 1
    x = highestScope
    print("Created Scope:\t", x)
    Scope_Stack.insert(x)
    return Scope_Stack[0]


def Destroy_Scope():
    x = Scope_Stack.pop(0)
    print("Destroyed Scope:\t", x)
    return Scope_Stack[0]


def Bin_Type_Compatiblity(left, right, op):
    check = left + right + op
    if check in typeCompatibility.keys():
        return typeCompatibility[check]
    check = right + left + op
    if check in typeCompatibility.keys():
        return typeCompatibility[check]
    return False


def Uni_Type_Compatiblity(left, op):
    check = left + op
    if check in typeCompatibility.keys():
        return typeCompatibility[check]
    return False
