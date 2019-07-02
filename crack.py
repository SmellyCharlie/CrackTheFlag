import argparse

class crack:

    parser = None
    config = None
    
    def __init__(self):
        self.parse()

    def parse(self):
        #Create Parser
        parser = argparse.ArgumentParser()
        #Load default arguments
        parser.add_argument("-f", "--f",  help="regex for the flag format")
        parser.add_argument()
        #Parse arguments
        parser.parse_args()

if __name__ == "__main__":
    crack()