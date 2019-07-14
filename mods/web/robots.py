import requests
import re

class Module():

    @classmethod
    def add_arguments(cls, crack, parser):
        return

    def __init__(self, web):
        self.evaluate(web)

    def evaluate(self, web):
        #TODO
        #Make this change user agent as a robot, and not a robot, so it avoids manual blocking
        url = web.url + "/robots.txt"
        print("Robots.txt:")
        try:
            r = requests.get(url)
            for line in r.text.splitlines():
                if re.search("(Allow:|Disallow:)", line):
                    print("     " + line)
                    web.directories.append(line.split(" ")[1])
        except:
            print("    No robots.txt found")
        