class ParseHandle:
    

    class InputParse:
        def __init__(self,):
            self = self 
        """Entry point, passing usr_io string and initial parameters."""
        def ParseParam(self, pstr, pass_param):
            self.setting = pass_param   

           # set = self.setting
            
            pstr = self.pstr
            
            slen = len(pstr)
            c = 0    
            while c < slen:
                if pstr[c] == '-':
                    pass 
                c += c
                

    def __init__(self,):
        self = self
   #     self.param_init = self.param_init    
    
    def set_param(self):
        default_param = ('sel_sort', False, 'integer', 'compare', False, False, False, 1)
        saved_param = ()
        if not saved_param:
           self.pass_param = default_param
            
        return self.pass_param
    def initialize_params(self):
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
        if not err:   
            usr_input = input("Enter a list of values and/or parameters. (Enter -h for help): ")
        else:
            print (err)
        return usr_input
if __name__ == "__main__":
    hndl = ParseHandle()
    b = hndl.usr_io()
    inpr = hndl.InputParse()
    a = inpr.p_str
    inpr.ParseParam(a, b)
