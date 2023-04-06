import requests
from chattools.config import PROXY_ADDR
import logging
logger = logging.getLogger(__file__)


class MyChatGPT(object):
    def __init__(self, key):
        self._key = key
        self._select_model = ''
        self._proxy = None
        if PROXY_ADDR:
            self._proxy = {
                "http": "socks5://{}".format(PROXY_ADDR),
                "https": "socks5://{}".format(PROXY_ADDR)
            }
        self._session = requests.session()
    
    def get_models(self):
        headers = {
            "Authorization": "Bearer {}".format(self._key)
        }
        url = 'https://api.openai.com/v1/models'
        r = self._session.get(url, headers=headers, proxies=self._proxy)
        return r.json()['data']
    
    def select_model(self, s='text-davinci-003'):
        rs = self.get_models()
        for it in rs:
            logger.info("model:{}".format(it['id']))
            if it['id'].startswith(s):
                self._select_model = it['id']
                break
        
    def chat(self, s):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self._key)
        }
        url = 'https://api.openai.com/v1/chat/completions'
        json_data = {
            "model": self._select_model,
            "messages": [{"role": "user",
                          "content": "{}".format(s)}]
        }
        res = self._session.post(url, headers=headers, json=json_data, proxies=self._proxy)
        res_data = res.json()['choices']
        if res_data:
            return res_data[0]['message']['content'].strip('\r\n\t ')

    def create_image(self, s, size="1024x1024", count=2):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self._key)
        }
        url = 'https://api.openai.com/v1/images/generations'
        json_data = {
            "prompt": s,
            "n": count,
            "size": size
        }
        res = self._session.post(url, headers=headers, json=json_data, proxies=self._proxy)
        res_list = []
        res_data = res.json()['data']
        for _it in res_data:
            res_list.append(_it['url'])
        return res_list
