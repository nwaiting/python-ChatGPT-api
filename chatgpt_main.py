import requests
import logging
import argparse
from chattools.config import CHATGPT_KEY, CHATGPT_CHAT_MODEL, CHATGPT_IMAGE_MODEL
from chattools.chat import MyChatGPT

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
                filemode='w')
logger = logging.getLogger(__name__)


def chat():
    mychat = MyChatGPT(CHATGPT_KEY)
    mychat.select_model(CHATGPT_CHAT_MODEL)
    logger.info("开始聊天, 输入 quit 退出")
    c = input('>>')
    while c != 'quit':
        r = mychat.chat(c)
        logger.info("gpt:{}".format(r))
        c = input('>>')
    logger.info("聊天结束")


def image():
    mychat = MyChatGPT(CHATGPT_KEY)
    mychat.select_model(CHATGPT_IMAGE_MODEL)
    logger.info("开始生成图片, 输入 quit 退出")
    c = input('>>')
    while c != 'quit':
        r = mychat.create_image(c)
        logger.info("images:{}".format(r))
        c = input('>>')
    logger.info("生成图片结束结束")


def parse_arg():
    parser = argparse.ArgumentParser(description='输入类型 chat/image (聊天或者生成图片)')
    parser.add_argument('-t', '--type', type=str, help='传入类型')
    _args = parser.parse_args()
    return _args


if __name__ == '__main__':
    args = parse_arg()
    if args.type == 'chat':
        chat()
    elif args.type == 'image':
        image()
    logger.error("end process")
    




