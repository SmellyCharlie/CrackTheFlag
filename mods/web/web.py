from .robots import Module as robots

class Module():

    url = ""
    directories = []

    @classmethod
    def add_arguments(cls, crack, parser):
        parser.add_argument('--web-url', default="", type=str, help='url for web module')

    def __init__(self, crack):
        self.url = crack.config["web_url"]
        self.evaluate(crack)


    def evaluate(self, crack):
        robots(self)
        return