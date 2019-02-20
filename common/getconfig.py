import configparser,sys
#sys.path.append("..")


class GetCof(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        #path = './common/'
        path = './'
        self.config.read(path+"panda-config.txt")
        #self.config.read("panda-config.txt")

    def getbutton(self,section,button,):
        k = self.config.get(section,button)
        return k

    def getphonee(self):
        k = self.config.get('mobile','nickname')
        return k
        
        




        

    
        
