class Module():

    def __init__(self, crack):
        self.evaluate(crack)


    @classmethod
    def add_arguments(cls, crack, parser):
        parser.add_argument('--caesar-c', default="", type=str, help='cipher text for caesar cipher')

    def evaluate(self, crack):
        cipher_text = crack.config["caesar_c"]
        for offset in range(0,26):
            plain_text = ""
            for c in cipher_text:
                if c.isalpha():
                    if (c.isupper()): 
                        plain_text += chr((ord(c) + offset - 65) % 26 + 65) 
                    else: 
                        plain_text += chr((ord(c) + offset - 97) % 26 + 97)
                else:
                    plain_text += c
            print(str(offset) + ": " + plain_text) 