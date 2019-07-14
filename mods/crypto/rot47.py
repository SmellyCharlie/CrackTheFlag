class Module():

    def __init__(self, crack):
        self.evaluate(crack)


    @classmethod
    def add_arguments(cls, crack, parser):
        parser.add_argument('--rot47-c', default="", type=str, help='cipher text for rot47')

    def evaluate(self, crack):
        cipher_text = crack.config["rot47_c"]
        for offset in range(0,93):
            plain_text = ""
            for c in cipher_text:
                if ord(c) >= 33 and ord(c) <= 126:
                     plain_text += chr(33 + ((ord(c) + offset) % 94))
                else:
                    plain_text += c
            print(str(offset) + ": " + plain_text) 