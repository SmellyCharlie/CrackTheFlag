import argparse
from mods import *
import importlib
import glob

class CrackTheFlag:

    modules = {}
    parser = None
    config = None
    
    
    def __init__(self):
        
        self.load_modules()
        self.parse()
        self.crack()

    def load_modules(self):
        
        for file in glob.glob('mods/*/*[a-zA-Z0-9].py'):
            self.modules[file.split("/")[2][:-3]] = importlib.import_module(file.replace("/", ".")[:-3])

    def parse(self):
        
        #Create Parser
        self.parser = argparse.ArgumentParser()
       
        #Load default arguments

        self.parser.add_argument("-f", "--f", type=str, help="regex for the flag format")
        self.parser.add_argument("-m", "--mod", type=str, help="module to load")
        
        #Load arguments from mods

        for mod in self.modules.values():
            mod.Module.add_arguments(self, self.parser)

        #Parse arguments
        self.config = vars(self.parser.parse_args())

    def crack(self):
        try:
            #TODO accept uppercase lol
            mod = self.modules.get(self.config["mod"])
            mod.Module(self)
        except:
            print("Module could not be found")
            return

if __name__ == "__main__":
    CrackTheFlag()