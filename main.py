import threading
import socket
import json
import re
import requests
import socket_duplex
import plug
import time
import random
import api
import psutil
import platform
import os
import hashlib
from urllib import parse


def get_message():
    """
    获取框架事件线程
    :return:
    """
    while True:
        message = message_socket.accept_message()
        if '}{' in message:
            m = re.findall(r"\{.*?\}", message)
            for i in m:
                plug.main(api.setstatus(i))
                time.sleep(0.01)
            return
        plug.main(api.setstatus(message))
        time.sleep(0.01)


if __name__ == '__main__':
    # 初始化自定义双工socket
    message_socket = socket_duplex.Socket("123456") # 此处传入httpApi上的token
    # 初始化api并传入plug
    api.init(message_socket)
    plug.init(api)
    # 启动事件接收
    t_get_message = threading.Thread(target=get_message)
    t_get_message.setDaemon(True)
    t_get_message.start()
    while True:
        time.sleep(60)

