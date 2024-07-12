class ParseHandle:
    

    class InputParse:
        """Parse input data and flags or return exceptions"""

        def __init__(self,): 
            self = self


        def ParseParam(p_str, pass_param):

            """Entry point, passing usr_io string to initial parameters."""
            for c, p in enumerate(p_str):
                d = c + 1
                if p == '-' and p_str[d] != '-':
                    flg_e = p_str.find(' ', c)
                    if flg_e == -1:
                        flg_grp = p_str[d:]
                        print(flg_grp)
                    else:
                        flg_grp = p_str[d:flg_e]
                        print(flg_e) 
                        print(flg_grp)
                    if flg_grp.find('='):
                        val_b = flg_grp.index('=')
                        key_e = val_b - 1
                        key = flg_grp[d:key_e]
                        print(key)
                        
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
