from LA import tokenize

input_file_name = "input.txt"
output_file_name = "output.txt"

with open(input_file_name, 'r') as input_file:
    source_code = input_file.read()

tokens = tokenize(source_code)

tokens.append({'Class': '@', 'Value': '@', 'Line': -1})  # You can use -1 for the line number

token_type = []
token_value = []
line_number = []

for token in tokens:
    # Check if the token is a dictionary or a list (depending on the structure of your 'tokens' list)
    
    if isinstance(token, list) and len(token) >= 3:
        # Assuming 'token' is a list where [0] is 'type', [1] is 'value', and [2] is 'line_number'
        token_type.append(token[0])
        token_value.append(token[1])
        line_number.append(token[2])


i = 0
error_line = 0
token_list=[]
syntax_Error = ""

def syntaxAnalyzer():
    global i,error_line, syntax_Error, token_list
    i = 0
    result = Start_NT()
    if (not result):
        syntax_Error += "\nTOKEN UNEXPECTED:\n\tValue:\t" + token_value[i] + "\n\tType:\t" + token_type[i] +\
                    "\n\tFile:\t\'.\\input.txt\' [@ Line number " + str(line_number[i]) + "]\n\tToken:\t" + str(
            error_line+1) + "\n\n\n"
        print(syntax_Error)
    elif (result):
        if(token_type[i]=="@"):
            print("Tree and Input Completely Parsed!")
        else:
            print("Tree Completely Parsed but Input not completely parsed!")

try:
    # START NT  -- COMPLETED
    def Start_NT():
        global i, token_type
        if(token_type[i] == "DT"):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Func" or token_type[i] == "Main"): # First of Y2
                if(Y2()):
                    return True
        elif(token_type[i] == "ID"): # First of Dict
            if(Dict()):
                i+=1
                if(token_type[i]==";"):
                    i+=1
                    if(token_type[i] == "ID"or token_type[i] == "DT" or token_type[i] == "Class" or token_type[i] =="Void" or token_type[i] == "@"): # First of Defs
                        if(Defs()):
                            i+=1
                            if(token_type[i] == "DT"):
                                i+=1
                                if(token_type[i] == "Main"):
                                    i+=1
                                    if(token_type[i] == "("):
                                        i+=1
                                        if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "string_const" or token_type[i] == "char_const" or token_type[i] ==")"):
                                            if(Arg_L()):
                                                i+=1
                                                if(token_type[i] ==")"):
                                                    i+=1
                                                    if(token_type[i] == "{"):
                                                        i+=1
                                                        if(token_type[i] == "If" or token_type[i] == "For" or token_type[i] =="BreakCon" or token_type[i] =="Return" or token_type[i] =="ID" or token_type[i] =="DT" or token_type[i] == "inc_dec" or token_type[i] =="Void" or token_type[i] == "}"):
                                                            if(MST()):
                                                                i+=1
                                                                if(token_type[i] == "}"):
                                                                    i+=1
                                                                    if(token_type[i] == "ID"or token_type[i] == "DT" or token_type[i] == "Class" or token_type[i] == "Void" or token_type[i] == "@"):
                                                                        if(Defs()):
                                                                            return True
      
        elif(token_type[i] == "Class"):
            if(Class()):
                i+=1
                if(token_type[i] == "ID"or token_type[i] == "DT" or token_type[i] == "Class" or token_type[i] == "Void" or token_type[i] == "@"):
                    if(Defs()):
                        i+=1
                        if(token_type[i] == "DT"):
                            i+=1
                            if(token_type[i] == "Main"):
                                i+=1
                                if(token_type[i] == "("):
                                    i+=1
                                    if(token_type[i] == "ID" or token_type[i] == "" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "string_const" or token_type[i] == "char_const" or token_type[i] ==")"):
                                        if(Arg_L()):
                                            i+=1
                                            if(token_type[i] == ")"):
                                                i+=1
                                                if(token_type[i] == "{"):
                                                    i+=1
                                                    if(token_type[i] == "If" or token_type[i] == "For" or token_type[i] =="BreakCon" or token_type[i] =="Return" or token_type[i] =="ID" or token_type[i] =="DT" or token_type[i] == "inc_dec" or token_type[i] =="Void" or token_type[i] == "}"):
                                                        if(MST()):
                                                            i+=1
                                                            if(token_type[i] == "}"):
                                                                i+=1
                                                                if(token_type[i] == "ID"or token_type[i] == "DT" or token_type[i] == "Class" or token_type[i] == "Void" or token_type[i] == "@"):
                                                                    if(Defs()):
                                                                        return True

        
        elif(token_type[i] == "Void"):
            i+=1
            if(token_type[i] == "Func"):
                i+=1
                if(token_type[i] == "ID"):
                    i+=1
                    if(token_type[i] == "("):
                        i+=1
                        if(token_type[i] == "DT" or token_type[i] ==")"):
                            if(PL()):
                                i+=1
                                if(token_type[i] ==")"):
                                    i+=1
                                    if(token_type[i] == "{"):
                                        i+=1
                                        if(token_type[i] == "If" or token_type[i] == "For" or token_type[i] =="BreakCon" or token_type[i] =="Return" or token_type[i] =="ID" or token_type[i] =="DT" or token_type[i] == "inc_dec" or token_type[i] =="Void" or token_type[i] == "}"):
                                            if(MST()):
                                                i+=1
                                                if(token_type[i] == "}"):
                                                    i+=1
                                                    if(token_type[i] == "ID"or token_type[i] == "DT" or token_type[i] == "Class" or token_type[i] == "Void" or token_type[i] == "@"):
                                                        if(Defs()):
                                                            i+=1
                                                            if(token_type[i] =="DT"):
                                                                i+=1
                                                                if(token_type[i] =="Main"):
                                                                    i+=1
                                                                    if(token_type[i] =="("):
                                                                        i+=1
                                                                        if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "string_const" or token_type[i] == "char_const" or token_type[i] ==")"):
                                                                            if(Arg_L()):
                                                                                i+=1
                                                                                if(token_type[i] == ")"):
                                                                                    i+=1
                                                                                    if(token_type[i] == "{"):
                                                                                        i+=1
                                                                                        if(token_type[i] == "If" or token_type[i] == "For" or token_type[i] =="BreakCon" or token_type[i] =="Return" or token_type[i] =="ID" or token_type[i] =="DT" or token_type[i] == "inc_dec" or token_type[i] =="Void" or token_type[i] == "}"):
                                                                                            if(MST()):
                                                                                                i+=1
                                                                                                if(token_type[i] == "}"):
                                                                                                    i+=1
                                                                                                    if(token_type[i] == "ID"or token_type[i] == "DT" or token_type[i] == "Class" or token_type[i] == "Void" or token_type[i] == "@"):
                                                                                                        if(Defs()):
                                                                                                            return True
            
        return False
    
    def Y2():
        global i, token_type
        if(token_type[i] == "ID" or token_type[i] == "Func"):
            if(Y1()):
                i+=1
                if(token_type[i] == "DT"):
                    i+=1
                    if(token_type[i] == "Main"):
                        i+=1
                        if(token_type[i] == "("):
                            i+=1
                            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "string_const" or token_type[i] == "char_const" or token_type[i] ==")"):
                                if(Arg_L()):
                                    i+=1
                                    if(token_type[i] == ")"):
                                        i+=1
                                        if(token_type[i] == "{"):
                                            i+=1
                                            if(token_type[i] == "If" or token_type[i] == "For" or token_type[i] =="BreakCon" or token_type[i] =="Return" or token_type[i] =="ID" or token_type[i] =="DT" or token_type[i] == "inc_dec" or token_type[i] =="Void" or token_type[i] == "}"):
                                                if(MST()):
                                                    i+=1
                                                    if(token_type[i] == "}"):
                                                        i+=1
                                                        if(token_type[i] == "ID"or token_type[i] == "DT" or token_type[i] == "Class" or token_type[i] == "Void" or token_type[i] == "@"):
                                                            if(Defs()):
                                                                return True
        
      
        elif(token_type[i] == "Main"):
            i+=1
            if(token_type[i] == "("):
                i+=1
                if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "string_const" or token_type[i] == "char_const" or token_type[i] ==")"):
                    if(Arg_L()):
                        i+=1
                        if(token_type[i] == ")"):
                            i+=1
                            if(token_type[i] == "{"):
                                i+=1
                                if(token_type[i] == "If" or token_type[i] == "For" or token_type[i] =="BreakCon" or token_type[i] =="Return" or token_type[i] =="ID" or token_type[i] =="DT" or token_type[i] == "inc_dec" or token_type[i] =="Void" or token_type[i] == "}"):
                                    if(MST()):
                                        i+=1
                                        if(token_type[i] == "}"):
                                            i+=1
                                            if(token_type[i] == "ID"or token_type[i] == "DT" or token_type[i] == "Class" or token_type[i] == "Void" or token_type[i] == "@"):
                                                if(Defs()):
                                                    return True

        return False
    
    # DEFINITIONS OUTSIDE THE MAIN -- COMPLETED
    def Defs():
        global i, token_type
        if(token_type[i] == "DT"):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Func"):
                if(Y1()):
                    return True
        
        
        elif(token_type[i] == "ID"):
            if(Dict()):
                i+=1
                if(token_type[i] == ";"):
                    i+=1
                    if(token_type[i] == "ID"or token_type[i] == "DT" or token_type[i] == "Class" or token_type[i] == "Void" or token_type[i] == "@"):
                        if(Defs()):
                            return True


       
        elif(token_type[i] == "Class"):
            if(Class()):
                i+=1
                if(token_type[i] == "ID"or token_type[i] == "DT" or token_type[i] == "Class" or token_type[i] == "Void" or token_type[i] == "@"):
                    if(Defs()):
                        return True

        
        elif(token_type[i] == "Void"):
            i+=1
            if(token_type[i] == "Func"):
                i+=1
                if(token_type[i] == "ID"):
                    i+=1
                    if(token_type[i] == "("):
                        i+=1
                        if(token_type[i] == "DT" or token_type[i] ==")"):
                            if(PL()):
                                i+=1
                                if(token_type[i] ==")"):
                                    i+=1
                                    if(token_type[i] == "{"):
                                        i+=1
                                        if(token_type[i] == "If" or token_type[i] == "For" or token_type[i] =="BreakCon" or token_type[i] =="Return" or token_type[i] =="ID" or token_type[i] =="DT" or token_type[i] == "inc_dec" or token_type[i] =="Void" or token_type[i] == "}"):
                                            if(MST()):
                                                i+=1
                                                if(token_type[i] == "}"):
                                                    i+=1
                                                    if(token_type[i] == "ID"or token_type[i] == "DT" or token_type[i] == "Class" or token_type[i] == "Void" or token_type[i] == "@"):
                                                        if(Defs()):
                                                            return True

        
        elif(token_type[i] =="DT" or token_type[i] =="@"):
            return True

        return False
    
    def Y1():
        global i, token_type
        if(token_type[i] == "ID"):
            i+=1
            if(token_type[i] == "=" or token_type[i] == "," or token_type[i] ==";"):
                if(Init()):
                    i+=1
                    if(token_type[i] == "," or token_type[i] == ";"):
                        if(List()):
                            i+=1
                            if(token_type[i] == ";"):
                                i+=1
                                if(token_type[i] == "ID"or token_type[i] == "DT" or token_type[i] == "Class" or token_type[i] == "Void" or token_type[i] == "@"):
                                    if(Defs()):
                                        return True
        
        elif(token_type[i] == "Func"):
            i+=1
            if(token_type[i] == "ID"):
                i+=1
                if(token_type[i] == "("):
                    i+=1
                    if(token_type[i] == "DT" or token_type[i] ==")"):
                        if(PL()):
                            i+=1
                            if(token_type[i] ==")"):
                                i+=1
                                if(token_type[i] == "{"):
                                    i+=1
                                    if(token_type[i] == "If" or token_type[i] == "For" or token_type[i] =="BreakCon" or token_type[i] =="Return" or token_type[i] =="ID" or token_type[i] =="DT" or token_type[i] == "inc_dec" or token_type[i] =="Void" or token_type[i] == "}"):
                                        if(MST()):
                                            i+=1
                                            if(token_type[i] == "}"):
                                                i+=1
                                                if(token_type[i] == "ID"or token_type[i] == "DT" or token_type[i] == "Class" or token_type[i] == "Void" or token_type[i] == "@"):
                                                    if(Defs()):
                                                        return True

        return False
    
    # BODY -- COMPLETE
    def Body():
        global i, token_type
        if(token_type[i] == ";"):
            return True
        
        elif(token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "BreakCon" or token_type[i] == "Return" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "inc_dec" or token_type[i] == "Void"):
            if(SST()):
                return True
        elif(token_type[i] == "{"):
            i+=1
            if(token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "BreakCon" or token_type[i] == "Return" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "inc_dec" or token_type[i] == "Void" or token_type[i] =="Elif" or token_type[i] == "Default" or token_type[i] == "}" ):
                if(MST()):
                    i+=1
                    if(token_type[i] == "}"):
                        return True

        return False
    

    # SINGLE LINE STATEMENT -- COMPLETE 
    def SST():
        global i, token_type
        if(token_type[i] == "If"):
            if(If_St()):
                return True
        
        elif( token_type[i] == "For"):
            if(For()):
                return True

        elif(token_type[i] == "BreakCon"):
            return True

        elif(token_type[i] == "Return"):
            if(Return()):
                return True

        elif(token_type[i] == "ID"):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "=" or token_type[i] == "." or token_type[i] == "[" or token_type[i] == "(" or token_type[i] == "OP_assign" or token_type[i] == "inc_dec"):
                if(SST1()):
                    i+=1
                    if(token_type[i] == ";"):
                        return True

        elif(token_type[i] =="DT"):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Func"):
                if(SST2):
                    i+=1
                    if(token_type[i] == ";"):
                        return True

        elif(token_type[i] == "inc_dec"):
            i+=1
            if(token_type[i] == "ID"):
                i+=1
                if(token_type[i] == "." or token_type[i] == "["  or token_type[i] =="(" or token_type[i] == ";"):
                    if(X()):
                        i+=1
                        if(token_type[i] == ";"):
                            return True

        elif(token_type[i] == "Void"):
            i+=1
            if(token_type[i] == "Func"):
                i+=1
                if(token_type[i] == "ID"):
                    i+=1
                    if(token_type[i] == "("):
                        i+=1
                        if(token_type[i] == "DT" or token_type[i] ==")"):
                            if(PL()):
                                i+=1
                                if(token_type[i] ==")"):
                                    i+=1
                                    if(token_type[i] == "{"):
                                        i+=1
                                        if(token_type[i] == "If" or token_type[i] == "For" or token_type[i] =="BreakCon" or token_type[i] =="Return" or token_type[i] =="ID" or token_type[i] =="DT" or token_type[i] == "inc_dec" or token_type[i] =="Void" or token_type[i] == "}"):
                                            if(MST()):
                                                i+=1
                                                if(token_type[i] == "}"):
                                                    return True
        return False
    
    def SST2():
        global i, token_type
        if(token_type[i] == "ID"):
            i+=1
            if(token_type[i] == "=" or token_type[i] == "," or token_type[i] == ";"):
                if(Init()):
                    i+=1
                    if(token_type[i] == "," or token_type[i] == ";"):
                        if(List()):
                            return True

        elif(token_type[i] == "Func"):
            i+=1
            if(token_type[i] == "ID"):
                i+=1
                if(token_type[i] == "("):
                    i+=1
                    if(token_type[i] == "DT" or token_type[i] ==")"):
                        if(PL()):
                            i+=1
                            if(token_type[i] ==")"):
                                i+=1
                                if(token_type[i] == "{"):
                                    i+=1
                                    if(token_type[i] == "If" or token_type[i] == "For" or token_type[i] =="BreakCon" or token_type[i] =="Return" or token_type[i] =="ID" or token_type[i] =="DT" or token_type[i] == "inc_dec" or token_type[i] =="Void" or token_type[i] == "}"):
                                        if(MST()):
                                            i+=1
                                            if(token_type[i] == "}"):
                                                return True

            
        return False
    
    def SST1():
        global i, token_type
        if(token_type[i] == "ID"):
            i+=1
            if(token_type[i] == "(" or token_type[i] == ";"):
                if(X6()):
                    return True

        elif(token_type[i] == "="):
            i+=1
            if(token_type[i] == "{"):
                i+=1
                if(token_type[i] == "(" or token_type[i] == "}"):
                    if(Dict1()):
                        i+=1
                        if(token_type[i] == "}"):
                            return True

        elif(token_type[i] == "."):
            i+=1
            if(token_type[i] == "ID"):
                i+=1
                if(token_type[i] == "=" or token_type[i] == "OP_assign" or token_type[i] == "inc_dec" or token_type[i] == "." or token_type[i] == "[" or token_type[i] == "(" or token_type[i] == ";"):
                    if(A1()):
                        return True  
 
        elif(token_type[i] == "["):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
                if(OE()):
                    i+=1
                    if(token_type[i] == "]"):
                        i+=1
                        if(token_type[i] == "." or token_type[i] == "(" or token_type[i] == "[" or token_type[i] == ";"):
                            if(A2()):
                                return True

        elif(token_type[i] == "("):
                i+=1
                if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "string_const" or token_type[i] == "char_const" or token_type[i] ==")"):
                    if(Arg_L()):
                        i+=1
                        if(token_type[i] == ")"):
                            i+=1
                            if(token_type[i] == "." or token_type[i] == "(" or token_type[i] == "[" or token_type[i] == ";"):
                                if(A3()):
                                    return True

        elif(token_type[i] == "=" or token_type[i] == "OP_assign"):
            if(AO()):
                i+=1
                if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
                    if(OE()):
                        return True

        elif(token_type[i] == "inc_dec"):
            return True
        return False
    
    def A1():
        global i, token_type
        if(token_type[i] == "=" or token_type[i] == "OP_assign" or token_type[i] == "inc_dec" ):
            if(A4()):
                return True

        elif(token_type[i] == "."):
            i+=1
            if(token_type[i] == "ID"):
                i+=1
                if(token_type[i] == "=" or token_type[i] == "OP_assign" or token_type[i] == "inc_dec" or token_type[i] == "." or token_type[i] == "[" or token_type[i] == "("  or token_type[i] == ";"): 
                    if(A1()):
                        return True  

        elif(token_type[i] == "["):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
                if(OE()):
                    i+=1
                    if(token_type[i] == "]"):
                        i+=1
                        if(token_type[i] == "." or token_type[i] == "(" or token_type[i] == "[" or token_type[i] == ";"):
                            if(A2()):
                                return True

        elif(token_type[i] == "("):
                i+=1
                if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "string_const" or token_type[i] == "char_const" or token_type[i] ==")"):
                    if(Arg_L()):
                        i+=1
                        if(token_type[i] == ")"):
                            i+=1
                            if(token_type[i] == "." or token_type[i] == "(" or token_type[i] == "[" or token_type[i] == ";"):
                                if(A3()):
                                    return True

        elif(token_type[i] == ";"):
            return True

        
        return False
    
    def A2():
        global i, token_type
        if(token_type[i] == "." or token_type[i] == "=" or token_type[i] == "OP_assign" or token_type[i] == "inc_dec"):
            if(Xo()):
                i+=1
                if(token_type[i] == "=" or token_type[i] == "OP_assign" or token_type[i] == "inc_dec" ):
                    if(A4()):
                        return True
            

        elif(token_type[i] == "." or token_type[i] == "(" or token_type[i] == "[" or token_type[i] == ";" ):
            if(X4()):
                return True
        return False
    
    def A3():
        global i, token_type
        if(token_type[i] == "." or token_type[i] == "["):
            if(X1()):
                i+=1
                if(token_type[i] == "=" or token_type[i] == "OP_assign" or token_type[i] == "inc_dec" ):
                    if(A4()):
                        return True

        elif(token_type[i] == "." or token_type[i] == "(" or token_type[i] == "[" or token_type[i] == ";"):
            if(X4()):
                return True
        return False
    
    def A4():
        global i, token_type
        if(token_type[i] == "=" or token_type[i] == "OP_assign"):
            if(AO()):
                i+=1
                if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
                    if(OE()):
                        return True

        elif(token_type[i] == "inc_dec" ):
            return True
        return False
    
    # MULTI-LINE STATEMENT -- INCOMPLETE
    def MST():
        global i, token_type

        return False
    
    # ARGUMENT LIST -- COMPLETED
    def Arg_L():
        global i, token_type
        if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
            if(OE()):
                i+=1
                if(token_type[i] == "," or token_type[i] == ")"):
                    if(Arg1()):
                        return True
                    

        elif(token_type[i] == ")"):
            return True

        return False
    
    def Arg1():
        global i, token_type
        if(token_type[i] == ","):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const"):
                if(OE()):
                    i+=1
                    if(token_type[i] == "," or token_type[i] == ")"):
                        if(Arg1()):
                            return True

        elif(token_type[i] == ")"):
            return True

        return False   
    
    # RETURN STATEMENT -- COMPLETED
    def Return():
        global i, token_type
        if(token_type[i] == "Return"):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" or token_type[i] == ";"):
                if(R1()):
                    i+=1
                    if(token_type[i] == ";"):
                        return True
        return False
    
    def R1():
        global i, token_type
        if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const"):
                if(OE()):
                    return True

        elif(token_type[i] == ";"):
            return True
        return False
    
    # DECLARATION, LIST AND INITIALIZATION -- COMPLETED
    def Dec():
        global i, token_type
        if(token_type[i] == "DT"):
            i+=1
            if(token_type[i] == "ID"):
                i+=1
                if(token_type[i] == "=" or token_type[i] == "," or token_type[i] == ";"):
                    if(Init()):
                        i+=1
                        if(token_type[i] == "," or token_type[i] == ";"):
                            if(List()):
                                return True

        return False
    
    def Init():
        global i, token_type
        if(token_type[i] == "="):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" or token_type[i] == "[" ):
                if(Init2()):
                    return True

        elif(token_type[i] == "," or token_type[i] == ";" ):
            return True

        return False
    
    def Init2():
        global i, token_type
        if(token_type[i] == "ID"):
            i+=1
            if(token_type[i] == "=" or token_type[i] == "," or token_type[i] == ";"):
                if(Init()):
                    return True

        elif(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const"):
            if(OE()):
                return True

        elif(token_type[i] == "["):
            if(List2()):
                return True

        return False
    
    def List():
        global i, token_type
        if(token_type[i] == "," ):
            i+=1
            if(token_type[i] == "ID"):
                i+=1
                if(token_type[i] == "=" or token_type[i] == "," or token_type[i] == ";"):
                    if(Init()):
                        i+=1
                        if(token_type[i] == "," or token_type[i] == ";"):
                            if(List()):
                                return True


        elif(token_type[i] == ";"):
            return True
        return False
    
    def List1():
        global i, token_type
        if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const"):
            if(OE()):
                i+=1
                if(token_type[i] == ","  or token_type[i] == "]"):
                    if(List1_()):
                        return True

        elif(token_type[i] == "]"):
            return True

        elif(token_type[i] == "["):
            if(List2()):
                i+=1
                if(token_type[i] == ","  or token_type[i] == "]"):
                    if(List1_()):
                        return True

        return False
    
    def List1_():
        global i, token_type
        if(token_type[i] == "," ):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" or token_type[i] == "["):
                if(List3()):
                    return True
        elif(token_type[i] == "]"):
            return True
        return False
    
    def List2():
        if(token_type[i] == "["):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" or token_type[i] == "[" or token_type[i] == "]"):
                if(List1()):
                    i+=1
                    if(token_type[i] == "]"):
                        return True
        return False
    
    def List3():
        global i, token_type
        if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
            if(OE()):
                i+=1
                if(token_type[i] == "," or token_type[i] == "]"):
                    if(List1_()):
                        return True

        elif(token_type[i] == "["):
            if(List2()):
                i+=1
                if(token_type[i] == ","  or token_type[i] == "]"):
                    if(List1_()):
                        return True
        return False
    
    # DICTIONARY -- COMPLETED
    def Dict():
        global i, token_type
        if(token_type[i] == "ID"):
            i+=1
            if(token_type[i] == "="):
                i+=1
                if(token_type[i] == "{"):
                    i+=1
                    if(token_type[i] == "(" or token_type[i] == "}"):
                        if(Dict1()):
                            i+=1
                            if(token_type[i] == "}"):
                                return True

        return False
    
    def Dict1():
        global i, token_type
        if(token_type[i] == "("):
            if(Pair()):
                i+=1
                if(token_type[i] == "," or token_type[i] == "}"):
                    if(Dict1_()):
                        return True

        elif(token_type[i] == "}"):
            return True
        return False
    
    def Dict1_():
        global i, token_type
        if(token_type[i] == "," ):
            i+=1
            if(token_type[i] == "("):
                if(Pair()):
                    i+=1
                    if(token_type[i] == "," or token_type[i] == "}"):
                        if(Dict1_()):
                            return True

        elif(token_type[i] == "}"):
            return True
        return False
    
    def Pair():
        global i, token_type
        if(token_type[i] == "("):
            i+=1
            if(token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const"):
                if(Const()):
                    i+=1
                    if(token_type[i] == ","):
                        i+=1
                        if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" or token_type[i] == "[" or token_type[i] == ")" or token_type[i] == "{"):
                            if(Value()):
                                i+=1
                                if(token_type[i] == ")"):
                                    return True
        return False
    
    def Value():
        global i, token_type
        if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
            if(OE()):
                return True

        elif(token_type[i] == "["):
            if(List2()):
                return True

        elif(token_type[i] == "{" ):
            i+=1
            if(token_type[i] == "(" or token_type[i] == "}"):
                if(Dict1()):
                    i+=1
                    if(token_type[i] == "}"):
                        return True
            
            

        elif(token_type[i] == "ID" ):
            if(Func_Call()):
                return True
        return False

    # CONSTANT 
    def Const():
        global i, token_type
        if(token_type[i] == "int_const"):
            i+=1
            return True
            
        elif(token_type[i] == "float_const"):
            i+=1
            return True

        elif(token_type[i] == "bool_const"):
            i+=1
            return True

        elif(token_type[i] == "string_const"):
            i+=1
            return True

        elif(token_type[i] == "char_const"):
            i+=1
            return True
        return False
    
    # FUNCTION -- COMPLETED
    def Func():
        global i, token_type
        if(token_type[i]=="Void" or token_type[i]=="DT"):
            if(Ret_Type()):
                i+=1
                if(token_type[i] == "Func"):
                    i+=1
                    if(token_type[i] == "ID"):
                        i+=1
                        if(token_type[i] == "("):
                            i+=1
                            if(token_type[i] == "DT" or token_type[i] ==")"):
                                if(PL()):
                                    i+=1
                                    if(token_type[i] ==")"):
                                        i+=1
                                        if(token_type[i] == "{"):
                                            i+=1
                                            if(token_type[i] == "If" or token_type[i] == "For" or token_type[i] =="BreakCon" or token_type[i] =="Return" or token_type[i] =="ID" or token_type[i] =="DT" or token_type[i] == "inc_dec" or token_type[i] =="Void" or token_type[i] == "}"):
                                                if(MST()):
                                                    i+=1
                                                    if(token_type[i] == "}"):
                                                        return True

        return False
    
    # RETURN TYPE -- COMPLETED
    def Ret_Type():
        global i, token_type
        if(token_type[i]=="Void"):
            i+=1
            return True
            
        elif(token_type[i]=="DT"):
            i+=1
            return True
        return False
    
    # PARAMETER LIST -- COMPLETED
    def PL():
        global i, token_type
        if(token_type[i]=="DT"): 
            if(P1()):
                i+=1
                if(token_type[i]== "," or token_type[i]== ")" ):
                    if(PL_()):
                        return True
        
        elif(token_type[i]== ")"):
            return True
        return False
    
    def PL_():
        global i, token_type
        if(token_type[i]== ","):
            i+=1
            if(token_type[i]=="DT"):
                if(P1()):
                    i+=1
                    if(token_type[i]== "," or token_type[i]== ")" ):
                        if(PL_()):
                            return True

        elif(token_type[i]== ")"):
            return True
        return False
    
    def P1():
        global i, token_type
        if(token_type[i]=="DT"):
            i+=1
            if(token_type[i]=="ID"):
                i+=1
                if(token_type[i]=="=" or token_type[i]== "," or token_type[i]== ")" ):
                    if(P2()):
                        return True
        return False
    
    def P2():
        global i, token_type
        if(token_type[i]=="="):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
                if(OE()):
                    return True
        
        elif(token_type[i]== "," or token_type[i]== ")"):
            return True
        return False
    
    # IF STATEMENT -- COMPLETED
    def If_St():
        global i, token_type
        if(token_type[i]== "If"):
            i+=1
            if(token_type[i]== "("):
                i+=1
                if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
                    if(OE()):
                        i+=1
                        if("token_type"[i]== ")"):
                            i+=1
                            if(token_type[i]== ";" or token_type[i]== "If" or token_type[i]== "For" or token_type[i]== "BreakCon" or token_type[i]== "Return" or token_type[i]== "ID" or token_type[i]== "DT" or token_type[i]== "inc_dec" or token_type[i]== "Void" or token_type[i]== "{"): 
                                if(Body()):
                                    i+=1
                                    if(token_type[i]== "Elif" or token_type[i]== "Default" or token_type[i]== "If" or token_type[i]== "For" or token_type[i]== "BreakCon" or token_type[i]== "Return" or token_type[i]== "ID" or token_type[i]== "DT" or token_type[i]== "inc_dec" or token_type[i]== "Void" or token_type[i]=="Self" or token_type[i]=="}" ):
                                        if(Elif()):
                                            i+=1
                                            if(token_type[i]== "Default" or token_type[i]== "If" or token_type[i]== "For" or token_type[i]== "BreakCon" or token_type[i]== "Return" or token_type[i]== "ID" or token_type[i]== "DT" or token_type[i]== "inc_dec" or token_type[i]== "Void" or token_type[i]=="Self" or token_type[i]== "}"):
                                                if(Default()):
                                                    return True
        return False
    
    def Elif():
        global i, token_type
        if(token_type[i]== "Elif"):
            i+=1
            if(token_type[i]== "("):
                i+=1
                if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
                    if(OE()):
                        i+=1
                        if("token_type"[i]== ")"):
                            i+=1
                            if(token_type[i]== ";" or token_type[i]== "If" or token_type[i]== "For" or token_type[i]== "BreakCon" or token_type[i]== "Return" or token_type[i]== "ID" or token_type[i]== "DT" or token_type[i]== "inc_dec" or token_type[i]== "Void" or token_type[i]== "{"): 
                                if(Body()):
                                    i+=1
                                    if(token_type[i]== "Elif" or token_type[i]== "Default" or token_type[i]== "If" or token_type[i]== "For" or token_type[i]== "BreakCon" or token_type[i]== "Return" or token_type[i]== "ID" or token_type[i]== "DT" or token_type[i]== "inc_dec" or token_type[i]== "Void" or token_type[i]=="Self" or token_type[i]== "}"):
                                        if(Elif()):
                                            return True


        elif(token_type[i]== "Default" or token_type[i]== "If" or token_type[i]== "For" or token_type[i]== "BreakCon" or token_type[i]== "Return" or token_type[i]== "ID" or token_type[i]== "DT" or token_type[i]== "inc_dec" or token_type[i]== "Void" or token_type[i]=="Self" or token_type[i] == "}"): 
            return True
        return False
    
    def Default():
        global i, token_type
        if(token_type[i]== "Default"):
            i+=1
            if(token_type[i]== ";" or token_type[i]== "If" or token_type[i]== "For" or token_type[i]== "BreakCon" or token_type[i]== "Return" or token_type[i]== "ID" or token_type[i]== "DT" or token_type[i]== "inc_dec" or token_type[i]== "Void" or token_type[i]== "{"): 
                if(Body()):
                    return True

        elif(token_type[i]== "If" or token_type[i]== "For" or token_type[i]== "BreakCon" or token_type[i]== "Return" or token_type[i]== "ID" or token_type[i]== "DT" or token_type[i]== "inc_dec" or token_type[i]== "Void" or token_type[i]=="Self" or token_type[i]== "}" ):
            return True
        return False
    
    # ASSIGNMENT STATEMENT -- COMPLETED
    def Assign_St():
        global i, token_type
        if(token_type[i]== "ID"):
            i+=1
            if(token_type[i]== "." or token_type[i]== "[" or token_type[i]== "(" or token_type[i]== "=" or token_type[i]== "OP_assign" ):
                if(X()):
                    i+=1
                    if(token_type[i]== "=" or token_type[i]== "OP_assign"):
                        if(AO()):
                            i+=1
                            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
                                if(OE()):
                                    return True

        return False
    # inc_dec, =, Op_assign, ,, ;, ) , ], OR_op, AND, RO, PM, MDM, P --> fo(X)
    def X():
        global i, token_type
        if(token_type[i] == "inc_dec" or token_type[i] == "=" or token_type[i] == "OP_assign" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")" or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] == "PM" or token_type[i] == "MDM" or token_type[i] == "P"):
            return True
        
        elif(token_type[i] == "."):
            i+=1
            if(token_type[i] == "ID"):
                i+=1
                if(token_type[i]== "." or token_type[i]== "[" or token_type[i]== "(" or token_type[i] == "inc_dec" or token_type[i] == "=" or token_type[i] == "OP_assign" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")" or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] == "PM" or token_type[i] == "MDM" or token_type[i] == "P"):
                    if(X()):
                        return True
                    
        elif(token_type[i]== "["):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
                if(OE()):
                    i+=1
                    if(token_type[i] == "]"):
                        i+=1
                        if(token_type[i]== "." or token_type[i] == "inc_dec" or token_type[i] == "=" or token_type[i] == "OP_assign" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")" or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] == "PM" or token_type[i] == "MDM" or token_type[i] == "P"):
                            if(Xo()):
                                return True

        elif(token_type[i] == "("):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "string_const" or token_type[i] == "char_const" or token_type[i] ==")"):
                if(Arg_L()):
                    i+=1
                    if(token_type[i] == ")"):
                        i+=1
                        if(token_type[i]== "." or token_type[i] == "["): 
                            if(X1()):
                                return True
        return False
    # inc_dec, =, Op_assign, ,, ;, ) , ], OR_op, AND, RO, PM, MDM, P --> Fo(Xo)
    def Xo():
        global i, token_type
        if(token_type[i] == "inc_dec" or token_type[i] == "=" or token_type[i] == "OP_assign" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")" or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] == "PM" or token_type[i] == "MDM" or token_type[i] == "P"):
            return True

        elif(token_type[i] == "."):
            i+=1
            if(token_type[i] == "ID"):
                i+=1
                if(token_type[i]== "." or token_type[i]== "[" or token_type[i]== "(" or token_type[i] == "inc_dec" or token_type[i] == "=" or token_type[i] == "OP_assign" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")" or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] == "PM" or token_type[i] == "MDM" or token_type[i] == "P"):
                    if(X()):
                        return True
        return False
    
    def X1():
        global i, token_type
        if(token_type[i] == "."):
            i+=1
            if(token_type[i] == "ID"):
                i+=1
                if(token_type[i]== "." or token_type[i]== "[" or token_type[i]== "(" or token_type[i] == "inc_dec" or token_type[i] == "=" or token_type[i] == "OP_assign" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")" or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] == "PM" or token_type[i] == "MDM" or token_type[i] == "P"):
                    if(X()):
                        return True
        elif(token_type[i]== "["):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
                if(OE()):
                    i+=1
                    if(token_type[i] == "]"):
                        i+=1
                        if(token_type[i]== "." or token_type[i]== "[" or token_type[i]== "(" or token_type[i] == "inc_dec" or token_type[i] == "=" or token_type[i] == "OP_assign" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")" or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] == "PM" or token_type[i] == "MDM" or token_type[i] == "P"):
                            if(X()):
                                return True
        return False
    
    def AO():
        global i, token_type
        if(token_type[i] == "="):
            return True
        elif(token_type[i] == "OP_assign"):
            return True
        return False
     
    # INCREMENT AND DECREMENT STATEMENT -- COMPLETED
    def Inc_Dec_St():
        global i, token_type
        if(token_type[i] == "ID"):
            i+=1
            if(token_type[i]== "." or token_type[i]== "[" or token_type[i]== "(" or token_type[i]== "inc_dec"):
                if(X()):
                    i+=1
                    if(token_type[i]== "inc_dec"):
                        return True

        elif(token_type[i]== "inc_dec"):
            i+=1
            if(token_type[i] == "ID"):
                i+=1
                if(token_type[i]== "." or token_type[i]== "[" or token_type[i]== "(" or token_type[i]== ";" ):
                    if(X()):
                        return True

        return False
    
    # FUNCTION CALL AND OBJECT ACCESS -- COMPLETED
    def Func_Call():
        global i, token_type
        if(token_type[i]== "ID"):
            i+=1
            if(token_type[i]== "." or token_type[i]== "[" or token_type[i]== "("):
                if(X3()):
                    i+=1
                    if(token_type[i]== "." or token_type[i]== "[" or token_type[i]== "(" or token_type[i]==  ")" ):
                        if(X4()):
                            return True
        return False
    
    def X3():
        global i, token_type
        if(token_type[i]== "."):
            i+=1
            if(token_type[i]== "ID"):
                return True

        elif(token_type[i]== "["):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
                if(OE()):
                    i+=1
                    if(token_type[i] == "]"):
                        return True

        elif(token_type[i] == "("):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "string_const" or token_type[i] == "char_const" or token_type[i] ==")"):
                if(Arg_L()):
                    i+=1
                    if(token_type[i] == ")"):
                        return True
        return False
    
    def X4():
        global i, token_type
        if(token_type[i]== "."):
            i+=1
            if(token_type[i]== "ID"):
                i+=1
                # {,, ;, ) , ], OR_op, AND, RO, PM, MDM, P -- Fo(X4)
                if(token_type[i]== "." or token_type[i]== "[" or token_type[i]== "(" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")" or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] == "PM" or token_type[i] == "MDM" or token_type[i] == "P"):
                    if(X4()):
                        return True

        elif(token_type[i]== "["):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
                if(OE()):
                    i+=1
                    if(token_type[i] == "]"):
                        i+=1
                        if(token_type[i]== "." or token_type[i]== "[" or token_type[i]== "(" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")" or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] == "PM" or token_type[i] == "MDM" or token_type[i] == "P"):
                            if(X4()):
                                return True


        elif(token_type[i] == "("):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "string_const" or token_type[i] == "char_const" or token_type[i] ==")"):
                if(Arg_L()):
                    i+=1
                    if(token_type[i] == ")"):
                        i+=1
                        if(token_type[i]== "." or token_type[i]== "[" or token_type[i]== "(" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")" or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] == "PM" or token_type[i] == "MDM" or token_type[i] == "P"):
                            if(X4()):
                                return True

        elif(token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")" or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] == "PM" or token_type[i] == "MDM" or token_type[i] == "P"):
            return True
        
        return False
    
    # EXPRESSION -- COMPLETED
    def OE():
        global i, token_type
        if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
            if(AE()):
                i+=1 
                # ,, ;, ) , ] -- fo(OE)
                if(token_type[i] == "OR_op" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")"  or token_type[i] == "]" ):
                    if(OE_()):
                        return True
        return False
    
    def OE_():
        global i, token_type
        if(token_type[i] == "OR_op"):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
                if(AE()):
                    i+=1
                    if(token_type[i] == "OR_op" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")"  or token_type[i] == "]" ):
                        if(OE_()):
                            return True
        elif(token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")"  or token_type[i] == "]" ):
            return True

        return False
    
    def AE():
        global i, token_type
        if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
            if(RE()):
                i+=1
                if(token_type[i] == "AND" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")"  or token_type[i] == "]" or token_type[i] == "OR_op"):
                    if(AE_()):
                        return True
        return False
    
    def AE_():
        global i, token_type
        if(token_type[i] == "AND"):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
                if(RE()):
                    i+=1
                    if(token_type[i] == "AND" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")"  or token_type[i] == "]" or token_type[i] == "OR_op"):
                        if(AE_()):
                            return True
        elif(token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")"  or token_type[i] == "]" or token_type[i] == "OR_op" ):
            return True
        return False
    
    def RE():
        global i, token_type
        if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
            if(E()):
                i+=1
                if(token_type[i] == "RO" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")"  or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND"):
                    if(RE_()):
                        return True
        return False
    
    def RE_():
        global i, token_type
        if(token_type[i] == "RO"):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
                if(E()):
                    i+=1
                    if(token_type[i] == "RO" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")"  or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND"):
                        if(RE_()):
                            return True
        elif(token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")"  or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND"):
            return True
        return False
    
    def E():
        global i, token_type
        if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
            if(T()):
                i+=1
                if(token_type[i] == "PM" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")"  or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO"):
                    if(E_()):
                        return True
        return False
    
    def E_():
        global i, token_type
        if(token_type[i] == "PM"):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
                if(T()):
                    i+=1
                    if(token_type[i] == "PM" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")"  or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO"):
                        if(E_()):
                            return True
        elif(token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")"  or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO"):
            return True
        return False
    
    def T():
        global i, token_type
        if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
            if(PE()):
                i+=1
                if(token_type[i] == "MDM" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")"  or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] =="PM" ):
                    if(T_()):
                        return True
        return False
    
    def T_():
        global i, token_type
        if(token_type[i] == "MDM"):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
                if(PE()):
                    i+=1
                    if(token_type[i] == "MDM" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")"  or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] =="PM"  ):
                        if(T_()):
                            return True
        elif(token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")"  or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] =="PM" ):
            return True
        return False
    
    def PE():
        global i, token_type
        if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
            if(F()):
                i+=1
                if(token_type[i] == "P" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")"  or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] =="PM"  or token_type[i] == "MDM"):
                    if(PE_()):
                        return True
        return False
    
    def PE_():
        global i, token_type
        if(token_type[i] == "P"):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
                if(F()):
                    i+=1
                    if(token_type[i] == "P" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")"  or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] =="PM" or token_type[i] == "MDM" ):
                        if(PE_()):
                            return True
        elif(token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")"  or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] =="PM" or token_type[i] == "MDM"):
            return True
        return False
    
    # OPERAND -- COMPLETED
    def F():
        global i, token_type
        if(token_type[i] == "ID"):
            i+=1
            # ,, ;, ) , ], OR_op, AND, RO, PM, MDM, P  -- fo(F)
            if(token_type[i] == "." or token_type[i] == "[" or token_type[i] == "(" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")" or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] =="PM" or token_type[i] == "MDM" or token_type[i] == "P"): 
                if(X5()): 
                    return True
        
        elif(token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
            if(Const()):
                return True

        elif(token_type[i]== "("):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
                if(OE()):
                    i+=1
                    if(token_type[i] == ")"):
                        return True

        elif( token_type[i] == "Not"):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const"):
                if(F()):
                    return True

        elif(token_type[i]== "inc_dec"):
            i+=1
            if(token_type[i] == "ID"):
                i+=1
                if(token_type[i]== "." or token_type[i]== "[" or token_type[i]== "(" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")" or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] =="PM" or token_type[i] == "MDM" or token_type[i] == "P"):
                    if(X()):
                        return True
        return False
    
    def X5():
        global i, token_type
        if(token_type[i]== "." or token_type[i]== "[" or token_type[i]== "(" or token_type[i] == "," or token_type[i] == ";" or token_type[i] == ")" or token_type[i] == "]" or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] =="PM" or token_type[i] == "MDM" or token_type[i] == "P"):
            if(X4()):
                return True

        if(token_type[i]== "." or token_type[i]== "[" or token_type[i]== "(" or token_type[i]== "inc_dec"):
                if(X()):
                    i+=1
                    if(token_type[i]== "inc_dec"):
                        return True
        return False
    
    # OBJECT DECLARATION -- COMPLETED
    def Obj():
        global i, token_type
        if(token_type[i] == "ID"):
            i+=1
            if(token_type[i] == "ID"):
                i+=1
                if(token_type[i]== "(" or token_type[i] == ";"):
                    if(X6()):
                        return True
                
        return False
    
    def X6():
        global i, token_type
        if(token_type[i] == ";"):
            return True

        elif(token_type[i] == "("):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "string_const" or token_type[i] == "char_const" or token_type[i] ==")"):
                if(Arg_L()):
                    i+=1
                    if(token_type[i] == ")"):
                        return True
        return False
    
    # FOR STATEMENT -- COMPLETED
    def For():
        global i, token_type
        if(token_type[i] == "For"):
            i+=1
            if(token_type[i] == "("):
                i+=1
                if(token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == ";" ):
                    if(F1()):
                        i+=1
                        if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "string_const" or token_type[i] == "char_const" or token_type[i] == ";"):
                            if(F2()):
                                i+=1
                                if(token_type[i] == ";" ):
                                    i+=1
                                    if(token_type[i] == "ID" or token_type[i] == "inc_dec" or token_type[i] == ")"):
                                        if(F3()):
                                            i+=1
                                            if(token_type[i] == ")"):
                                                i+=1
                                                if(token_type[i]== ";" or token_type[i]== "If" or token_type[i]== "For" or token_type[i]== "BreakCon" or token_type[i]== "Return" or token_type[i]== "ID" or token_type[i]== "DT" or token_type[i]== "inc_dec" or token_type[i]== "Void" or token_type[i]== "{"):
                                                    if(Body()):
                                                        return True
        return False
    
    def F1():
        global i, token_type
        if(token_type[i] == "DT"):
            if(Dec()):
                i+=1
                if(token_type[i]== ";"):
                    return True

        elif(token_type[i] == "ID"):
            if(Assign_St()):
                i+=1
                if(token_type[i]== ";"):
                    return True

        elif(token_type[i]== ";"):
                    return True
        return False
    
    def F2():
        global i, token_type
        if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
            if(OE()):
                return True

        elif(token_type[i]== ";"):
            return True
        return False
    
    def F3():
        global i, token_type
        if(token_type[i] == "ID"):
            i+=1
            if(token_type[i]== "." or token_type[i]== "[" or token_type[i]== "(" or token_type[i]== "=" or token_type[i]== "inc_dec" or token_type[i]=="OP_assign"):
                if(X()):
                    i+=1
                    if( token_type[i]== "=" or token_type[i]== "inc_dec" or token_type[i]=="OP_assign"):
                        if(F4()):
                            return True

        elif(token_type[i]== "inc_dec"):
            i+=1
            if(token_type[i] == "ID"):
                i+=1
                if(token_type[i]== "." or token_type[i]== "[" or token_type[i]== "(" or token_type[i] == ")"):
                    if(X()):
                        return True

        elif(token_type[i] == ")"):
            return True
        return False
    
    def F4():
        global i, token_type
        if(token_type[i]== "inc_dec"):
            return True

        elif(token_type[i]== "=" or token_type[i]== "OP_assign"):
            if(AO()):
                i+=1
                if(token_type[i] == "ID" or token_type[i] == "Not" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "bool_const" or token_type[i] == "str_const" or token_type[i] == "char_const" ):
                    if(OE()):
                        return True
        return False
    
    # CLASS -- COMPLETED
    def Class():
        global i, token_type
        if(token_type[i] == "Class"):
            i+=1
            if(token_type[i] == "ID"):
                i+=1
                if(token_type[i] == "AM" or token_type[i] == "ID"or token_type[i] == "=>" ):
                    if(Inherit()):
                        i+=1
                        if(token_type[i] =="=>"):
                            i+=1
                            if(token_type[i] =="{"):
                                i+=1
                                if(token_type[i] == "AM" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] =="Void" or token_type[i] =="Virtual" or token_type[i] =="Static" or token_type[i] == "-:" or token_type[i] =="}"):
                                    if(Class_Body()):
                                        i+=1
                                        if(token_type[i] =="}"):
                                            i+=1
                                            if(token_type[i] ==";"):
                                                return True
        return False
    
    def Inherit():
        global i, token_type
        if(token_type[i] =="AM"):
            i+=1
            if(token_type[i] =="ID"):
                i+=1
                if(token_type[i] =="," or token_type[i] == "=>"):
                    if(Multi_Inherit()):
                        return True
        elif(token_type[i] =="ID"):
                i+=1
                if(token_type[i] =="," or token_type[i] == "=>"):
                    if(Multi_Inherit()):
                        return True

        elif(token_type[i] =="=>"):
            return True

        return False
    
    def Multi_Inherit():
        global i, token_type
        if(token_type[i] ==","):
            i+=1
            if(token_type[i] =="AM" or token_type[i] =="ID"):
                if(AM1()):
                    i+=1
                    if(token_type[i] =="ID"):
                        i+=1
                        if(token_type[i] =="," or token_type[i] == "=>"):
                            if(Multi_Inherit()):
                                return True

        elif(token_type[i] == "=>"):
            return True
        return False
    
    def Class_Body():
        global i, token_type
        if(token_type[i] =="AM"):
            i+=1
            if(token_type[i] == ":"):
                i+=1
                if(token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] =="Void" or token_type[i] =="Virtual" or token_type[i] =="Static" or token_type[i] == "-:"):
                    if(C1()):
                        i+=1
                        if(token_type[i] == "AM" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] =="Void" or token_type[i] =="Virtual" or token_type[i] =="Static" or token_type[i] == "-:" or token_type[i] =="}"):
                            if(Class_Body()):
                                return True

        elif(token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] =="Void" or token_type[i] =="Virtual" or token_type[i] =="Static" or token_type[i] == "-:"):
            if(C1()):
                i+=1
                if(token_type[i] == "AM" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] =="Void" or token_type[i] =="Virtual" or token_type[i] =="Static" or token_type[i] == "-:" or token_type[i] =="}"):
                    if(Class_Body()):
                        return True
             
        elif(token_type[i] =="}"):
            return True
        return False
    
    def C1():
        global i, token_type
        if(token_type[i] == "DT"):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "Func"):
                if(Z2()):
                    return True
                
        elif(token_type[i] == "ID"):
            i+=1
            if(token_type[i] == "ID" or token_type[i] == "("):
                if(Z3()):
                    return True
            
        elif(token_type[i] =="Void"):
            i+=1
            if(token_type[i] == "Func"):
                i+=1
                if(token_type[i] =="ID"):
                    i+=1
                    if(token_type[i] == "("):
                        i+=1
                        if(token_type[i] == "DT" or token_type[i] == ")"):
                            if(PL()):
                                i+=1
                                if(token_type[i] == ")"):
                                    i+=1
                                    if(token_type[i] =="{" or token_type[i] =="Override"):
                                        if(Z1()):
                                            i+=1
                                            if(token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] =="Void" or token_type[i] =="Virtual" or token_type[i] =="Static" or token_type[i] == "-:"):
                                                if(C1()):
                                                    return True


            
        elif(token_type[i] =="Virtual"):
            if(Virtual_Func()):
                i+=1
                if(token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] =="Void" or token_type[i] =="Virtual" or token_type[i] =="Static" or token_type[i] == "-:"):
                    if(C1()):
                        return True
            
        elif(token_type[i] =="Static"):
            if(Static_Func()):
                i+=1
                if(token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] =="Void" or token_type[i] =="Virtual" or token_type[i] =="Static" or token_type[i] == "-:"):
                    if(C1()):
                        return True
        elif(token_type[i] == "-:"):
            if(Destructor()):
                i+=1
                if(token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] =="Void" or token_type[i] =="Virtual" or token_type[i] =="Static" or token_type[i] == "-:"):
                    if(C1()):
                        return True
            
        return False
    
    def Z2():
        global i, token_type
        if(token_type[i] == "ID"):
            i+=1
            if(token_type[i] == "=" or token_type[i] == "," or token_type[i] == ";"):
                if(Init()):
                    i+=1
                    if(token_type[i] == "," or token_type[i] == ";"):
                        if(List()):
                            i+=1
                            if(token_type[i] == ";"):
                                i+=1
                                if(token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] =="Void" or token_type[i] =="Virtual" or token_type[i] =="Static" or token_type[i] == "-:"):
                                    if(C1()):
                                        return True

        elif(token_type[i] == "Func"):
                i+=1
                if(token_type[i] =="ID"):
                    i+=1
                    if(token_type[i] == "("):
                        i+=1
                        if(token_type[i] == "DT" or token_type[i] == ")"):
                            if(PL()):
                                i+=1
                                if(token_type[i] == ")"):
                                    i+=1
                                    if(token_type[i] =="}" or token_type[i] =="Override"):
                                        if(Z1()):
                                            i+=1
                                            if(token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] =="Void" or token_type[i] =="Virtual" or token_type[i] =="Static" or token_type[i] == "-:"):
                                                if(C1()):
                                                    return True

        return False
    
    def Z3():
        global i, token_type
        if(token_type[i] == "ID"):
            i+=1
            if(token_type[i] ==";"):
                i+=1
                if(token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] =="Void" or token_type[i] =="Virtual" or token_type[i] =="Static" or token_type[i] == "-:"):
                    if(C1()):
                        return True
                    
        elif(token_type[i] == "("):
            i+=1
            if(token_type[i] == "DT" or token_type[i] == ")"):
                if(Param_List()):
                    i+=1
                    if(token_type[i] == ")"):
                        i+=1
                        if(token_type[i] =="{"):
                            i+=1
                            if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}"):
                                if(Class_MST()):
                                    i+=1
                                    if(token_type[i] == "}"):
                                        i+=1
                                        if(token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] =="Void" or token_type[i] =="Virtual" or token_type[i] =="Static" or token_type[i] == "-:"):
                                            if(C1()):
                                                return True

        return False
    
    def Attribute():
        global i, token_type
        if(token_type[i] == "DT"):
            if(Dec()):
                i+=1
                if(token_type[i] == ";"):
                    return True

        elif(token_type[i] == "ID"):
            if(Obj_Dec()):
                i+=1
                if(token_type[i] == ";"):
                    return True

        return False
    
    def Obj_Dec():
        global i, token_type
        if(token_type[i] == "ID"):
            i+=1
            if(token_type[i] == "ID"):
                return True
        return False
    
    def Constructor():
        global i, token_type
        if(token_type[i] == "ID"):
            i+=1
            if(token_type[i] == "("):
                i+=1
                if(token_type[i] == "DT" or token_type[i] == ")"):
                    if(Param_List()):
                        i+=1
                        if(token_type[i] == ")"):
                            i+=1
                            if(token_type[i] =="{"):
                                i+=1
                                if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}"):
                                    if(Class_MST()):
                                        i+=1
                                        if(token_type[i] == "}"):
                                            return True

        return False
    
    def Param_List():
        global i, token_type
        if(token_type[i] == "DT"):
            if(Param()):
                i+=1
                if(token_type[i] == "," or token_type[i] == ")"):
                    if(Param_Tail()):
                        return True

        elif(token_type[i] == ")"):
            return True

        return False
    
    def Param():
        global i, token_type
        if(token_type[i] == "DT"):
            i+=1
            if(token_type[i] == "ID"):
                return True

        return False
    
    def Param_Tail():
        global i, token_type
        if(token_type[i] == "," ):
            i+=1
            if(token_type[i] == "DT"):
                if(Param()):
                    i+=1
                    if(token_type[i] == "," or token_type[i] == ")"):
                        if(Param_Tail()):
                            return True


        elif(token_type[i] == ")"):
            return True
        return False
    
    def Body_Func():
        global i, token_type
        if(token_type[i] == "Void"):
            i+=1
            if(token_type[i] == "Func"):
                i+=1
                if(token_type[i] =="ID"):
                    i+=1
                    if(token_type[i] == "("):
                        i+=1
                        if(token_type[i] == "DT" or token_type[i] == ")"):
                            if(PL()):
                                i+=1
                                if(token_type[i] == ")"):
                                    i+=1
                                    if(token_type[i] =="{" or token_type[i] =="Override"):
                                        if(Z1()):
                                            return True

        elif(token_type[i] == "DT"):
            i+=1
            if(token_type[i] == "Func"):
                i+=1
                if(token_type[i] =="ID"):
                    i+=1
                    if(token_type[i] == "("):
                        i+=1
                        if(token_type[i] == "DT" or token_type[i] == ")"):
                            if(PL()):
                                i+=1
                                if(token_type[i] == ")"):
                                    i+=1
                                    if(token_type[i] =="}" or token_type[i] =="Override"):
                                        if(Z1()):
                                            return True

            
        elif(token_type[i] =="Virtual"):
            if(Virtual_Func()):
                return True

        elif(token_type[i] =="Static"):
            if(Static_Func()):
                return True

        return False
    
    def Z1():
        global i, token_type
        if(token_type[i] == "{"):
            i+=1
            if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}"):
                if(Class_MST()):
                    i+=1
                    if(token_type[i] == "}"):
                        return True

        elif(token_type[i] =="Override"):
            i+=1
            if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}"):
                if(Class_MST()):
                    i+=1
                    if(token_type[i] == "}"):
                        return True

        return False
    
    def Func1():
        global i, token_type
        if(token_type[i] == "void" or token_type[i] == "DT"):
            if(Ret_Type()):
                i+=1
                if(token_type[i] == "Func"):
                    i+=1
                    if(token_type[i] =="ID"):
                        i+=1
                        if(token_type[i] == "("):
                            i+=1
                            if(token_type[i] == "DT" or token_type[i] == ")"):
                                if(PL()):
                                    i+=1
                                    if(token_type[i] == ")"):
                                        i+=1
                                        if(token_type[i] == "{"):
                                            i+=1
                                            if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}"):
                                                if(Class_MST()):
                                                    i+=1
                                                    if(token_type[i] == "}"):
                                                        return True

        return False
    
    def Virtual_Func():
        global i, token_type
        if(token_type[i] == "Virtual"):
            i+=1
            if(token_type[i] == "void" or token_type[i] == "DT"):
                if(Ret_Type()):
                    i+=1
                    if(token_type[i] == "Func"):
                        i+=1
                        if(token_type[i] =="ID"):
                            i+=1
                            if(token_type[i] == "("):
                                i+=1
                                if(token_type[i] == "DT" or token_type[i] == ")"):
                                    if(Param_List):
                                        i+=1
                                        if(token_type[i] == ")"):
                                            i+=1
                                            if(token_type[i] == "="):
                                                i+=1
                                                if(token_value[i] == "0"):
                                                    i+=1
                                                    if(token_type[i] == ";"):
                                                        return True

        return False
    
    def Overriden_Func():
        global i, token_type
        if(token_type[i] == "void" or token_type[i] == "DT"):
            if(Ret_Type()):
                i+=1
                if(token_type[i] == "Func"):
                    i+=1
                    if(token_type[i] =="ID"):
                        i+=1
                        if(token_type[i] == "("):
                            i+=1
                            if(token_type[i] == "DT" or token_type[i] == ")"):
                                if(PL()):
                                    i+=1
                                    if(token_type[i] == ")"):
                                        i+=1
                                        if(token_type[i] == "Override"):
                                            i+=1
                                            if(token_type[i] == "{"):
                                                i+=1
                                                if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}"):
                                                    if(Class_MST()):
                                                        i+=1
                                                        if(token_type[i] == "}"):
                                                            return True
        return False
    
    def Static_Func():
        global i, token_type
        if(token_type[i] == "Static"):
            i+=1
            if(token_type[i] == "void" or token_type[i] == "DT"):
                if(Ret_Type()):
                    i+=1
                    if(token_type[i] == "Func"):
                        i+=1
                        if(token_type[i] =="ID"):
                            i+=1
                            if(token_type[i] == "("):
                                i+=1
                                if(token_type[i] == "DT" or token_type[i] == ")"):
                                    if(PL()):
                                        i+=1
                                        if(token_type[i] == ")"):
                                            i+=1
                                            if(token_type[i] == "{"):
                                                i+=1
                                                if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}"):
                                                    if(Class_MST()):
                                                        i+=1
                                                        if(token_type[i] == "}"):
                                                            return True
        return False
    
    def Destructor():
        global i, token_type
        if(token_type[i] == "-:"):
            i+=1
            if(token_type[i] == "ID"):
                i+=1
                if(token_type[i] == "("):
                    i+=1
                    if(token_type[i] == ")"):
                        i+=1
                        if(token_type[i] == ";"):
                            return True
        return False
    
    def AM1():
        global i, token_type
        if(token_type[i] == "AM"):
            return True

        elif(token_type[i] == "ID"):
            return True

        return False
    
    def AM2():
        global i, token_type
        if(token_type[i] == "AM"):
            i+=1
            if(token_type[i] == ":"):
                return True
            return True

        elif(token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] =="Void" or token_type[i] =="Virtual" or token_type[i] =="Static" or token_type[i] == "-:"):
            return True
        return False
    
    def Self():
        global i, token_type
        if(token_type[i] == "Self"):
            i+=1
            if(token_type[i] == "."):
                return True

        elif(token_type[i] == "ID"):
            return True
        return False
    
    def Class_MST():
        global i, token_type
        if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon"):
            if(Class_SST()):
                i+=1
                if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}"):
                    if(Class_MST()):
                        return True
            
        elif(token_type[i] == "}"):
            return True
        return False
    
    def Class_SST():
        global i, token_type
        if(token_type[i] == "Self"):
                i+=1
                if(token_type[i] == "ID"):
                    i+=1
                    if(token_type[i] == "." or token_type[i] == "[" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "=" or token_type[i] == "OP_assign" ):
                        if(X()):
                            i+=1
                            if(token_type[i] == "inc_dec" or token_type[i] == "=" or token_type[i] == "OP_assign" ):
                                if(B1()):
                                    return True

        elif(token_type[i] == "ID"):
            i+=1
            if(token_type[i] == "=" or token_type[i] == "ID" or token_type[i] == "." or token_type[i] == "[" or token_type[i] == "(" or token_type[i] == "Self" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}" ):
                if(B3()):
                    return True
            
        elif(token_type[i] == "If"):
            if(If_St()):
                return True

        elif(token_type[i] == "For"):
            if(For()):
                return True

        elif(token_type[i] == "BreakCon"):
            i+=1
            if(token_type[i] == ";"):
                return True

        elif(token_type[i] == "Return"):
            if(Return()):
                return True

        elif(token_type[i] == "DT"):
            if(Dec()):
                i+=1
                if(token_type[i] == ";"):
                    return True

        elif(token_type[i] == "inc_dec"):
            i+=1
            if(token_type[i] == "Self" or token_type[i] == "ID"):
                if(Self()):
                    i+=1
                    if(token_type[i] == "ID"):
                        i+=1
                        if(token_type[i] == "." or token_type[i] == "[" or token_type[i] == "(" or token_type[i] == ";"):
                            if(X()):
                                i+=1
                                if(token_type[i] == ";"):
                                    return True   
        return False
    
    def B1():
        global i, token_type
        if(token_type[i] == "=" or token_type[i] == "OP_assign"):
            if(AO()):
                i+=1
                if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "(" or token_type[i] == "Not" or token_type[i] == "inc_deec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "char_const" or token_type[i] == "bool_const" or token_type[i] == "str_const"):
                    if(OE_CLass()):
                        return True

        elif(token_type[i] == "inc_dec"):
            return True

        return False
    
    def B2():
        global i, token_type
        if(token_type[i] == "="):
            i+=1
            if(token_type[i] == "{"):
                i+=1
                if(token_type[i] == "(" or token_type[i] == "}"):
                    if(Dict1()):
                        i+=1
                        if(token_type[i] == "}"):
                            return True

        elif(token_type[i] == "ID"):
            i+=1
            if(token_type[i] == "(" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}"):
                if(X6()):
                    return True
        return False
    
    def B3():
        global i, token_type
        if(token_type[i] == "." or token_type[i] == "[" or token_type[i] == "(" or token_type[i] == "inc_dec" or token_type[i] == "=" or token_type[i] == "OP_assign"):
            if(X()):
                i+=1
                if(token_type[i] == "inc_dec" or token_type[i] == "=" or token_type[i] == "OP_assign"):
                    if(B1()):
                        return True

        elif(token_type[i] == "=" or token_type[i] == "ID"):
            if(B2()):
                return True
        return False
    
    # CLASS ASSIGNMENT STATEMENT -- COMPLETED
    def Class_Assign_St():
        global i, token_type
        if(token_type[i] == "Self" or token_type[i] == "ID"):
            if(Self()):
                i+=1
                if(token_type[i] == "ID"):
                    i+=1
                    if(token_type[i] == "." or token_type[i] == "(" or token_type[i] == "[" or token_type[i] == "=" or token_type[i] == "OP_assign"):
                        if(X()):
                            i+=1
                            if(token_type[i] == "=" or token_type[i] == "OP_assign"):
                                if(AO()):
                                    i+=1
                                    if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "(" or token_type[i] == "Not" or token_type[i] == "inc_deec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "char_const" or token_type[i] == "bool_const" or token_type[i] == "str_const"):
                                        if(OE_CLass()):
                                            return True

        return False
    # Other X, Xo, X1 and AO are same as simple Assignment Statement

    # CLASS INCREMENT DECREMENT STATEMENT -- COMPLETED  
    def Class_Inc_Dec_St():
        global i, token_type
        if(token_type[i] == "Self" or token_type[i] == "ID"):
            if(Self()):
                i+=1
                if(token_type[i] == "ID"):
                    i+=1
                    if(token_type[i] == "." or token_type[i] == "(" or token_type[i] == "[" or token_type[i] == "inc_dec"):
                        if(X()):
                            i+=1
                            if(token_type[i] == "inc_dec"):
                                return True

        elif(token_type[i] == "inc_dec"):
            i+=1
            if(token_type[i] == "Self" or token_type[i] == "ID"):
                if(Self()):
                    i+=1
                    if(token_type[i] == "ID"):
                        i+=1
                        if(token_type[i] == "." or token_type[i] == "(" or token_type[i] == "[" or token_type[i] == ";" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}"  or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] == "PM" or token_type[i] == "MDM" or token_type[i] == "P" or token_type[i] == ")"):
                            if(X()):
                                return True


        return False

    # CLASS EXPRESSION -- COMPLETED 
    def F_Class():
        global i, token_type
        if(token_type[i] == "Self" or token_type[i] == "ID"):
            if(Self()):
                i+=1
                if(token_type[i] == "ID"):
                    i+=1
                    if(token_type[i] == "." or token_type[i] == "(" or token_type[i] == "[" or token_type[i] == ";" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}"  or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] == "PM" or token_type[i] == "MDM" or token_type[i] == "P"  or token_type[i] == ")"):
                        if(X5()):
                            return True

        elif(token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "str_const" or token_type[i] == "bool_const" or token_type[i] == "char_const"):
            if(Const()):
                return True

        elif(token_type[i] == "("):
            i+=1
            if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "(" or token_type[i] == "Not" or token_type[i] == "inc_deec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "char_const" or token_type[i] == "bool_const" or token_type[i] == "str_const"):
                if(OE_CLass()):
                    i+=1
                    if(token_type[i] == "("):
                        return True

        elif(token_type[i] == "Not"):
            i+=1
            if(token_type[i] == ";" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}"  or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] == "PM" or token_type[i] == "MDM" or token_type[i] == "P" or token_type[i] == ")"):
                if(F_Class()):
                    return True

        elif(token_type[i] == "inc_dec"):
            i+=1
            if(token_type[i] == "Self" or token_type[i] == "ID"):
                if(Self()):
                    i+=1
                    if(token_type[i] == "ID"):
                        i+=1
                        if(token_type[i] == "." or token_type[i] == "(" or token_type[i] == "[" or token_type[i] == ";" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}"  or token_type[i] == "OR_op" or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] == "PM" or token_type[i] == "MDM" or token_type[i] == "P"  or token_type[i] == ")"):
                            if(X()):
                                return True
        return False
    
    def OE_CLass():
        global i, token_type
        if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "(" or token_type[i] == "Not" or token_type[i] == "inc_deec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "char_const" or token_type[i] == "bool_const" or token_type[i] == "str_const"):
            if(AE_Class()):
                i+=1
                if(token_type[i] == "OR_op" or token_type[i] == ";" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}" or token_type[i] == ")"):
                    if(OE_Class_()):
                        return True

        return False
    
    def OE_Class_():
        global i, token_type
        if(token_type[i] == "OR_op"):
            i+=1
            if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "(" or token_type[i] == "Not" or token_type[i] == "inc_deec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "char_const" or token_type[i] == "bool_const" or token_type[i] == "str_const"):
                if(AE_Class()):
                    i+=1
                    if(token_type[i] == "OR_op" or  token_type[i] == ";" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}" or token_type[i] == ")"):
                        if(OE_Class_()):
                            return True

        elif(token_type[i] == ";" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}" or token_type[i] == ")"):
            return True
        return False
    
    def AE_Class():
        global i, token_type
        if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "(" or token_type[i] == "Not" or token_type[i] == "inc_deec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "char_const" or token_type[i] == "bool_const" or token_type[i] == "str_const"):
            if(RE_Class()):
                i+=1
                if(token_type[i] == "AND" or token_type[i] == ";" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}" or token_type[i] == "OR_op" or token_type[i] == ")"):
                    if(AE_Class_()):
                        return True

        return False
    
    def AE_Class_():
        global i, token_type
        if(token_type[i] == "AND"):
            i+=1
            if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "(" or token_type[i] == "Not" or token_type[i] == "inc_deec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "char_const" or token_type[i] == "bool_const" or token_type[i] == "str_const"):
                if(RE_Class()):
                    i+=1
                    if(token_type[i] == "AND" or token_type[i] == ";" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}" or token_type[i] == "OR_op" or token_type[i] == ")"):
                        if(AE_Class_()):
                            return True

        elif(token_type[i] == ";" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}" or token_type[i] == "OR_op" or token_type[i] == ")"):
            return True
        return False
    
    def RE_Class():
        global i, token_type
        if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "(" or token_type[i] == "Not" or token_type[i] == "inc_deec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "char_const" or token_type[i] == "bool_const" or token_type[i] == "str_const"):
            if(E_Class()):
                i+=1
                if(token_type[i] == "RO" or token_type[i] == ";" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}"  or token_type[i] == "OR_op"  or token_type[i] == "AND" or token_type[i] == ")"):
                    if(RE_Class_()):
                        return True
        return False
    
    def RE_Class_():
        global i, token_type
        if(token_type[i] == "RO"):
            i+=1
            if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "(" or token_type[i] == "Not" or token_type[i] == "inc_deec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "char_const" or token_type[i] == "bool_const" or token_type[i] == "str_const"):
                if(E_Class()):
                    i+=1
                    if(token_type[i] == "RO" or token_type[i] == ";" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}"  or token_type[i] == "OR_op"  or token_type[i] == "AND" or token_type[i] == ")"):
                        if(RE_Class_()):
                            return True

        elif(token_type[i] == ";" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}"  or token_type[i] == "OR_op"  or token_type[i] == "AND" or token_type[i] == ")"):
            return True
        return False
    
    def E_Class():
        global i, token_type
        if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "(" or token_type[i] == "Not" or token_type[i] == "inc_deec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "char_const" or token_type[i] == "bool_const" or token_type[i] == "str_const"):
            if(T_Class()):
                i+=1
                if(token_type[i] == "PM" or token_type[i] == ";" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}"or token_type[i] == "OR_op"  or token_type[i] == "AND" or token_type[i] == "RO"or token_type[i] == ")"):
                    if(E_Class_()):
                        return True
        return False
    
    def E_Class_():
        global i, token_type
        if(token_type[i] == "PM"):
            i+=1
            if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "(" or token_type[i] == "Not" or token_type[i] == "inc_deec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "char_const" or token_type[i] == "bool_const" or token_type[i] == "str_const"):
                if(T_Class()):
                    i+=1
                    if(token_type[i] == "PM" or token_type[i] == ";" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}"or token_type[i] == "OR_op"  or token_type[i] == "AND" or token_type[i] == "RO"or token_type[i] == ")"):
                        if(E_Class_()):
                            return True

        elif(token_type[i] == ";" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}"or token_type[i] == "OR_op"  or token_type[i] == "AND" or token_type[i] == "RO"or token_type[i] == ")"):
            return True
        return False
    
    def T_Class():
        global i, token_type
        if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "(" or token_type[i] == "Not" or token_type[i] == "inc_deec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "char_const" or token_type[i] == "bool_const" or token_type[i] == "str_const"):
            if(PE_Class()):
                i+=1
                if(token_type[i] == "MDM" or token_type[i] == ";" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}" or token_type[i] == "OR_op"  or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] == "PM" or token_type[i] == ")"):
                    if(T_Class_()):
                        return True

        return False
    
    def T_Class_():
        global i, token_type
        if(token_type[i] == "MDM"):
            i+=1
            if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "(" or token_type[i] == "Not" or token_type[i] == "inc_deec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "char_const" or token_type[i] == "bool_const" or token_type[i] == "str_const"):
                if(PE_Class()):
                    i+=1
                    if(token_type[i] == "MDM" or token_type[i] == ";" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}" or token_type[i] == "OR_op"  or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] == "PM" or token_type[i] == ")"):
                        if(T_Class_()):
                            return True

        elif(token_type[i] == ";" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}" or token_type[i] == "OR_op"  or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] == "PM" or token_type[i] == ")"):
            return True
        return False
    
    def PE_Class():
        global i, token_type
        if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "(" or token_type[i] == "Not" or token_type[i] == "inc_deec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "char_const" or token_type[i] == "bool_const" or token_type[i] == "str_const"):
            if(F_Class()):
                i+=1
                if(token_type[i] == "P" or token_type[i] == ";" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}" or token_type[i] == "OR_op"  or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] == "PM" or token_type[i] == "MDM" or token_type[i] == ")"):
                    if(PE_Class_()): 
                        return True

        return False
    
    def PE_Class_():
        global i, token_type
        if(token_type[i] == "P"):
            i+=1
            if(token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "(" or token_type[i] == "Not" or token_type[i] == "inc_deec" or token_type[i] == "int_const" or token_type[i] == "float_const" or token_type[i] == "char_const" or token_type[i] == "bool_const" or token_type[i] == "str_const"):
                if(F_Class()):
                    i+=1
                    if(token_type[i] == "P" or token_type[i] == ";" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}" or token_type[i] == "OR_op"  or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] == "PM" or token_type[i] == "MDM" or token_type[i] == ")"):
                        if(PE_Class_()):
                            return True

        elif(token_type[i] == ";" or token_type[i] == "Self" or token_type[i] == "ID" or token_type[i] == "DT" or token_type[i] == "If" or token_type[i] == "For" or token_type[i] == "Return" or token_type[i] == "BreakCon" or token_type[i] == "}" or token_type[i] == "OR_op"  or token_type[i] == "AND" or token_type[i] == "RO" or token_type[i] == "PM" or token_type[i] == "MDM" or token_type[i] == ")"):
            return True
        return False
  
except LookupError:
    print("Tree Incomplete... Input Completely Parsed")

    

print("\nSynatx Analyzer Result\n")
syntaxAnalyzer()