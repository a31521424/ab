import threading
import re
import socket_duplex
import plug
import time
import api
import traceback


def get_message():
    """
    获取框架事件线程
    :return:
    """
    while True:
        message = message_socket.accept_message(timeout=60)
        try:
            if message is not None:
                if '}{' in message:
                    m = re.findall(r"\{.*?\}", message)
                    for i in m:
                        info = api.setstatus(i)
                        if info is not None:
                            threading.Thread(target=plug.main, args=(info, )).start()
                        time.sleep(0.01)
                else:
                    info = api.setstatus(message)
                    if info is not None:
                        threading.Thread(target=plug.main, args=(info, )).start()
        except Exception:
            print("接收消息时发生了一个错误")
        time.sleep(0.01)


if __name__ == '__main__':
    try:
        # 初始化自定义双工socket
        message_socket = socket_duplex.Socket("123456")  # 此处传入httpApi上的token
        # 启动事件接收
        t_get_message = threading.Thread(target=get_message)
        t_get_message.setDaemon(True)
        t_get_message.start()
        # 初始化api并传入plug
        time.sleep(0.1)
        api.init(message_socket)
        plug.init(api)
        while True:
            time.sleep(60)
    except Exception as e:
        with open('log.txt', 'a+') as w:
            w.write("时间:%s\n错误:%s \n位置:%s\n" %(time.strftime("%Y-%m-%d %H:%M:%S"), str(e), traceback.format_exc()))
