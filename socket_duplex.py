import socket
import threading
import time
import random
import json
import traceback



class Socket:
    message_box = []  # 消息池
    lock = threading.Lock()
    conn = None
    key = None
    ver_status = False  # 验证状态
    last_time = time.time()  # 上次发送时间

    def __init__(self, key):
        """构造方法
        :param key: 传入插件的密码 httpApi只有密码匹配才能通信
        """
        r_socket = socket.socket()
        r_socket.connect(('127.0.0.1', 8895))
        self.conn = r_socket
        self.key = key
        t1 = threading.Thread(target=self.recv)
        t1.setDaemon(True)
        t1.start()

    def recv(self):
        """ 接收socket消息并添加到消息池
        :return:
        """
        while True:
            message = ""
            try:
                message = self.conn.recv(100 * 1024).decode("gbk")  # 接受10byte数据
            except Exception as e:
                with open('log.txt', 'a+') as w:
                    w.write(
                        "时间:%s\n错误:%s \n位置:%s\n" % (time.strftime("%Y-%m-%d %H:%M:%S"), str(e), traceback.format_exc()))
            if message == "":
                time.sleep(0.01)
                break
            if self.ver_status is False:
                if message == self.key:
                    print("框架与插件对接成功")
                    self.ver_status = True
                else:
                    print("对接密匙错误")
                    break
            else:
                self.message_box.append(message)
            time.sleep(0.01)

    def accept_message(self, id="123456789abcdef", timeout=5):
        t = time.time()
        while True:
            for i in self.message_box:
                i: str
                if '"message_id":"%s"' % id in i:
                    self.message_box.remove(i)
                    if id != "123456789abcdef":
                        return json.loads(i)['return']
                    else:
                        return i
            time.sleep(0.01)
            if t - time.time() > timeout:
                return

    def send_message(self, message):
        with self.lock:
            if time.time() - self.last_time < 0.01:
                time.sleep(0.01)
            self.last_time = time.time()
        message: str
        random_string = ""
        if self.ver_status:
            random_string = str(time.time()) + str(random.randint(1, 99))
            random_string = random_string.replace(".", "")
            message = message[0:1] + '"set_message_id": "%s",' % random_string + message[1:]
            self.conn.send(message.encode("gbk"))
        else:
            print("未与http插件连接")
        return random_string
