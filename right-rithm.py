class ParseHandle:
    

    class InputParse:
        """Parse input data and flags or return exceptions"""

        def __init__(self,): 
            self = self


        def ParseParam(p_str, pass_param):

            """Entry point, passing usr_io string to initial parameters."""
            flags = []
            slen = len(p_str)
            c = 0
            while c < slen:
                d = c + 1
                if p_str[c] == '-'and p_str[d] != '-':     #check flag for abbr. or verbode format.
                    flg_e = p_str.find(' ', c)          
                    if flg_e == -1:                        #check for string end by index reversal.
                        flg_e = slen + 1
                    flg = p_str[d:flg_e]
                    value = ''
                    for i in flg:
                        if p_str[d+1] != '=' and not value:
                            flags.append(i)
                            print (flags)
                            d += 1
                        elif i == '=':
                            value = p_str[d:flg_e]
                            flags.append(value)
                            print(flags)
                            d == flg_e
                            break
                        print(d)
                c += 1
    def __init__(self,):
        self = self
    #     self.param_init = self.param_init    
    
    def set_param():
        default_param = ('sel_sort', False, 'integer', 'compare', False, False, False, 1)
        saved_param = ()
        if not saved_param:
            pass_param = default_param
        return pass_param   
    
    def initialize_params(self,):
       self.param = {
            'algorithm': None,
            'verbose': None,
            'data_type_in': None,
            'compare': None,
            'time_complex': None,
            'colorize': None,
            'log': None,
            'data_div': None
        }
    def usr_io(err = False):
       # if not err:   
        usr_input = input("Enter a list of values and/or parameters. (Enter -h for help): ")
      #  else:
      #      print (err)
        return usr_input

if __name__ == "__main__":
    in_usr = ParseHandle.usr_io()
    in_prm = ParseHandle.set_param()
    ParseHandle.InputParse.ParseParam(in_usr, in_prm)
