# -*- coding: utf-8 -*-
# filename: test.py

import werobot
from werobot.replies import ImageReply,TextReply
import hashlib
from create import *


# 输入微信公众平台请求凭证
robot = werobot.WeRoBot(token='')         # 写入服务器配置填写的 Token
robot.config["APP_ID"] = ""               # 写入开发者ID
robot.config["ENCODING_AES_KEY"] = ""     # 写入服务器配置填写的 EncodingAESKey
robot.config["APP_SECRET"]=""

explain="公众号回复 自己战队名称, 即可生成专属海报及报名二维码(战队名不要带emoji如: 🐎)"

client = robot.client
token = client.grant_token()
print(token)

def get_img_media_id(img_file_name):
  """
  * 上传临时素菜
  * 1、临时素材media_id是可复用的。
  * 2、媒体文件在微信后台保存时间为3天，即3天后media_id失效。
  * 3、上传临时素材的格式、大小限制与公众平台官网一致。
  """
  # media_json = client.upload_media("image", open(img_file_name, "rb"))

  media_json = client.upload_permanent_media("image", open(img_file_name, "rb")) ##永久素材
  media_id = media_json['media_id']

  return media_id

#对图像进行md5加密
def md5(text):
    return hashlib.md5(text.encode()).hexdigest()

def handlermessage(content,id):
    if content=="报名":
        return ImageReply(message=id,media_id="yfLP0QY2faoF0Tb8ClFH6OA8uo-Ga_pinW7xJfG4mQXiw6yp1jTCv8vmxf7KnEt9")
    elif content =="flag":
        return "flag{we1come_to_HuhstCtf2022}"
    else:
        with open("./teamnaem.txt","a+") as f:
            f.write(content+"\n")
        savepath="./images/"+md5(content)+".png"
        create(content.replace(" ",""),savepath)
        media_id=get_img_media_id(savepath)
        return ImageReply(message=id,media_id=media_id)




@robot.subscribe
def subscribe(message):

    return "欢迎关注HuhstSec实验室, 公众号回复报名 获取报名方式!"

# 建立一个消息处理装饰器，当 handler 无论收到何种信息时都运行 hello 函数
@robot.text
def hello(message):
    content=message.content
    return handlermessage(content,message)


# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = '80'
robot.run()
