import argparse

class crack:

    parser = None
    config = None
    
    def __init__(self):
        self.parse()

    def parse(self):
        #Create Parser
        self.parser = argparse.ArgumentParser()
        #Load default arguments

        self.parser.add_argument("-f", "--f", type=str, help="regex for the flag format")
        self.parser.add_argument("-m", "--mod", type=str, help="module to load")
        
        #Parse arguments
        self.config = vars(self.parser.parse_args())

if __name__ == "__main__":
    crack()