import requests


class MyChatGPT(object):
    def __init__(self, key):
        self._key = key
        self._select_model = ''
        self._session = requests.session()
    
    def get_models(self):
        url = ''
        return url
        r = self._session.get(url)
        return r.json()
    
    def select_model(self, s=''):
        rs = self.get_models()
        for it in rs:
            if it.find(s) >= 0:
                self._select_model = it
                break
        
    def chat(self, s):
        return s


