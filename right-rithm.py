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
            d = 1
            print(slen)
            while c < slen:
                if p_str[c] == '-' and p_str[d] != '-':
                    print(p_str[d])
                    while p_str[c].isspace() or p_str[c] != '-':
                        print(p_str[c])
                        flags.append(p_str[c]) 
                        d += 1
                        c += 1
                print(flags)        
                c += 1
                d += 1
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
    print(in_prm)
    ParseHandle.InputParse.ParseParam(in_usr, in_prm)
