import requests
import logging
from chattools.config import CHATGPT_KEY, CHATGPT_MODEL
from chattools.chat import MyChatGPT

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
                filemode='w')
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    mychat = MyChatGPT(CHATGPT_KEY)
    mychat.select_model(CHATGPT_MODEL)
    logger.info("开始聊天")
    c = input('>>:')
    while c != 'quit':
        logger.info("你:{}".format(c))
        r = mychat.chat(c)
        logger.info("GPT:{}".format(r))
        c = input('>>:')
    logger.info("聊天结束")
        


