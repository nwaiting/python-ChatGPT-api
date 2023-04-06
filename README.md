# <p align="center">python-ChatGPT-api</p>

<br>
<p align="center">
    <a href="#"><img src="https://img.shields.io/badge/python-3.7-green.svg"></a>
</p>
<br />

## Documentation

<p> 使用python调用chatgpt的api接口，做成一个自动聊天机器人，可以接入到相应的应用中 </p>


## Install
#### *How you run*

在chattools/config.py中配置key，在 [官网](https://platform.openai.com/account/api-keys) 申请api的key

修改需要使用的模型，在chattools/config.py的CHATGPT_CHAT_MODEL配置聊天的模型名字，在chattools/config.py的CHATGPT_IMAGE_MODEL配置生成图片的模型名字


```python
python chatgpt_main.py -h
可以查看现有的功能，现在有聊天和生产图片功能

python chatgpt_main.py -t chat
进入聊天模式

python chatgpt_main.py -t image
进入生成图片模式

```

## 微信
<img src="img/wx.png" width="249"/>
