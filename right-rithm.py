class ParseHandle:
    

    class InputParse:
        def __init__(self,):
            self = self 
        def ParseParam(self, p_str, pass_param):
            """Entry point, passing usr_io string and initial parameters."""

            self.setting = pass_param   
            self.p_str = p_str

           # set = self.setting
            print (self.setting)            
            print (self.p_str)
            
            slen = len(p_str)
            c = 0    
            while c < slen:
                if p_str[c] == '-':
                    pass 
                c += c

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
            'time_Complex': None,
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

