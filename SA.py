from LA2 import tokenize

class SyntaxAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.token_index = -1
        self.errors = []

    def get_next_token(self):
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
            return True
        return False

    def syntax_error(self, expected):
        self.errors.append(f"Syntax Error: Expected {expected} but got {self.current_token[0]}")

    def parse(self):
        if self.get_next_token():
            if self.Start_Nt():
                print("\n\t\t\t\t\t\t\t Congratulations! Syntax is correct.\n\t\t\t\t\t\t\t=====================================")
            else:
                print("\n\t\t\t\t\t\t\t !!! Ooops :( Wrong Syntax !!! \n\t\t\t\t\t\t\t ============================== ")
                if self.errors:
                    for error in self.errors:
                        print(error)
        else:
            print("No tokens to analyze.")

    # Grammar rules
    # _____________

    # START 
    def Start_Nt(self): 
        if self.current_token[0] == 'DT':
            T = self.current_token[1]
            # print("Value: ", T)
            if (self.get_next_token() and self.Y2()):
                return True
        elif self.current_token[0] == 'Void':
            T = 'void'
            if (self.get_next_token() and self.Y5()):
                return True
        elif self.current_token[0] == 'ID':
            N = self.current_token[1]
            if self.get_next_token() and self.Y4():
                if self.Return_Type():
                    if self.current_token[0] == 'Main' and self.get_next_token():
                        if self.current_token[0] == '(':
                            #  Create_Scope()
                            if self.get_next_token() and self.current_token[0] == ')':
                                if self.get_next_token() and self.current_token[0] == '{':
                                    if self.get_next_token() and self.Mst():
                                        if self.current_token[0] == '}':
                                            # Destroy_Scope()
                                            if self.Defs():
                                                return True
        elif (self.current_token[0] == 'Class'):
                T = 'klass'
                if self.get_next_token() and self.current_token[0] == 'ID':
                    N = self.current_token[1]
                    if self.get_next_token() and self.Inherit():
                        if self.current_token[0] == '=>' and self.get_next_token():
                            # InsertDT()
                            if self.current_token[0] == '{' and self.get_next_token():
                                if self.Class_Body():
                                    if self.get_next_token() and self.current_token[0] == '}':
                                        if self.get_next_token() and self.current_token[0] == ';' and self.get_next_token():
                                            if self.Defs():
                                                if self.get_next_token() and self.Return_Type():
                                                    if self.current_token[0] == 'Main' and self.get_next_token():
                                                        if self.current_token[0] == '(' and self.get_next_token():
                                                            # createScope()
                                                            if self.current_token[0] == ')' and self.get_next_token():
                                                                if self.current_token[0] == '{' and self.get_next_token():
                                                                    if self.Mst():
                                                                        if self.current_token[0] == '}':
                                                                            # DestroyScope()
                                                                            if self.Defs():
                                                                                return True
        
        return False
    
    def Y2(self):
        if self.current_token[0] == 'ID' or self.current_token[0] == 'Func':
            if self.Y1():
                if self.Return_Type():
                    if self.current_token[0] == 'Main' and self.get_next_token():
                        if self.current_token[0] == '(' and self.get_next_token():
                            # CreateScope()
                            if self.current_token[0] == ')' and self.get_next_token():
                                if self.current_token[0] == '{' and self.get_next_token():
                                    if self.Mst():
                                        if self.current_token[0] == '}':
                                            # DestroyScope()
                                            if self.Defs():
                                                return True
        elif self.current_token[0] == 'Main' and self.get_next_token():
            if self.current_token[0] == '(' and self.get_next_token():
                 # CreateScope()
                if self.current_token[0] == ')':
                    if self.get_next_token() and self.current_token[0] == '{':
                        if self.get_next_token() and self.Mst():
                            if self.current_token[0] == '}':
                                 # DestroyScope()
                                if self.Defs():
                                    return True

        return False  
    
    def Y5(self):
        if self.current_token[0] == 'Func':
            
            if self.get_next_token() and self.current_token[0] == 'ID':
                N = self.current_token[1]
                if self.get_next_token():
                    if self.current_token[0] == '(':
                         # CreateScope()
                        if self.get_next_token() and self.Pl():
                            if self.current_token[0] == ')':
                                # Type_Expression = PL + '->' + T
                                # insertST(..,Type_Expression,..)
                                if self.get_next_token() and self.current_token[0] == '{' and self.get_next_token():
                                    if self.Mst():
                                        if self.current_token[0] == '}':
                                            # DestroyScope()
                                            if self.get_next_token() and self.Defs():
                                                if self.get_next_token() and self.Return_Type():
                                                    if self.current_token[0] == 'Main' and self.get_next_token():
                                                        if self.current_token[0] == '(':
                                                            # CreateScope()
                                                            if self.get_next_token() and self.current_token[0] == ')' and self.get_next_token():
                                                                if self.current_token[0] == '{' and self.get_next_token():
                                                                    if self.Mst():
                                                                        if self.current_token[0] == '}':
                                                                            # DestroyScope()
                                                                            if self.Defs():
                                                                                return True
        elif self.current_token[0] == 'Main' and self.get_next_token():
            if self.current_token[0] == '(':
                # CreateScope()
                if self.get_next_token() and self.current_token[0] == ')' and self.get_next_token():
                    if self.current_token[0] == '{' and self.get_next_token():
                        if self.Mst():
                        #     if self.current_token[0] == '}':
                        #         # DestroyScope()
                        #         if self.Defs():
                                    return True

        return False  
    
    # START END 

    # DEFINITION 
    def Defs(self):
        
        if self.current_token[0] == 'DT':
                T = self.current_token[1]
                if self.get_next_token() and self.Y1():
                    return True
        elif self.current_token[0] == 'Void':
            T = 'void'
            if self.get_next_token() and self.current_token[0] == 'Func':
                if self.get_next_token() and self.current_token[0] == 'ID':
                    N = self.current_token[1]
                    if self.get_next_token() and self.current_token[0] == '(':
                        # CreateScope()
                        if self.get_next_token() and self.Pl():
                            if self.current_token[0] == ')':
                                # Type_Expression = PL + '->' + T
                                # insertST(..,Type_Expression,..)
                                if self.get_next_token() and self.current_token[0] == '{':
                                    if self.get_next_token() and self.Mst():
                                        if self.current_token[0] == '}':
                                            # DestroyScope()
                                            if self.Defs():
                                                return True
        elif self.current_token[0] == 'ID':
            N = self.current_token[1]
            if self.get_next_token() and self.Y4():
                return True
        elif self.current_token[0] == 'Class':
            T = 'klass'
            if self.get_next_token() and self.current_token[0] == 'ID':
                N = self.current_token[1]
                if self.get_next_token() and self.Inherit():
                    if self.current_token[0] == '=>':
                        # InsertDT()
                        if self.get_next_token() and self.current_token[0] == '{':
                            if self.get_next_token() and  self.Class_Body():
                                if self.get_next_token() and self.current_token[0] == '}':
                                    if self.get_next_token() and self.current_token[0] == ';':
                                        if self.Defs():
                                            return True
        elif self.current_token[0] == '@' or self.current_token[0] == ';' or self.current_token[0] == '}' or self.current_token[0] == 'DT' or self.current_token[0] == 'Void' or self.current_token[0] == 'ID' : # done 
            return True

        return False
    def Y1(self):
        if self.current_token[0] == 'ID':
            N = self.current_token[1]
            if self.get_next_token() and self.Y3():
                return True
        elif self.current_token[0] == 'Func':
            if self.get_next_token() and self.current_token[0] == 'ID':
                N = self.current_token[1]
                if self.get_next_token() and self.current_token[0] == '(':
                    # CreateScope()
                    if self.get_next_token() and self.Pl():
                        if self.current_token[0] == ')':
                            # Type_Expression = PL + '->' + T
                            # insertST(..,Type_Expression,..)
                            if self.get_next_token() and self.current_token[0] == '{':
                                if self.get_next_token() and self.Mst():
                                    if self.current_token[0] == '}':
                                        # DestroyScope()
                                        if self.Defs():
                                            return True
        return False
    
    def Y3(self):

        if self.current_token[0] == '=':
            op = self.current_token[1]
            if self.get_next_token() and self.Y6():
                return True
        elif self.current_token[0] == ',' or self.current_token[0] == ';':
            if self.List():
                if self.current_token[0] == ';':
                    if self.get_next_token() and self.Defs():
                        return True
        return False
    
    def Y4(self):
        if self.current_token[0] == 'Func':
            T = N
            if self.get_next_token() and self.current_token[0] == 'ID':
                N = self.current_token[1]
                if self.get_next_token() and self.current_token[0] == '(':
                    # CreateScope()
                    if self.get_next_token() and self.Pl():
                        if self.current_token[0] == ')':
                            # Type_Expression = PL + '->' + T
                            # insertST(..,Type_Expression,..)
                            if self.get_next_token() and self.current_token[0] == '{':
                                if self.get_next_token() and self.Mst():
                                    if self.current_token[0] == '}':
                                        # Destroyscope()
                                        if self.get_next_token() and self.Defs():
                                            return True
        elif self.current_token[0] == 'ID':
            N = self.current_token[1]
            if self.get_next_token() and self.current_token[0] == '=':
                op = self.current_token[1]
                if self.get_next_token() and self.current_token[0] == '[':
                    # T = T + '[]'
                    # InsertST()
                    if self.List1():
                        if self.current_token[0] == ']':
                            # Bin_Type_Comp()
                            if self.get_next_token() and self.current_token[0] == ';':
                                if self.get_next_token() and self.Defs():
                                    return True
        elif self.current_token[0] == '=':
            op = self.current_token[1]
            if self.get_next_token() and self.current_token[0] == '{':
                # T = "{}"
                # InsertST(N,T,S)
                if self.Dict1() and self.current_token[0] == '}':
                    if self.get_next_token() and self.current_token[0] == ';':
                        if self.get_next_token() and self.Defs():
                            return True
        return False
    
    def Y6(self):
        if self.current_token[0] == 'ID' or self.current_token[0] == 'Self' or self.current_token[0] == 'int_const' or self.current_token[0] == 'float_const' or self.current_token[0] == 'char_const' or self.current_token[0] == 'bool_const' or self.current_token[0] == 'str_const' or self.current_token[0] == '(' or self.current_token[0] == 'Not' or self.current_token[0] == 'inc_dec':
            if self.Init2():
                if self.List():
                    if self.current_token[0] == ';':
                        if self.get_next_token():
                            return self.Defs()
        elif self.current_token[0] == '[':
            # T = T + '[]'
            # InsertST()
            if self.List1():
                if self.current_token[0] == ']':
                    # Bin_Type_comp()
                    if self.get_next_token() and self.current_token[0] == ';':
                        if self.get_next_token() and self.Defs():
                            return True
        return False
    # DEFINITION END

    # TYPE 
    def Type(self):
        if self.current_token[0] in ['DT', 'ID']:
            T = self.current_token[1]
            if self.get_next_token():
                return True
        else:
            self.syntax_error("DT or ID")
        return False
    # TYPE END  

    #DECLARATION 
    def Init(self):
        if self.current_token[0] == '=':
            op = self.current_token[1]
            if self.get_next_token() and self.Init2():
                return True
        elif self.current_token[0] == ',' or self.current_token[0] == ';' :  # done
            return True
        return False
    
    def List(self):
        if self.current_token[0] == ',':
            if self.get_next_token() and self.current_token[0] == 'ID':
                N = self.current_token[1]
                if self.get_next_token() and self.Init():
                    if self.List():
                        return True
        elif self.current_token[0] == ',' or self.current_token[0] == ';' :  
            # InsertST()
            # done
            return True
        return False
    
    def Init2(self):
        if self.current_token[0] == 'ID':
            N = self.current_token[1]
            if self.get_next_token() and self.Init():
                return True
        elif self.current_token[0] == 'ID' or self.current_token[0] == 'Self' or self.current_token[0] == 'int_const' or self.current_token[0] == 'float_const' or self.current_token[0] == 'char_const' or self.current_token[0] == 'bool_const' or self.current_token[0] == 'str_const' or self.current_token[0] == '(' or self.current_token[0] == 'Not' or self.current_token[0] == 'inc_dec': 
            if self.OE():
                # Bin_Type_Ccomp()
                if self.List():
                    return True
        return False
    #DECLARATION END 

    #LIST DECLARATION 
    def List1(self):
        if self.current_token[0] == 'ID' or self.current_token[0] == 'Self' or self.current_token[0] == 'int_const' or self.current_token[0] == 'float_const' or self.current_token[0] == 'char_const' or self.current_token[0] == 'bool_const' or self.current_token[0] == 'str_const' or self.current_token[0] == '(' or self.current_token[0] == 'Not' or self.current_token[0] == 'inc_dec':
        
            if self.OE(): 
                if self.List1_():
                    return True
        elif self.current_token[0] == '[':
            if self.get_next_token() and self.List1():
                if self.current_token[0] == ']':
                    if self.get_next_token() and self.List1_():
                        return True
        elif self.current_token[0] == ']':
            # T = '_'
            # done
            return True 
        return False
    
    def List1_(self):
        if self.current_token[0] == ',':
            if self.get_next_token() and self.List3():
                # if (List1_type != List3_type):
                    # "Type mismatch"
                    return True
        elif self.current_token[0] == ']': 
            # T = T1
             # done
            return True
        return False
    
    def List3(self):
        if self.current_token[0] == 'ID' or self.current_token[0] == 'Self' or self.current_token[0] == 'int_const' or self.current_token[0] == 'float_const' or self.current_token[0] == 'char_const' or self.current_token[0] == 'bool_const' or self.current_token[0] == 'str_const' or self.current_token[0] == '(' or self.current_token[0] == 'Not' or self.current_token[0] == 'inc_dec':
            if self.OE():
                if self.List1_():
                    return True
        elif self.current_token[0] == '[':
            if self.get_next_token() and self.List1():
                if self.current_token[0] == ']':
                    if self.get_next_token() and self.List1_():
                        return True
        return False
    #LIST DECLARATION END

    # MULTI LINE STATEMENT 
    def Mst(self):
        
        if self.current_token[0] == 'ID' or self.current_token[0] == 'Self' or self.current_token[0] == 'DT' or self.current_token[0] == 'Void' or self.current_token[0] == 'inc_dec' or self.current_token[0] == 'For' or self.current_token[0] =='If' or self.current_token[0] == 'BreakCon' or self.current_token[0] == 'Return':
            if self.Sst():
                # if self.Mst():
                    return True
        elif self.current_token[0] == '}':  # done
            return True
        return False
    # MULTI LINE STATEMENT END 

    # RETURN STATEMENT 
    def Return(self):
        if self.current_token[0] == 'Return':
            if self.get_next_token() and self.R1():
                if self.current_token[0] == ';':
                    # if T != Func_Ret_Type:
                        # "Type mismatch"
                    if self.get_next_token():
                        return True
        return False
    
    def R1(self):
        if self.current_token[0] == 'ID' or self.current_token[0] == 'Self' or self.current_token[0] == 'int_const' or self.current_token[0] == 'float_const' or self.current_token[0] == 'char_const' or self.current_token[0] == 'bool_const' or self.current_token[0] == 'str_const' or self.current_token[0] == '(' or self.current_token[0] == 'Not' or self.current_token[0] == 'inc_dec':
            if self.OE():
                return True
        elif self.current_token[0] == ';':
            # T = 'void'
            # done
            return True     
        return False
    # RETURN STATEMENT END

    # DICTIONARY 
    def Dict1(self):
        if self.current_token[0] == '(':
            if self.Pair():
                if self.Dict1_():
                    return True
        elif self.current_token[0] == '}':  # done
            return True
        return False
    
    def Dict1_(self):
        if self.current_token[0] == ',':
            if self.get_next_token() and self.Pair():
                if self.Dict1_():
                    return True
        elif self.current_token[0] == '}':  # done
            return True
        return False
    
    def Pair(self):
        if self.current_token[0] == '(':
            if self.get_next_token() and self.Const():
                if self.current_token[0] == ',':
                    if self.get_next_token() and self.Value():
                        if self.current_token[0] == ')':
                            if self.get_next_token():
                                return True
        return False
    
    def Value(self):
        if self.current_token[0] == 'ID' or self.current_token[0] == 'Self' or self.current_token[0] == 'int_const' or self.current_token[0] == 'float_const' or self.current_token[0] == 'char_const' or self.current_token[0] == 'bool_const' or self.current_token[0] == 'str_const' or self.current_token[0] == '(' or self.current_token[0] == 'Not' or self.current_token[0] == 'inc_dec':
            if self.OE():
                return True
        elif self.current_token[0] == '[':
            if self.get_next_token() and self.List1():
                if self.current_token[0] == ']':
                    if self.get_next_token():
                        return True
        elif self.current_token[0] == '{':
            if self.get_next_token() and self.Dict1():
                if self.current_token[0] == '}':
                    if self.get_next_token():
                        return True
        return False
    # DICTIONARY END
    
    # CONSTANT 
    def Const(self):
        if self.current_token[0] in ['int_const', 'bool_const', 'float_const', 'char_const', 'str_const']:
            T = self.current_token[1]
            if self.get_next_token():
                return True
        return False
    # CONSTANT END 

    # RETURN TYPE
    def Return_Type(self):
        if self.current_token[0] == "DT" or self.current_token[0] == "Void" or self.current_token[0] == "ID":
            T = self.current_token[1]
            if self.get_next_token():
                return True
        return False
    # RETURN TYPE END 

    # PARAMETER LIST 
    def Pl(self):
        if self.current_token[0] == 'DT' or self.current_token[0] == 'ID':
            if self.P1():
                if self.Pl_():
                    # PL = T
                    return True
        elif self.current_token[0] == ')':
            # PL = 'void'
            # done
            return True
        return False
    
    def Pl_(self):
        if self.current_token[0] == ',':
            if self.get_next_token() and self.P1():
                if self.Pl_():
                    # PL += ',' + T
                    return True
        elif self.current_token[0] == ')':  # done
            return True
        return False
    
    def P1(self):
        if self.current_token[0] == 'DT' or self.current_token[0] == 'ID':
            if self.Type():
                if self.current_token[0] == 'ID':
                    N = self.current_token[1]
                    # InsetST()
                    if self.get_next_token() and self.P2():
                        return True
        elif self.current_token[0] == ',' or self.current_token[0] == ')':  # done
            return True
        return False
    
    def P2(self):
        if self.current_token[0] == '=':
            op = self.current_token[1]
            if self.get_next_token() and self.OE():
                # Bin_Type_comp()
                return True
        elif self.current_token[0] == ',' or self.current_token[0] == ')':
            #T = T1
              # done
            return True
        return False
    # PARAMETER LIST END

    # ARGUMENT LIST 
    def Al(self):
        if self.current_token[0] == 'ID' or self.current_token[0] == 'Self' or self.current_token[0] == 'int_const' or self.current_token[0] == 'float_const' or self.current_token[0] == 'char_const' or self.current_token[0] == 'bool_const' or self.current_token[0] == 'str_const' or self.current_token[0] == '(' or self.current_token[0] == 'Not' or self.current_token[0] == 'inc_dec' :
            if self.OE():
                if self.Al1():
                    # PL = T
                    return True
        elif self.current_token[0] == ')':
            PL = 'void'
              # done
            return True
        return False
    
    def Al1(self):
        if self.current_token[0] == ',':
            if self.get_next_token() and self.OE():
                if self.Al1():
                    # PL += ',' + T
                    return True
        elif self.current_token[0] == ')':  # done
            return True
        return False
    # ARGUMENT LIST END

    # FOR LOOP 
    def For_St(self):
        if self.current_token[0] == 'For':
            if self.get_next_token() :
                if self.current_token[0] == '(':
                    # CreateScope()
                    if self.get_next_token() and self.F1():
                        if self.current_token[0] == ';' and self.get_next_token():
                            if self.F2():
                                if self.current_token[0] == ';' and self.get_next_token():
                                    if self.F3():
                                        if self.current_token[0] == ')' and self.get_next_token():
                                            if self.Body():
                                                # DestroyScope()
                                                return True
        return False
    
    def F1(self):
        if self.current_token[0] == 'DT':
            T = self.current_token[1]
            if self.get_next_token() and self.current_token[0] == 'ID':
                N = self.current_token[1]
                if self.get_next_token() and self.Init():
                    if self.List():
                        return True
        elif self.current_token[0] == 'ID':
            CR = '_'
            N = self.current_token[1]
            if self.get_next_token() and self.A1():
                return True
        elif self.current_token[0] == 'Self':
            if self.get_next_token() and self.current_token[0] == '.':
                # CR = CCR 
                if self.get_next_token() and self.current_token[0] == 'ID':
                    N = self.current_token[1]
                    if self.get_next_token() and self.B3():
                        if self.AO():
                            if self.OE():
                                # Bin_Type_Comp()
                                return True
        elif self.current_token[0] == ';':  # done
            return True
        return False
    
    def A1(self):
        if self.current_token[0] == 'ID':
            T = N
            N = self.current_token[1]
            if self.get_next_token() and self.Init():
                if self.List():
                    return True
        elif self.current_token[0] == '.' or self.current_token[0] == '[' or self.current_token[0] == '(' or self.current_token[0] == '=' or self.current_token[0] == 'OP_assign' or self.current_token[0] == 'inc_dec':
            if self.B3():
                if self.AO(): 
                    if self.OE():
                        # Bin_Type_Comp
                        return True
        return False
    
    def F2(self):
        if self.current_token[0] == 'ID' or self.current_token[0] == 'Self' or self.current_token[0] == 'int_const' or self.current_token[0] == 'float_const' or self.current_token[0] == 'char_const' or self.current_token[0] == 'bool_const' or self.current_token[0] == 'str_const' or self.current_token[0] == '(' or self.current_token[0] == 'Not' or self.current_token[0] == 'inc_dec' :
            if self.OE():
                return True
        elif self.current_token[0] == ';':  # done
            return True
        return False
    
    def F3(self):
        if self.current_token[0] == 'Self':
            if self.get_next_token() and self.current_token[0] == '.':
                # CR = CCR
                if self.get_next_token() and self.current_token[0] == 'ID':
                    N = self.current_token[1]
                    if self.get_next_token() and self.B3():
                        if self.get_next_token() and self.F4():
                            return True
        elif self.current_token[0] == 'ID':
            N = self.current_token[1]
            CR = '_'
            if self.get_next_token() and self.B3():
                 if self.F4():
                    return True
        elif self.current_token[0] in ['inc_dec']:
            op = self.current_token[1]
            if self.get_next_token() and self.Self():
                if self.current_token[0] == 'ID':
                    N = self.current_token[1]
                    if self.get_next_token() and self.X():
                        # Uni_Type_Comp()
                        return True
        return False
    
    def F4(self):
        if self.current_token[0] == 'inc_dec':
            op = self.current_token[1]
            # uni_type_comp()
            if self.get_next_token():
                return True
        elif self.current_token[0] == '=' or self.current_token[0] == 'OP_assign' :
            if self.AO(): 
                if self.OE():
                    # Bin_type_comp()
                    return True
        return False
    
    def Self(self):
        if self.current_token[0] == 'Self':
            if self.get_next_token() and self.current_token[0] == '.':
                # CR = CCR 
                return True
        elif self.current_token[0] == 'ID':
             # CR = '_'
             # done
            return True
        return False
    
    def B3(self):
        # if CR == '_':
            # T = lookupST(N):
            # if T == False:
                # RMT = lookupMT(N,CCR)
                # if RMT == False
                    # "undeclared id"
                # else:
                #   T = RMT.type
                    # if RMT.AM == 'secure':
                     # "this var can't accessed outside the class"
        # elif CR == CCR:
            # RMT = lookupMT(name, CR)
            # if RMT == False:
                # "Undeclared id"
            # else:
            #   T = RMT.Type
        if self.current_token[1] == '.':
            # if T == "ID":
                # RDT = lookupDT(T)
                # if RDT == False:
                    # "CLass is not Defined"
            # else:
                # 'Dot is not valid'
            if self.get_next_token() and self.current_token[0] == 'ID':
                N = self.current_token[1]
                if self.get_next_token() and self.B3() and self.get_next_token():
                    return True

        elif self.current_token[1] == '[' and self.get_next_token():
            if self.OE():
                # if T != 'int':
                #   "Invalid index"
                if self.current_token[1] == ']':
                    # if CR == '_':
                        # T = lookupST(N):
                        # if T == False:
                            # RMT = lookupMT(N,CCR)
                            # if RMT == False
                                # "undeclared id"
                            # else:
                            #   T = RMT.type
                                # if RMT.AM == 'secure':
                                    # "this var can't accessed outside the class"
                    # elif CR == CCR:
                        # RMT = lookupMT(name, CR)
                        # if RMT == False:
                            # "Undeclared id"
                        # else:
                            #   T = RMT.Type
                    # if T contains '[]':
                    #   "Correct"
                    # else:
                        # "array does not exist"
                    if self.get_next_token() and self.B3() and self.get_next_token():
                        return True

        elif self.current_token[1] == '(' and self.get_next_token():
            if self.Al():
                if self.current_token[1] == ')':
                    # if CR == '_':
                        # RMT = lookupFuncMT(N, PL, CCR)
                        # if RMT == False:
                            # check in all parent classes
                            # T = lookupfuncST(N,PL)
                            # if T == False:
                            #   "Undeclared"
                        # else:
                        #   T = RMT.type
                    # elif CR == CCR:
                    #   RMT = lookupFuncMT(N,PL,CR)
                    #   if RMT == False:
                    #       "undeclared"
                    #   else:
                    #       T = RMT.type
                    if self.get_next_token() and self.current_token[1] == '.':
                        # if T == "ID":
                            # RDT = lookupDT(T)
                            # if RDT == False:
                                # "CLass is not Defined"
                        # else:
                            # 'Dot is not valid'
                        if self.get_next_token() and self.current_token[0] == 'ID':
                            N = self.current_token[1]
                            if self.get_next_token() and self.B3() and self.get_next_token():
                                return True
        elif self.current_token[0] == '=' or self.current_token[0] == 'OP_assign' or self.current_token[0] == 'inc_dec':
            # if CR == '_':
            # T = lookupST(N):
            # if T == False:
                # RMT = lookupMT(N,CCR)
                # if RMT == False
                    # "undeclared id"
                # else:
                #   T = RMT.type
                    # if RMT.AM == 'secure':
                     # "this var can't accessed outside the class"
        #     elif CR == CCR:
                # RMT = lookupMT(name, CR)
                # if RMT == False:
                    # "Undeclared id"
                # else:
                #   T = RMT.Type
             # done 
            return True
        return False
    # FOR LOOP END 

    # IF STATEMENT 

    def If_St(self):
        if self.current_token[0] == 'If':
            if self.get_next_token():
                if self.current_token[0] == '(' and self.get_next_token():
                    if self.OE():
                        # if self.current_token[0] == ')' and self.get_next_token():
                            # Create_Scope()
                            # if self.Body(): 
                            #     Destroy_Scope()
                            #     if self.Elif():
                            #         if self.Default():
                                        return True
        return False
    
    def Elif(self):
        if self.current_token[0] == 'Elif':
            if self.get_next_token():
                if self.current_token[0] == '(' and self.get_next_token():
                    if self.OE():
                        if self.current_token[0] == ')' and self.get_next_token():
                            #Create_scope()
                            if self.Body():
                                # Destroy_Scope()
                                if  self.Elif():
                                    return True
        elif self.current_token[0] == 'DT' or self.current_token[0] == 'Self' or self.current_token[0] == 'inc_dec' or self.current_token[0] == 'ID' or self.current_token[0] == 'Void' or self.current_token[0] == 'For'or self.current_token[0] == 'If' or self.current_token[0] == 'BreakCon' or self.current_token[0] == 'Return' or self.current_token[0] == '}' or self.current_token[0] == 'Default' : # done
            return True
        return False
    
    def Default(self):
        if self.current_token[0] == 'Default':
            if self.get_next_token() :
                #Create_scope()
                if self.Body() :
                    # Destroy_Scope()
                    return True
        elif self.current_token[0] == 'DT' or self.current_token[0] == 'Self' or self.current_token[0] == 'inc_dec' or self.current_token[0] == 'ID' or self.current_token[0] == 'Void' or self.current_token[0] == 'For'or self.current_token[0] == 'If' or self.current_token[0] == 'BreakCon' or self.current_token[0] == 'Return' or self.current_token[0] == '}' or self.current_token[0] == 'Elif' or self.current_token[0] == 'Default' :  # done
            return True
        return False
    # IF STATEMENT END 

    # BODY 
    def Body(self):
        if self.current_token[0] == ';':
            if self.get_next_token():
                return True
        if self.current_token[0] == 'ID' or self.current_token[0] == 'Self' or self.current_token[0] == 'DT' or self.current_token[0] == 'Void' or self.current_token[0] == 'inc_dec' or self.current_token[0] == 'For' or self.current_token[0] == 'If' or self.current_token[0] == 'BreakCon' or self.current_token[0] == 'Return':
            if self.Sst():
                return True
        elif self.current_token[0] == '{' and self.get_next_token():
            if self.Mst():
                if self.current_token[0] == '}':
                    return True
        return False
    # BODY END 

    # SINGLE LINE STATEMENT 
    def Sst(self):
        if self.current_token[0] == 'DT':
            T = self.current_token[1]
            if self.get_next_token() and self.S1():
                return True
        elif self.current_token[0] == 'Self':
            if self.get_next_token() and self.current_token[0] == '.':
                #CR = CCR
                if self.get_next_token() and self.current_token[0] == 'ID':
                    N=self.current_token[1]
                    if self.get_next_token() and self.S2():
                        return True
        elif self.current_token[0] == 'ID':
            N=self.current_token[1]
            #CR = '_'
            if self.get_next_token() and self.S2():
                return True
        elif self.current_token[0] == 'inc_dec':
            op= self.current_token[1]
            if self.get_next_token() and self.Self():
                if self.current_token[0] == 'ID':
                    N=self.current_token[1]
                    if  self.get_next_token() and self.X():
                        #Uni_Type_Comp()
                        if  self.get_next_token() and self.current_token[0] == ';' and self.get_next_token():
                            return True
        elif self.current_token[0] == 'Void':
            T=self.current_token[1]
            if self.get_next_token() and self.current_token[0] == 'Func':
                if self.get_next_token() and self.current_token[0] == 'ID':
                    N=self.current_token[1]
                    if self.get_next_token() and self.current_token[0] == '(':
                        #Create_Scope()
                        if self.get_next_token() and self.Pl():
                            if self.current_token[0] == ')':
                                # Type_Expresion = PL + "->"+ T
                                # insertST()
                                if self.get_next_token():
                                    if self.current_token[0] == '{' and self.get_next_token():
                                        if self.Mst():
                                            if self.current_token[0] == '}':
                                                # Destroy_Scope()
                                                if self.get_next_token():
                                                    return True
        elif self.current_token[0] == 'For':
            if self.For_St():
                return True  
        elif self.current_token[0] == 'If':
            if self.If_St():
                return True  
        elif self.current_token[0] == 'Return':
            if self.Return():
                #check must be present inside a function
                return True  
        
        elif self.current_token[0] == 'BreakCon':
            # BC= True
            # check if it is present inside loop then valid
            if self.get_next_token() and self.current_token[0] == ';':
                if self.get_next_token():
                    return True
        return False
    
    def S1(self):
        if self.current_token[0] == 'ID':
            N=self.current_token[1]
            if self.get_next_token() and self.S5():
                return True
        elif self.current_token[0] == 'Func':
            if self.get_next_token() and self.current_token[0] == 'ID':
                N=self.current_token[1]
                if self.get_next_token():
                    if self.current_token[0] == '(':
                        # Create_Scope()
                        if self.get_next_token() and self.Pl():
                            if self.current_token[0] == ')':
                                if self.get_next_token():
                                    # Type_Expression = PL+ "->" + T
                                    # insertST()
                                    if self.current_token[0] == '{' and self.get_next_token():
                                        if self.Mst():
                                            if self.current_token[0] == '}':
                                                # Destroy_Scope()
                                                if self.get_next_token():
                                                    return True
        return False
    
    def S2(self):
        # if(CR='_'):
        #   T=lookUpST(N)
        #   check in all parent scopes
        #   if(T==False):
        #       RMT=lookUpMT(N,CCR)
        #       if(RMT==False):
        #           "Undeclared"
        #       else:
        #           T=RMT.Type
        #       if(RMT.AM=="secure"):
        #           "variable can't be accessed outside of the class"
        # elif(CR==CCR):
        #   RMT=lookUpMT(N,CR)
        #   if(RMT=="_"):
        #       "Undeclared"
        #   else:
        #       T=RMT.Type
        if self.current_token[0] == '.':
            # if T == "ID":
                # RDT = lookupDT(T)
                # if RDT == False:
                    # "CLass is not Defined"
            # else:
                # 'Dot is not valid'
            if self.get_next_token() and self.current_token[0] == 'ID':
                N=self.current_token[1]
                if self.get_next_token() and self.B():
                    if self.current_token[0] == ';' and self.get_next_token():
                        return True
        elif self.current_token[0] == '[':
            if self.get_next_token() and self.OE():
                #if(T!="int"):
                #   "invalid index"
                if self.current_token[0] == ']':
                    # if(CR='_'):
                    #   T=lookUpST(N)
                    #   check in all parent scopes
                    #   if(T==False):
                    #       RMT=lookUpMT(N,CCR)
                    #       if(RMT==False):
                    #           "Undeclared"
                    #       else:
                    #           T=RMT.Type
                    #       if(RMT.AM=="secure"):
                    #           "variable can't be accessed outside of the class"
                    # elif(CR==CCR):
                    #   RMT=lookUpMT(N,CR)
                    #   if(RMT=="_"):
                    #       "Undeclared"
                    #   else:
                    #       T=RMT.Type
                    #if(T contains "[]"):
                    #   "it is valid"
                    if self.get_next_token() and self.B():
                        if self.current_token[0] == ';' and self.get_next_token():
                            return True
        elif self.current_token[0] == '(':
            if self.get_next_token() and self.Al():
                if self.current_token[0] == ')':
                    # if CR == '_':
                    #   RMT = lookupFuncMT(N, PL, CCR)
                    #   if RMT == False:
                    #       check in all parent classes
                    #       T = lookupfuncST(N,PL)
                    #       if T == False:
                    #          "Undeclared"
                    #   else:
                    #      T = RMT.type
                    # elif CR == CCR:
                    #   RMT = lookupFuncMT(N,PL,CR)
                    #   if RMT == False:
                    #       "undeclared"
                    #   else:
                    #       T = RMT.type
                    if self.get_next_token() and self.B1():
                        if self.current_token[0] == ';' and self.get_next_token():
                            return True
        elif self.current_token[0] == 'inc_dec':
            op=self.current_token[1]
            #Uni_Type_Comp()
            if self.get_next_token() and self.current_token[0] == ';':
                if self.get_next_token():
                    return True
        elif self.current_token[0] == 'OP_assign':
            op=self.current_token[1]
            if self.get_next_token() and self.OE():
                if self.current_token[0] == ';' and self.get_next_token():
                    return True
        elif self.current_token[0] == ';':
            if self.get_next_token():
                return True
        elif self.current_token[0] == 'ID':
            N=self.current_token[1]
            if self.get_next_token() and self.S3():
                return True
        elif self.current_token[0] == 'Func':
            if self.get_next_token() and self.current_token[0] == 'ID':
                N=self.current_token[1]
                if self.current_token[0] == '(':
                    #Create_Scope()
                    if self.get_next_token() and self.Pl():
                        if self.current_token[0] == ')':
                            # Type_Expression = PL+ "->" + T
                            # insertST()
                            if self.get_next_token():
                                if self.current_token[0] == '{' and self.get_next_token():
                                    if self.Mst():
                                        if self.current_token[0] == '}':
                                            #Destroy_Scope()
                                            if self.get_next_token():
                                                return True
        elif self.current_token[0] == '=':
            op=self.current_token[1]
            if self.get_next_token() and self.B2():
                return True
        return False
    
    def S3(self):
        #insertST()
        if self.current_token[0] == ';':
            if self.get_next_token():
                return True
        elif self.current_token[0] == '=':
            op=self.current_token[1]
            if self.get_next_token() and self.S4():
                return True
        return False
    
    def S4(self):
        if self.current_token[0] == '[':
            # T = T + "[]"
            # insertST()
            if self.get_next_token() and self.List1():
                if self.current_token[0] == ']':
                    #Bin_Type_Comp()
                    if self.get_next_token():
                        if self.current_token[0] == ';' and self.get_next_token():
                            return True
        elif self.current_token[0] == 'New':
            if self.get_next_token() and self.current_token[0] == 'ID':
                N=self.current_token[1]
                if self.get_next_token():
                    if self.current_token[0] == '(' and self.get_next_token():
                        if self.current_token[0] == ')':
                            # RDT=lookUpDT(N)
                            # if RDT == False:
                            #   "Class is not defined"
                            # also --> child class object can't refer to parent class
                            #   "Type mismatch"
                            if self.get_next_token():
                                if self.current_token[0] == ';' and self.get_next_token():
                                    return True
        return False
    
    def S5(self):
        if self.current_token[0] == '=':
            op=self.current_token[1]
            if self.get_next_token():
                return self.S6()
        elif self.current_token[0] == ',' or self.current_token[0] == ';':
            if self.List():
                if self.current_token[0] == ';':
                    if self.get_next_token():
                        return True
        return False


    def S6(self):
        if self.current_token[0] == 'ID' or self.current_token[0] == 'Self' or self.current_token[0] == 'int_const' or self.current_token[0] == 'float_const' or self.current_token[0] == 'char_const' or self.current_token[0] == 'bool_const' or self.current_token[0] == 'str_const' or self.current_token[0] == '(' or self.current_token[0] == 'Not' or self.current_token[0] == 'inc_dec' :
            if self.Init2():
                if self.List():
                    if self.current_token[0] == ';':
                        if self.get_next_token():
                            return True
        elif self.current_token[0] == '[':
            # T = T + "[]"
            # insertST()
            if self.List1():
                # Bin_Type_Comp()
                if self.current_token[0] == ']':
                    if self.get_next_token():
                        return True
        return False
    
    def B(self):
        # if(CR='_'):
        #   T=lookUpST(N)
        #   check in all parent scopes
        #   if(T==False):
        #       RMT=lookUpMT(N,CCR)
        #       if(RMT==False):
        #           "Undeclared"
        #       else:
        #           T=RMT.Type
        #       if(RMT.AM=="secure"):
        #           "variable can't be accessed outside of the class"
        # elif(CR==CCR):
        #   RMT=lookUpMT(N,CR)
        #   if(RMT=="_"):
        #       "Undeclared"
        #   else:
        #       T=RMT.Type
        if self.current_token[0] == '.':
             # if T == "ID":
                # RDT = lookupDT(T)
                # if RDT == False:
                    # "CLass is not Defined"
            # else:
                # 'Dot is not valid'
            if self.get_next_token() and self.current_token[0] == 'ID':
                N=self.current_token[1]
                if self.get_next_token() and self.B():
                    return True
        elif self.current_token[0] == '[':
            if self.get_next_token() and self.OE() :
                #if(T!="int"):
                #   "invalid index"
                if self.get_next_token():
                    if self.current_token[0] == ']':
                        # if(CR='_'):
                        #   T=lookUpST(N)
                        #   check in all parent scopes
                        #   if(T==False):
                        #       RMT=lookUpMT(N,CCR)
                        #       if(RMT==False):
                        #           "Undeclared"
                        #       else:
                        #           T=RMT.Type
                        #       if(RMT.AM=="secure"):
                        #           "variable can't be accessed outside of the class"
                        # elif(CR==CCR):
                        #   RMT=lookUpMT(N,CR)
                        #   if(RMT=="_"):
                        #       "Undeclared"
                        #   else:
                        #       T=RMT.Type
                        #if(T contains "[]"):
                        #   "it is valid"
                        if self.get_next_token():
                            if self.B():
                                return True
        elif self.current_token[0] == '(':
            if self.get_next_token() and self.Al():
                if self.current_token[0] == ')':
                    # if CR == '_':
                    #   RMT = lookupFuncMT(N, PL, CCR)
                    #   if RMT == False:
                    #       check in all parent classes
                    #       T = lookupfuncST(N,PL)
                    #       if T == False:
                    #          "Undeclared"
                    #   else:
                    #      T = RMT.type
                    # elif CR == CCR:
                    #   RMT = lookupFuncMT(N,PL,CR)
                    #   if RMT == False:
                    #       "undeclared"
                    #   else:
                    #       T = RMT.type
                    if self.get_next_token():
                        if self.B1():
                            return True
        elif self.current_token[0] == ';':  # done
            # if(CR='_'):
            #   T=lookUpST(N)
            #   check in all parent scopes
            #   if(T==False):
            #       RMT=lookUpMT(N,CCR)
            #       if(RMT==False):
            #           "Undeclared"
            #       else:
            #           T=RMT.Type
            #       if(RMT.AM=="secure"):
            #           "variable can't be accessed outside of the class"
            # elif(CR==CCR):
            #   RMT=lookUpMT(N,CR)
            #   if(RMT=="_"):
            #       "Undeclared"
            #   else:
            #       T=RMT.Type
            return True
        elif self.current_token[0] == 'inc_dec':
            op=self.current_token[1]
            # Uni_Type_Comp()
            if self.get_next_token():
                return True
        elif self.current_token[0] == '=':
            op=self.current_token[1]
            if self.get_next_token() and self.OE():
                # Bin_Type_Comp()
                return True
        elif self.current_token[0] == 'OP_assign':
            op=self.current_token[1]
            if self.get_next_token() and self.OE():
                # Bin_Type_Comp()
                return True
        return False
    
    def B1(self):
        if self.current_token[0] == '.':
            # if T == "ID":
                # RDT = lookupDT(T)
                # if RDT == False:
                    # "CLass is not Defined"
            # else:
                # 'Dot is not valid'
            if self.get_next_token() and self.current_token[0] == 'ID':
                N=self.current_token[1]
                if self.get_next_token() and self.B():
                    return True
        elif self.current_token[0] == 'inc_dec':
            op=self.current_token[1]
            # Uni_Type_Comp()
            if self.get_next_token():
                return True
        elif self.current_token[0] == ';':  # done

            return True
        return False
    
    def B2(self):
        if self.current_token[0] == 'ID' or self.current_token[0] == 'Self' or self.current_token[0] == 'int_const' or self.current_token[0] == 'float_const' or self.current_token[0] == 'char_const' or self.current_token[0] == 'bool_const' or self.current_token[0] == 'str_const' or self.current_token[0] == '(' or self.current_token[0] == 'Not' or self.current_token[0] == 'inc_dec' :
            if self.OE():
                # Bin_Type_Comp()
                if self.current_token[0] == ';':
                    if self.get_next_token():
                        return True
        elif self.current_token[0] == '{':
            # T = "{}"
            # insertST(N,T,S)
            if self.get_next_token() and self.Dict1():
                if self.current_token[0] == '}' and self.get_next_token():
                    if self.current_token[0] == ';' and self.get_next_token():
                        return True
        return False

    # SINGLE LINE STATEMENT END 

    # EXPRESSION 
    def OE(self):
        if self.current_token[0] == 'ID' or self.current_token[0] == 'Self' or self.current_token[0] == 'int_const' or self.current_token[0] == 'float_const' or self.current_token[0] == 'char_const' or self.current_token[0] == 'bool_const' or self.current_token[0] == 'str_const' or self.current_token[0] == '(' or self.current_token[0] == 'Not' or self.current_token[0] == 'inc_dec'  :
            if self.AE():
                if self.OE_():
                    return True
        return False
    
    def OE_(self):
        if self.current_token[0] == 'OR_op':
            op=self.current_token[1]
            if self.get_next_token() and self.AE():
                # Bin_Type_Comp()
                if self.OE_():
                    return True
        elif self.current_token[0] == ',' or self.current_token[0] == ';' or self.current_token[0] == ']' or self.current_token[0] == ')':  # done
            # T = T1
            return True
        return False
    
    def AE(self):
        if self.current_token[0] == 'ID' or self.current_token[0] == 'Self' or self.current_token[0] == 'int_const' or self.current_token[0] == 'float_const' or self.current_token[0] == 'char_const' or self.current_token[0] == 'bool_const' or self.current_token[0] == 'str_const' or self.current_token[0] == '(' or self.current_token[0] == 'Not' or self.current_token[0] == 'inc_dec'  :
            if self.RE():
                if self.AE_():
                    return True
        return False
    
    def AE_(self):
        if self.current_token[0] == 'AND':
            op=self.current_token[1]
            if self.get_next_token() and self.RE():
                # Bin_Type_Comp()
                if self.AE_():
                    return True
        elif self.current_token[0] == 'OR_op' or self.current_token[0] == ',' or self.current_token[0] == ';' or self.current_token[0] == ']' or self.current_token[0] == ')': # done
             # T = T1
            return True  
        
        return False
    
    
    def RE(self):
        if self.current_token[0] == 'ID' or self.current_token[0] == 'Self' or self.current_token[0] == 'int_const' or self.current_token[0] == 'float_const' or self.current_token[0] == 'char_const' or self.current_token[0] == 'bool_const' or self.current_token[0] == 'str_const' or self.current_token[0] == '(' or self.current_token[0] == 'Not' or self.current_token[0] == 'inc_dec'  :
            if self.E():
                if self.RE_():
                    return True
        return False
    
    def RE_(self):
        if self.current_token[0] =='RO':
            op=self.current_token[1]
            if self.get_next_token() and self.E():
                # Bin_Type_Comp()
                if self.RE_():
                    return True
            
        elif self.current_token[0] == 'AND' or self.current_token[0] == 'OR_op' or self.current_token[0] == ',' or self.current_token[0] == ';' or self.current_token[0] == ']' or self.current_token[0] == ')':  # done
            # T = T1
            return True
        return False
    
    def E(self):
        if self.current_token[0] == 'ID' or self.current_token[0] == 'Self' or self.current_token[0] == 'int_const' or self.current_token[0] == 'float_const' or self.current_token[0] == 'char_const' or self.current_token[0] == 'bool_const' or self.current_token[0] == 'str_const' or self.current_token[0] == '(' or self.current_token[0] == 'Not' or self.current_token[0] == 'inc_dec'  :
            if self.T():
                if self.E_():
                    return True
        return False
    
    def E_(self):
        if self.current_token[0] =='PM':
            op=self.current_token[1]
            if self.get_next_token() and self.T():
                 # Bin_Type_Comp()
                if self.E_():
                    return True
        elif self.current_token[0] == 'RO' or self.current_token[0] == 'AND' or self.current_token[0] == 'OR_op' or self.current_token[0] == ',' or self.current_token[0] == ';' or self.current_token[0] == ']' or self.current_token[0] == ')':  # done
            # T = T1
            return True
        return False
    
    def T(self):
        if self.current_token[0] == 'ID' or self.current_token[0] == 'Self' or self.current_token[0] == 'int_const' or self.current_token[0] == 'float_const' or self.current_token[0] == 'char_const' or self.current_token[0] == 'bool_const' or self.current_token[0] == 'str_const' or self.current_token[0] == '(' or self.current_token[0] == 'Not' or self.current_token[0] == 'inc_dec'  :
            if self.PE():
                if self.T_():
                    return True
        return False
    
    def T_(self):
        if self.current_token[0] =='MDM':
            op=self.current_token[1]
            if self.get_next_token() and self.PE():
                # Bin_Type_Comp()
                if self.T_():
                    return True
        elif self.current_token[0] == 'PM' or self.current_token[0] == 'RO' or self.current_token[0] == 'AND' or self.current_token[0] == 'OR_op' or self.current_token[0] == ',' or self.current_token[0] == ';' or self.current_token[0] == ']' or self.current_token[0] == ')':  # done
            # T = T1
            return True
        return False
    
    def PE(self):
        if self.current_token[0] == 'ID' or self.current_token[0] == 'Self' or self.current_token[0] == 'int_const' or self.current_token[0] == 'float_const' or self.current_token[0] == 'char_const' or self.current_token[0] == 'bool_const' or self.current_token[0] == 'str_const' or self.current_token[0] == '(' or self.current_token[0] == 'Not' or self.current_token[0] == 'inc_dec'  :
            if self.get_next_token() and self.F():
                if self.PE_():
                    return True
        return False
    
    def PE_(self):
        if self.current_token[0] == 'P':
            op=self.current_token[1]
            if self.get_next_token() and self.F():
                # Bin_Type_Comp()
                if self.PE_():
                    return True
        elif self.current_token[0] == 'MDM' or self.current_token[0] == 'PM' or self.current_token[0] == 'RO' or self.current_token[0] == 'AND' or self.current_token[0] == 'OR_op' or self.current_token[0] == ',' or self.current_token[0] == ';' or self.current_token[0] == ']' or self.current_token[0] == ')':   # done
             # T = T1
            return True
        return False
    # EXPRESSION END 

    # OPERAND 
    def F(self):
        if self.current_token[0] == 'Self':
            if self.get_next_token():
                if self.current_token[0] == '.':
                    # CR = CCR
                    if self.current_token[0] == 'ID':
                        N=self.current_token[1]
                        if self.X1():
                            return True
        elif self.current_token[0] == 'ID':
            N=self.current_token[1]
            # CR = "_"
            if self.get_next_token() and self.X1():
                return True
        elif self.Const():
            return True
        elif self.current_token[0] == '(':
            if self.get_next_token() and self.OE():
                if self.current_token[0] == ')' and self.get_next_token():
                    return True
        elif self.current_token[0] == 'Not':
            op=self.current_token[1]
            if self.get_next_token() and self.F():
                return True
        elif self.current_token[0] == 'inc_dec':
            op=self.current_token[1]
            if self.get_next_token() and self.Self():
                if self.current_token[0] == 'ID':
                    N=self.current_token[1]
                    if self.get_next_token() and self.X():
                        # Uni_Type_Comp()
                        return True
        return False
    
    def X1(self):
        # if(CR='_'):
        #   T=lookUpST(N)
        #   check in all parent scopes
        #   if(T==False):
        #       RMT=lookUpMT(N,CCR)
        #       if(RMT==False):
        #           "Undeclared"
        #       else:
        #           T=RMT.Type
        #       if(RMT.AM=="secure"):
        #           "variable can't be accessed outside of the class"
        # elif(CR==CCR):
        #   RMT=lookUpMT(N,CR)
        #   if(RMT=="_"):
        #       "Undeclared"
        #   else:
        #       T=RMT.Type
        if self.current_token[0] == '.':
             # if T == "ID":
                # RDT = lookupDT(T)
                # if RDT == False:
                    # "CLass is not Defined"
            # else:
                # 'Dot is not valid'
            if self.get_next_token() and self.current_token[0] == 'ID':
                N=self.current_token[1]
                if  self.X1():
                    if self.X3():
                        return True
        elif self.current_token[0] == '[':
            if self.get_next_token() and self.OE():
                # if T!="int":
                #   "invalid index"
                if self.current_token[0] == ']':
                    # if(CR='_'):
                    #   T=lookUpST(N)
                    #   check in all parent scopes
                    #   if(T==False):
                    #       RMT=lookUpMT(N,CCR)
                    #       if(RMT==False):
                    #           "Undeclared"
                    #       else:
                    #           T=RMT.Type
                    #       if(RMT.AM=="secure"):
                    #           "variable can't be accessed outside of the class"
                    # elif(CR==CCR):
                    #   RMT=lookUpMT(N,CR)
                    #   if(RMT=="_"):
                    #       "Undeclared"
                    #   else:
                    #       T=RMT.Type
                    #if(T contains "[]"):
                    #   "it is valid"
                    if self.X1():
                        if self.X3():
                            return True
        elif self.current_token[0] == '(':
            if self.get_next_token() and self.Al():
                if self.current_token[0] == ')' :
                    # if CR == '_':
                    #   RMT = lookupFuncMT(N, PL, CCR)
                    #   if RMT == False:
                    #       check in all parent classes
                    #       T = lookupfuncST(N,PL)
                    #       if T == False:
                    #          "Undeclared"
                    #   else:
                    #      T = RMT.type
                    # elif CR == CCR:
                    #   RMT = lookupFuncMT(N,PL,CR)
                    #   if RMT == False:
                    #       "undeclared"
                    #   else:
                    #       T = RMT.type
                    if self.X2():
                        return True
        elif self.current_token[0] == 'P' or self.current_token[0] == 'MDM' or self.current_token[0] == 'PM' or self.current_token[0] == 'RO' or self.current_token[0] == 'AND' or self.current_token[0] == 'OR_op' or self.current_token[0] == ',' or self.current_token[0] == ';' or self.current_token[0] == ']' or self.current_token[0] == ')' or self.current_token[0] == 'inc_dec':  # done
            # if(CR='_'):
            #   T=lookUpST(N)
            #   check in all parent scopes
            #   if(T==False):
            #       RMT=lookUpMT(N,CCR)
            #       if(RMT==False):
            #           "Undeclared"
            #       else:
            #           T=RMT.Type
            #       if(RMT.AM=="secure"):
            #           "variable can't be accessed outside of the class"
            # elif(CR==CCR):
            #   RMT=lookUpMT(N,CR)
            #   if(RMT=="_"):
            #       "Undeclared"
            #   else:
            #       T=RMT.Type
            return True

        return False
    
    def X2(self):
        if self.current_token[0] == 'inc_dec':
            op=self.current_token[1]
            # Uni_Type_Comp()
            if self.get_next_token():
                return True
        elif self.current_token[0] == '.':
             # if T == "ID":
                # RDT = lookupDT(T)
                # if RDT == False:
                    # "CLass is not Defined"
            # else:
                # 'Dot is not valid'
            if self.get_next_token() and self.current_token[0] == 'ID':
                N=self.current_token[1]
                if self.X1():
                    return True
        elif self.current_token[0] == 'P' or self.current_token[0] == 'MDM' or self.current_token[0] == 'PM' or self.current_token[0] == 'RO' or self.current_token[0] == 'AND' or self.current_token[0] == 'OR_op' or self.current_token[0] == ',' or self.current_token[0] == ';' or self.current_token[0] == ']' or self.current_token[0] == ')' or self.current_token[0] == 'inc_dec':  # done
            return True
        return False
    
    def X3(self):
        if self.current_token[0] == 'inc_dec':
            op=self.current_token[1]
            # Uni_Type_Comp()
            if self.get_next_token():
                return True
        elif self.current_token[0] == 'P' or self.current_token[0] == 'MDM' or self.current_token[0] == 'PM' or self.current_token[0] == 'RO' or self.current_token[0] == 'AND' or self.current_token[0] == 'OR_op' or self.current_token[0] == ',' or self.current_token[0] == ';' or self.current_token[0] == ']' or self.current_token[0] == ')' or self.current_token[0] == 'inc_dec':  # done
            return True
        return False
    # OPERAND END 

    # CLASS 
    # def Class(self):
    #     if self.current_token[0] == 'Class':
    #         if self.get_next_token() and self.current_token[0] == 'ID':
    #             if self.get_next_token() and self.Inherit():
    #                 if self.current_token[0] == '=>' and self.get_next_token():
    #                     if self.current_token[0] == '{' and self.get_next_token():
    #                         if self.Class_Body() and self.get_next_token():
    #                              if self.current_token[0] == '}':
    #                                 if self.get_next_token() and self.current_token[0] == ';':
    #                                     return True
    #     return False
    # CLASS END 

    # INHERITANCE 
    def Inherit(self):
        if self.current_token[0] == ':':
            if self.get_next_token() and self.Inh():
                return True
        elif self.current_token[0] == '=>':  # done
            return True
        return False
    
    def Inh(self):
        if self.current_token[0] == "AccessMod":
            if self.get_next_token() and self.current_token[0] == 'ID':
                if self.get_next_token() and self.Multi_Inherit():
                    return True
        elif self.current_token[0] == 'ID':
                if self.get_next_token() and self.Multi_Inherit():
                    return True
        return False
    # INHERITANCE END 

    # MULTI INHERITANCE 
    def Multi_Inherit(self):
        if self.current_token[0] == ',':
            if self.get_next_token() and self.AM1():
                if self.current_token[0] == 'ID':
                    if self.get_next_token() and self.Multi_Inherit():
                        return True
        elif self.current_token[0] == '=>':  # done
            return True
        return False
    # MULTI INHERITANCE END 

    # ACCESS MODIFIER 
    def AM1(self):
        if self.current_token[0] == 'AccessMod':
            if self.get_next_token():
                return True
        elif self.current_token[0] == 'ID':  # done
            return True
        return False
    # ACCESS MODIFIER END 

    # CLASS MEMBERS
    def C1(self):
        if self.current_token[0] == 'DT':
            if self.get_next_token() and self.Z2():
                if self.C1():
                     return True
        elif self.current_token[0] == 'ID':
            if self.get_next_token() and self.Z3():
                return True
        elif self.current_token[0] == '-:':
            if self.get_next_token() and self.current_token[0] == 'ID':
                if self.get_next_token() and self.current_token[0] == '(':
                    if self.get_next_token() and self.current_token[0] == ')':
                        if self.get_next_token() and self.current_token[0] == '{':
                            if self.get_next_token() and self.Mst():
                                if self.current_token[0] == '}' and self.C1():
                                    return True
        elif self.current_token[0] == 'Void':
            if self.get_next_token() and self.current_token[0] == 'Func' :
                if self.get_next_token() and self.current_token[0] == 'ID':
                    if self.get_next_token() and self.current_token[0] == '(':
                        if self.get_next_token() and self.Pl():
                            if self.current_token[0] == ')' and self.get_next_token():
                                if self.Z1():
                                    if self.get_next_token() and self.C1():
                                        return True

        elif self.current_token[0] == 'Static':
            if self.get_next_token() and self.Static_Func():
                if self.get_next_token() and self.C1():
                    return True
        elif self.current_token[0] == 'Virtual' :
            if self.get_next_token() and self.Virtual_Func():
                if self.get_next_token() and self.C1():
                    return True
        elif self.current_token[0] == 'DT' or self.current_token[0] == 'Self' or self.current_token[0] == 'inc_dec' or self.current_token[0] == 'Void' or self.current_token[0] == 'For' or self.current_token[0] == 'If' or self.current_token[0] == 'BreakCon' or self.current_token[0] == 'Return' or self.current_token[0] == '}' or self.current_token[0] == 'Elif' or self.current_token[0] == 'Default' or self.current_token[0] == '-:' or self.current_token[0] == '-Static' or self.current_token[0] == 'Virtual' or self.current_token[0] == 'AccessMod':  # done
            return True
        return False
    
    def Z2(self):
        if self.current_token[0] == 'ID':
            if self.get_next_token():
                return self.S5()

        elif self.current_token[0] == 'Func':
            if self.get_next_token() and self.current_token[0] == 'ID':
                if self.get_next_token() and self.current_token[0] == '(':
                    if self.get_next_token() and self.Pl():
                        if self.current_token[0] == ')' and self.get_next_token():
                            if self.Z1():
                                if self.get_next_token() and self.C1():
                                    if self.get_next_token():
                                        return True

        return False

    def Z3(self):
        if self.current_token[0] == 'ID':
            if self.get_next_token():
                if self.S5():
                    if self.C1():
                        return True 

        elif self.current_token[0] == '(':
            if self.get_next_token() and self.Param_List():
                if self.current_token[0] == ')' and self.get_next_token():
                    if self.current_token[0] == '{' and self.get_next_token():
                        if self.Mst():
                            if self.current_token[0] == '}' and self.get_next_token():
                                if self.C1():
                                    return True

        elif self.current_token[0] == 'Func':
            if self.get_next_token() and self.current_token[0] == 'ID':
                if self.get_next_token() and self.current_token[0] == '(':
                    if self.get_next_token() and self.Pl():
                        if self.current_token[0] == ')'and self.get_next_token():
                            if self.Z1():
                                if self.get_next_token() and self.C1():
                                    return True
        return False
    # CLASS MEMBERS END 

    # PARAMETER LIST FOR CONSTRUCTORS 
    def Param_List(self):
        if self.current_token[0] == 'DT' or self.current_token[0] == 'ID' :
            if self.Param():
                return self.Param_()
        elif self.current_token[0] == ')':  # done
            return True
        return False
    
    def Param(self):
        if self.current_token[0] == 'DT' or self.current_token[0] == 'ID' :
            if self.Type():
                if self.current_token[0] == 'ID':
                    if self.get_next_token():
                        return True
        return False
    
    def Param_(self):
        if self.current_token[0] == ',':
            if self.get_next_token() and self.Param():
                if self.Param_():
                    return True
        elif self.current_token[0] == ')': # done
            return True

        return False
    # PARAMETER LIST FOR CONSTRUCTORS END 

    # STATIC FUNCTION 
    def Static_Func(self):
        if self.current_token[0] == 'Static':
            if self.Return_Type():
                if self.current_token[0] == 'Func':
                    if self.get_next_token() and self.current_token[0] == 'ID':
                        if self.get_next_token() and self.current_token[0] == '(':
                            if self.get_next_token() and self.Param():
                                if self.current_token[0] == ')' and self.get_next_token():
                                    if self.current_token[0] == '{' and self.get_next_token():
                                        if self.Mst():
                                            if self.current_token[0] == '}':
                                                return True

        return False
    # STATIC FuncTION END 

    # VIRTUAL FuncTION 
    def Virtual_Func(self):
        if self.current_token[0] == 'Virtual':
            if self.Return_Type():
                if self.current_token[0] == 'Func':
                    if self.get_next_token() and self.current_token[0] == 'ID':
                        if self.get_next_token() and self.current_token[0] == '(':
                            if self.get_next_token() and self.Param():
                                if self.current_token[0] == ')'and self.get_next_token():
                                    if self.current_token[0] == '=':
                                        if self.get_next_token() and self.current_token[0] == '0':
                                            if self.get_next_token() and self.current_token[0] == ';':
                                                return True
        return False
    # VIRTUAL FUNCTION END 

    # BODY FUNCTIONS 
  
    def Z1(self):
        if self.current_token[0] == '{':
            if self.get_next_token() and self.Mst():
                if self.current_token[0] == '}':
                    return True

        elif self.current_token[0] == 'Override':
            if self.get_next_token() and self.current_token[0] == '{':
                if self.get_next_token() and self.Mst():
                    if self.current_token[0] == '}':
                        return True
        return False
    # BODY FuncTIONS END 

     # CLASS BODY 
    def Class_Body(self):
        if self.current_token[0] == 'AccessMod':
            if self.get_next_token() and self.current_token[0] == ':':
                if self.get_next_token() and self.C1():
                    if self.get_next_token() and self.Class_Body():
                        return True
            elif self.C1():
                if self.get_next_token() and self.Class_Body():
                    return True

        elif self.current_token[0] == '}':  # done
            return True

        return False
    # CLASS BODY END 

    # AO 
    def AO(self):
        if self.current_token[0] in ['=', 'OP_assign']:
            if self.get_next_token():
                return True
        return False
    # AO End

    # X
    def X(self):
        if self.current_token[0] == '.':
            if self.get_next_token() and self.current_token[0] == 'ID':
                if self.get_next_token() and self.X():
                    return True
        elif self.current_token[0] == '[':
            if self.get_next_token() and self.OE():
                if self.current_token[0] == ']' and self.get_next_token():
                    if self.X():
                        return True
        elif self.current_token[0] == '(':
            if self.get_next_token() and self.Al():
                if self.current_token[0] == ')' and self.get_next_token():
                    if self.X4():
                        return True
        elif self.current_token[0] == 'P' or self.current_token[0] == 'MDM' or self.current_token[0] == 'PM' or self.current_token[0] == 'RO' or self.current_token[0] == 'AND' or self.current_token[0] == 'OR_op' or self.current_token[0] == ',' or self.current_token[0] == ';' or self.current_token[0] == ']' or self.current_token[0] == ')':  # done
            return True
        return False
    
    def X4(self):
        if self.current_token[0] == '.':
            if self.get_next_token() and self.current_token[0] == 'ID':
                if self.get_next_token() and self.X():
                    return True
        elif self.current_token[0] == 'P' or self.current_token[0] == 'MDM' or self.current_token[0] == 'PM' or self.current_token[0] == 'RO' or self.current_token[0] == 'AND' or self.current_token[0] == 'OR_op' or self.current_token[0] == ',' or self.current_token[0] == ';' or self.current_token[0] == ']' or self.current_token[0] == ')':  # done
            return True

        return False
    
    # X End
    
# MAIN PROGRAM
# ____________

input_file_name = "input.txt"
output_file_name = "output.txt"

with open(input_file_name, 'r') as input_file:
    source_code = input_file.read()

tokens = tokenize(source_code)
# Initializing the syntax analyzer with the tokens
syntax_analyzer = SyntaxAnalyzer(tokens)
syntax_analyzer.parse()