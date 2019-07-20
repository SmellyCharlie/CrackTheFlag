import requests
from string import Template


class Module:
    url_template = Template('https://www.md5.ovh/index.php?md5=$hash&result=json')

    def __init__(self, crack):
        self.evaluate(crack)

    @classmethod
    def add_arguments(cls, _, parser):
        parser.add_argument('--md5', default='', type=str, help='Check if there\'s a known hash on '
                                                                'https://www.md5.ovh')

    def evaluate(self, crack):
        hash = crack.config['md5']
        url = self.url_template.substitute(hash=hash)
        response = requests.get(url=url)
        if response.ok:
            try:
                resp_data = response.json()[0]
                if resp_data['result'] == 'OK':
                    print('Known hash:')
                    print(f'Decrypted: {resp_data["decrypted"]}')
                    print(f'Hex:       {resp_data["decryptedHexadecimal"]}')
                elif resp_data['result'] == 'KO':
                    print('Nothing found')
            except ValueError:
                print(response.text)
