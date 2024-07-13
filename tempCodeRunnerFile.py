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