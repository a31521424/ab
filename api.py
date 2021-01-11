import json
import socket_duplex

message_socket: socket_duplex.Socket = None
info = None


def init(socket):
    global message_socket
    if message_socket is None:
        message_socket = socket


def reply(msg, bubble_id=-1):
    global info
    if info is not None:
        sendmsg(info['qq_id'], info['type'], info['source'], info['to_obj'], msg, bubble_id)


def setstatus(content):
    global info
    try:
        info = json.loads(content)
    except Exception as e:
        print(e)
        print(content)
    return info


def sendmsg(qq_id, type, to_group, to_obj, msg, bubble_id):
    """ 发送普通文本消息
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param type: 信息类型 整数型 0在线临时会话 1好友 2群 3讨论组 4群临时会话 5讨论组临时会话 7好友验证回复会话 8群匿名消息 ）
	:param to_group: 收信对象群_讨论组 文本型 发送群匿名消息、群信息、讨论组、群或讨论组临时会话信息时填写，如发送对象为好友或信息类型是0时可空
	:param to_obj: 收信QQ 文本型 收信对象QQ
	:param msg: 内容 文本型 信息内容
	:param bubble_id: 气泡ID 整数型 -1为随机气泡
    :return:
    """
    global message_socket
    order = {'func': "sendmsg", 'qq_id': qq_id, 'type': type, 'to_group': to_group, 'to_obj': to_obj, 'msg': msg,
             'bubble_id': bubble_id}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def sendxml(qq_id, send_type, type, to_group, to_obj, obj_msg, msg_sub_type):
    """ 发送XML消息
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param send_type: 发送方式 整数型 1普通 2匿名（匿名需要群开启）
	:param type: 信息类型 整数型 0在线临时会话 1好友 2群 3讨论组 4群临时会话 5讨论组临时会话 7好友验证回复会话
	:param to_group: 收信对象所属群_讨论组 文本型 发送群信息、讨论组、群或讨论组临时会话信息时填写，如发送对象为好友或信息类型是0时可空
	:param to_obj: 收信对象QQ 文本型 收信对象QQ
	:param obj_msg: ObjectMsg 文本型 XML代码或Json代码
	:param msg_sub_type: 结构子类型 整数型 0基本 2点歌
    :return:
    """
    global message_socket
    order = {'func': "sendxml", 'qq_id': qq_id, 'send_type': send_type, 'type': type, 'to_group': to_group,
             'to_obj': to_obj, 'obj_msg': obj_msg, 'msg_sub_type': msg_sub_type}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def sendjson(qq_id, send_type, type, to_group, to_obj, obj_msg):
    """ 发送JSON结构消息
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param send_type: 发送方式 整数型 1普通 2匿名（匿名需要群开启）
	:param type: 信息类型 整数型 0在线临时会话 1好友 2群 3讨论组 4群临时会话 5讨论组临时会话 7好友验证回复会话
	:param to_group: 收信对象所属群_讨论组 文本型 发送群信息、讨论组、群或讨论组临时会话信息时填，如发送对象为好友或信息类型是0时可空
	:param to_obj: 收信对象QQ 文本型 收信对象QQ
	:param obj_msg: Json结构 文本型 Json结构内容
    :return:
    """
    global message_socket
    order = {'func': "sendjson", 'qq_id': qq_id, 'send_type': send_type, 'type': type, 'to_group': to_group,
             'to_obj': to_obj, 'obj_msg': obj_msg}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def upvote(qq_id, be_like_obj):
    """ 调用一次点一下，成功返回空，失败返回理由如：每天最多给他点十个赞哦，调用此Api时应注意频率，每人每日可被赞10次，每日每Q最多可赞50人
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param be_like_obj: 被赞QQ 文本型 填写被赞人QQ
    :return: 文本型
    """
    global message_socket
    order = {'func': "upvote", 'qq_id': qq_id, 'be_like_obj': be_like_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getcookies(qq_id):
    """ 取得机器人网页操作用的Cookies
	:param qq_id: 响应QQ 文本型 机器人QQ
    :return: 文本型
    """
    global message_socket
    order = {'func': "getcookies", 'qq_id': qq_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getblogpskey(qq_id):
    """ 取得腾讯微博页面操作用参数P_skey
	:param qq_id: 响应QQ 文本型 机器人QQ
    :return: 文本型
    """
    global message_socket
    order = {'func': "getblogpskey", 'qq_id': qq_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getzonepskey(qq_id):
    """ 取得QQ空间页面操作用参数P_skey
	:param qq_id: 响应QQ 文本型 机器人QQ
    :return: 文本型
    """
    global message_socket
    order = {'func': "getzonepskey", 'qq_id': qq_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getgrouppskey(qq_id):
    """ 取得QQ群页面操作用参数P_skey
	:param qq_id: 响应QQ 文本型 机器人QQ
    :return: 文本型
    """
    global message_socket
    order = {'func': "getgrouppskey", 'qq_id': qq_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getclassroompskey(qq_id):
    """ 取得腾讯课堂页面操作用参数P_skey
	:param qq_id: 响应QQ 文本型 机器人QQ
    :return: 文本型
    """
    global message_socket
    order = {'func': "getclassroompskey", 'qq_id': qq_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getbkn(qq_id):
    """ 取得机器人网页操作用参数Bkn或G_tk
	:param qq_id: 响应QQ 文本型 机器人QQ
    :return: 文本型
    """
    global message_socket
    order = {'func': "getbkn", 'qq_id': qq_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getbkn32(qq_id):
    """ 取得机器人网页操作用参数长Bkn或长G_tk
	:param qq_id: 响应QQ 文本型 机器人QQ
    :return: 文本型
    """
    global message_socket
    order = {'func': "getbkn32", 'qq_id': qq_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getlongldw(qq_id):
    """ 取得机器人网页操作用参数长Ldw
	:param qq_id: 响应QQ 文本型 机器人QQ
    :return: 文本型
    """
    global message_socket
    order = {'func': "getlongldw", 'qq_id': qq_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getclientkey(qq_id):
    """ 取得机器人网页操作用的Clientkey
	:param qq_id: 响应QQ 文本型 机器人QQ
    :return: 文本型
    """
    global message_socket
    order = {'func': "getclientkey", 'qq_id': qq_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getlongclientkey(qq_id):
    """ 取得机器人网页操作用的长Clientkey
	:param qq_id: 响应QQ 文本型 机器人QQ
    :return: 文本型
    """
    global message_socket
    order = {'func': "getlongclientkey", 'qq_id': qq_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def admininvitegroup(qq_id, to_obj, to_group):
    """ 管理员邀请对象入群，频率过快会失败
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_obj: 对象QQ 文本型 被邀请人QQ号码（多个号码使用 #换行符 分割）
	:param to_group: 群号 文本型 被邀请加入的群号
    :return:
    """
    global message_socket
    order = {'func': "admininvitegroup", 'qq_id': qq_id, 'to_obj': to_obj, 'to_group': to_group}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def noadmininvitegroup(qq_id, to_obj, to_group):
    """ 非管理员邀请对象入群，频率过快会失败
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_obj: 对象QQ 文本型 被邀请人QQ号码（多个号码使用 #换行符 分割）
	:param to_group: 群号 文本型 被邀请加入的群号
    :return:
    """
    global message_socket
    order = {'func': "noadmininvitegroup", 'qq_id': qq_id, 'to_obj': to_obj, 'to_group': to_group}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def getnick(qq_id, to_obj):
    """ 取对象昵称
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_obj: 对象QQ 文本型 欲取得的QQ的号码
    :return: 文本型
    """
    global message_socket
    order = {'func': "getnick", 'qq_id': qq_id, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getgroupcard(qq_id, to_group, to_obj):
    """ 取对象群名片
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_group: 群号 文本型 群号
	:param to_obj: 对象QQ 文本型 欲取得群名片的QQ号码
    :return: 文本型
    """
    global message_socket
    order = {'func': "getgroupcard", 'qq_id': qq_id, 'to_group': to_group, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getobjlevel(qq_id, to_obj):
    """ 取对象QQ等级 成功返回等级  失败返回-1
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_obj: 对象QQ 文本型 欲取得的QQ的号码
    :return: 整数型
    """
    global message_socket
    order = {'func': "getobjlevel", 'qq_id': qq_id, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getfriendlist(qq_id):
    """ 取得好友列表，返回获取到的原始JSON格式信息，需自行解析
	:param qq_id: 响应QQ 文本型 机器人QQ
    :return: 文本型
    """
    global message_socket
    order = {'func': "getfriendlist", 'qq_id': qq_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getfriendlist_b(qq_id):
    """ 取得好友列表，返回内容#换行符分割
	:param qq_id: 响应QQ 文本型 机器人QQ
    :return: 文本型
    """
    global message_socket
    order = {'func': "getfriendlist_b", 'qq_id': qq_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getgroupadmin(qq_id, to_group):
    """ 取得群管理，返回获取到的原始JSON格式信息，需自行解析
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_group: 群号 文本型 欲取管理员列表群号
    :return: 文本型
    """
    global message_socket
    order = {'func': "getgroupadmin", 'qq_id': qq_id, 'to_group': to_group}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getgrouplist_a(qq_id):
    """ 取得群列表，#换行符分割 不受最高获取500群限制（如需获取群名称请对应调用 Api_GetGroupName 理论群名获取不会频繁）
	:param qq_id: 响应QQ 文本型 机器人QQ
    :return: 文本型
    """
    global message_socket
    order = {'func': "getgrouplist_a", 'qq_id': qq_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getgrouplist(qq_id):
    """ 取得群列表，返回获取到的原始JSON格式信息，需自行解析
	:param qq_id: 响应QQ 文本型 机器人QQ
    :return: 文本型
    """
    global message_socket
    order = {'func': "getgrouplist", 'qq_id': qq_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getgrouplist_b(qq_id):
    """ 取得群列表，返回获取到的原始JSON格式信息，需自行解析
	:param qq_id: 响应QQ 文本型 机器人QQ
    :return: 文本型
    """
    global message_socket
    order = {'func': "getgrouplist_b", 'qq_id': qq_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getgroupmemberlist(qq_id, to_group):
    """ 取得群成员列表，返回获取到的原始JSON格式信息，需自行解析（有群员昵称）
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_group: 群号 文本型 欲取群成员列表群号
    :return: 文本型
    """
    global message_socket
    order = {'func': "getgroupmemberlist", 'qq_id': qq_id, 'to_group': to_group}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getgroupmemberlist_b(qq_id, to_group):
    """ 取得群成员列表，返回QQ号和身份Json格式信息 失败返回空（无群员昵称）
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_group: 群号 文本型 欲取群成员列表群号
    :return: 文本型
    """
    global message_socket
    order = {'func': "getgroupmemberlist_b", 'qq_id': qq_id, 'to_group': to_group}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getgroupmemberlist_c(qq_id, to_group):
    """ 取得群成员列表，返回获取到的原始JSON格式信息，需自行解析（有群员昵称）
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_group: 群号 文本型 欲取群成员列表群号
    :return: 文本型
    """
    global message_socket
    order = {'func': "getgroupmemberlist_c", 'qq_id': qq_id, 'to_group': to_group}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def isshutup(qq_id, to_group, to_obj):
    """ 查询对象或自己是否被禁言  禁言返回真 失败或未禁言返回假
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_group: 群号 文本型 欲查询的群号
	:param to_obj: 对象QQ 文本型 需要查询的对象QQ
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "isshutup", 'qq_id': qq_id, 'to_group': to_group, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def shutup(qq_id, to_group, to_obj, time):
    """ 群内禁言某人
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_group: 群号 文本型 欲操作的群号
	:param to_obj: 对象QQ 文本型 欲禁言的对象，如留空且机器人QQ为管理员，将设置该群为全群禁言
	:param time: 时间 整数型 0为解除禁言 （禁言单位为秒），如为全群禁言，参数为非0，解除全群禁言为0
    :return:
    """
    global message_socket
    order = {'func': "shutup", 'qq_id': qq_id, 'to_group': to_group, 'to_obj': to_obj, 'time': time}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def joingroup(qq_id, to_group, reason):
    """ 申请加群
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_group: 群号 文本型 欲申请加入的群号
	:param reason: 理由 文本型 附加理由，可留空（需回答正确问题时，请填写问题答案）
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "joingroup", 'qq_id': qq_id, 'to_group': to_group, 'reason': reason}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def quitgroup(qq_id, to_group):
    """ 退群
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_group: 群号 文本型 欲退出的群号
    :return:
    """
    global message_socket
    order = {'func': "quitgroup", 'qq_id': qq_id, 'to_group': to_group}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def uploadpic(qq_id, up_type, ref_obj, pic_url):
    """ 上传图片（通过读入字节集方式），可使用网页链接或本地读入，成功返回该图片GUID，失败返回空
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param up_type: 上传类型 整数型 1好友、临时会话  2群、讨论组 Ps：好友临时会话用类型 1，群讨论组用类型 2；当填写错误时，图片GUID发送不会成功
	:param ref_obj: 参考对象 文本型 上传该图片所属的群号或QQ
	:param pic_url: 图片地址 文本型 图片地址 网络或本地位置
    :return: 文本型
    """
    global message_socket
    order = {'func': "uploadpic", 'qq_id': qq_id, 'up_type': up_type, 'ref_obj': ref_obj, 'pic_url': pic_url}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getpiclink(qq_id, pic_type, ref_obj, guid):
    """ 根据图片GUID取得图片下载连接
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param pic_type: 图片类型 整数型 1 群 讨论组  2临时会话和好友
	:param ref_obj: 参考对象 文本型 图片所属对应的群号和好友QQ（可随意乱填写）
	:param guid: 图片GUID 文本型 例如[IR:pic={xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}.jpg]
    :return: 文本型
    """
    global message_socket
    order = {'func': "getpiclink", 'qq_id': qq_id, 'pic_type': pic_type, 'ref_obj': ref_obj, 'guid': guid}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def outputlog(msg):
    """ 向ER框架日志窗口发送一条本插件的日志，可用于调试输出需要的内容，或定位插件错误与运行状态
	:param msg: 内容 文本型 任意想输出的文本格式信息
    :return:
    """
    global message_socket
    order = {'func': "outputlog", 'msg': msg}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def teaencrypt(en_data, session_key):
    """ Tea加密
	:param en_data: 需加密内容 文本型 需加密的内容
	:param session_key: 会话KEY 文本型 这里填Api_SessionKey
    :return: 文本型
    """
    global message_socket
    order = {'func': "teaencrypt", 'en_data': en_data, 'session_key': session_key}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def teadecrypt(de_data, session_key):
    """ 腾讯Tea解密
	:param de_data: 需解密内容 文本型 需解密的内容
	:param session_key: 会话KEY 文本型 这里填Api_SessionKey
    :return: 文本型
    """
    global message_socket
    order = {'func': "teadecrypt", 'de_data': de_data, 'session_key': session_key}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def sessionkey(qq_id):
    """ 获取会话SessionKey密钥
	:param qq_id: 响应QQ 文本型 欲获取的QQ
    :return: 文本型
    """
    global message_socket
    order = {'func': "sessionkey", 'qq_id': qq_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def gntransgid(to_group):
    """ 群号转群ID
	:param to_group: 群号  文本型
    :return: 文本型
    """
    global message_socket
    order = {'func': "gntransgid", 'to_group': to_group}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def gidtransgn(group_id):
    """ 群ID转群号
	:param group_id: 群ID  文本型
    :return: 文本型
    """
    global message_socket
    order = {'func': "gidtransgn", 'group_id': group_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def pbgroupnotic(qq_id, to_group, title, msg):
    """ 发布群公告（成功返回真，失败返回假），调用此API应保证响应QQ为管理员
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_group: 群号 文本型 欲发布公告的群号
	:param title: 标题 文本型 公告标题
	:param msg: 内容 文本型 公告内容
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "pbgroupnotic", 'qq_id': qq_id, 'to_group': to_group, 'title': title, 'msg': msg}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getnotice(qq_id, to_group):
    """ 取群公告，返回该群最新公告
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_group: 群号 文本型 欲取得公告的群号
    :return: 文本型
    """
    global message_socket
    order = {'func': "getnotice", 'qq_id': qq_id, 'to_group': to_group}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def shakewindow(qq_id, to_obj):
    """ 向好友发起窗口抖动，调用此Api腾讯会限制频率
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_obj: 接收QQ 文本型 接收抖动消息的QQ
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "shakewindow", 'qq_id': qq_id, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def handlegroupevent(qq_id, request_type, to_obj, to_group, seq, dispose_type, msg):
    """ 处理群验证事件
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param request_type: 请求类型 整数型 213请求入群  214我被邀请加入某群  215某人被邀请加入群  101某人请求添加好友
	:param to_obj: 对象QQ 文本型 申请入群 被邀请人 请求添加好友人的QQ （当请求类型为214时这里为邀请人QQ）
	:param to_group: 群号 文本型 收到请求群号（好友添加时这里请为空）
	:param seq: seq 文本型 需要处理事件的seq （好友事件留空）
	:param dispose_type: 处理方式 整数型 10同意 20拒绝 30忽略
	:param msg: 附加信息 文本型 拒绝入群，拒绝添加好友 附加信息
    :return:
    """
    global message_socket
    order = {'func': "handlegroupevent", 'qq_id': qq_id, 'request_type': request_type, 'to_obj': to_obj,
             'to_group': to_group, 'seq': seq, 'dispose_type': dispose_type, 'msg': msg}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def setanon(qq_id, to_group, switch):
    """ 开关群匿名消息发送功能    成功返回真  失败返回假
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_group: 群号 文本型 需开关群匿名功能群号
	:param switch: 开关 逻辑型 真开    假关
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "setanon", 'qq_id': qq_id, 'to_group': to_group, 'switch': switch}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def setgroupcard(qq_id, to_group, to_obj, nick):
    """ 修改对象群名片 成功返回真 失败返回假
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_group: 群号 文本型 对象所处群号
	:param to_obj: 对象QQ 文本型 被修改名片人QQ
	:param nick: 名片 文本型 需要修改的名片
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "setgroupcard", 'qq_id': qq_id, 'to_group': to_group, 'to_obj': to_obj, 'nick': nick}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def quitdisgroup(qq_id, discussion_id):
    """ 退出讨论组
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param discussion_id: 讨论组ID 文本型 需退出的讨论组ID
    :return:
    """
    global message_socket
    order = {'func': "quitdisgroup", 'qq_id': qq_id, 'discussion_id': discussion_id}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def createdisgroup(qq_id, discussion_name):
    """ 创建一个讨论组 成功返回讨论组ID 失败返回空
	:param qq_id: 响应QQ 文本型 机器人
	:param discussion_name: 讨论组名称 文本型 建立的讨论组名称
    :return: 文本型
    """
    global message_socket
    order = {'func': "createdisgroup", 'qq_id': qq_id, 'discussion_name': discussion_name}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def kickdisgroupmbr(qq_id, discussion_id, to_obj):
    """ 将对象移除讨论组 成功返回空 失败返回理由
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param discussion_id: 讨论组ID 文本型 需执行的讨论组ID
	:param to_obj: 对象QQ 文本型 被执行对象
    :return: 文本型
    """
    global message_socket
    order = {'func': "kickdisgroupmbr", 'qq_id': qq_id, 'discussion_id': discussion_id, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def invitedisgroup(qq_id, discussion_id, to_obj):
    """ 邀请对象加入讨论组 成功返回空 失败返回理由
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param discussion_id: 讨论组ID 文本型 需执行的讨论组ID
	:param to_obj: 邀请对象QQ 文本型 被邀请对象QQ 多个用  #换行符 分割
    :return: 文本型
    """
    global message_socket
    order = {'func': "invitedisgroup", 'qq_id': qq_id, 'discussion_id': discussion_id, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getdisgrouplist(qq_id):
    """ 取出讨论组列表 （返回格式为 换行符分割开的）
	:param qq_id: 响应QQ 文本型 机器人QQ
    :return: 文本型
    """
    global message_socket
    order = {'func': "getdisgrouplist", 'qq_id': qq_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getdisgroupmemberlist(qq_id, discussion_id):
    """ 取出讨论组成员列表 （返回格式为 换行符分割开的）
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param discussion_id: 讨论组ID 文本型 需获取的讨论组ID
    :return: 文本型
    """
    global message_socket
    order = {'func': "getdisgroupmemberlist", 'qq_id': qq_id, 'discussion_id': discussion_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def setdisgroupname(qq_id, discussion_id, discussion_name):
    """ 修改讨论组名称
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param discussion_id: 讨论组ID 文本型 需执行的讨论组ID
	:param discussion_name: 讨论组名称 文本型 需修改的名称
    :return:
    """
    global message_socket
    order = {'func': "setdisgroupname", 'qq_id': qq_id, 'discussion_id': discussion_id,
             'discussion_name': discussion_name}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def kickgroupmbr(qq_id, to_group, to_obj, dispose_type):
    """ 将对象移除群
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_group: 群号 文本型 被执行群号
	:param to_obj: 对象QQ 文本型 被执行对象
	:param dispose_type: 不再接收加群请求 逻辑型 真为不再接收，假为接收
    :return:
    """
    global message_socket
    order = {'func': "kickgroupmbr", 'qq_id': qq_id, 'to_group': to_group, 'to_obj': to_obj,
             'dispose_type': dispose_type}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def getobjvote(qq_id, to_obj):
    """ 获取对象当前赞数量 失败返回-1   成功返回赞数 （获取频繁会出现失败现象，请自行写判断处理失败问题）
	:param qq_id: 响应QQ  文本型
	:param to_obj: 对象QQ  文本型
    :return: 长整数型
    """
    global message_socket
    order = {'func': "getobjvote", 'qq_id': qq_id, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def uploadvoice(qq_id, up_type, to_group, voi_url):
    """ 上传QQ语音，成功返回语音GUID  失败返回空
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param up_type: 上传类型 整数型 2、QQ群 讨论组
	:param to_group: 接收群号 文本型 需上传的群号
	:param voi_url: 语音地址 文本型 语音网络或本地位置（AMR Silk编码）
    :return: 文本型
    """
    global message_socket
    order = {'func': "uploadvoice", 'qq_id': qq_id, 'up_type': up_type, 'to_group': to_group, 'voi_url': voi_url}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getvoilink(qq_id, guid):
    """ 通过语音GUID获取下载连接 失败返回空
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param guid: 语音GUID 文本型 [IR:Voi={xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx}.amr]
    :return: 文本型
    """
    global message_socket
    order = {'func': "getvoilink", 'qq_id': qq_id, 'guid': guid}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def gettimestamp():
    """ 获取当前框架内部时间戳

    :return: 长整数型
    """
    global message_socket
    order = {'func': "gettimestamp"}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def sendpack(qq_id, package):
    """ 向腾讯发送原始封包（成功返回腾讯返回的包 失败返回空）
	:param qq_id: 响应QQ  文本型
	:param package: 封包 文本型 封包内容
    :return: 文本型
    """
    global message_socket
    order = {'func': "sendpack", 'qq_id': qq_id, 'package': package}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getobjinfo(qq_id, to_obj):
    """ 获取对象资料 此方式为http，调用时应自行注意控制频率（成功返回JSON格式自行解析）
	:param qq_id: 响应QQ  文本型
	:param to_obj: 对象QQ  文本型
    :return: 文本型
    """
    global message_socket
    order = {'func': "getobjinfo", 'qq_id': qq_id, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getgender(qq_id, to_obj):
    """ 取对象性别 1男 2女  未知或失败返回-1
	:param qq_id: 响应QQ  文本型
	:param to_obj: 对象QQ  文本型
    :return: 整数型
    """
    global message_socket
    order = {'func': "getgender", 'qq_id': qq_id, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getqqage(qq_id, to_obj):
    """ 取Q龄 成功返回Q龄 失败返回-1
	:param qq_id: 响应QQ  文本型
	:param to_obj: 对象QQ  文本型
    :return: 整数型
    """
    global message_socket
    order = {'func': "getqqage", 'qq_id': qq_id, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getage(qq_id, to_obj):
    """ 取年龄 成功返回年龄 失败返回-1
	:param qq_id: 响应QQ  文本型
	:param to_obj: 对象QQ  文本型
    :return: 整数型
    """
    global message_socket
    order = {'func': "getage", 'qq_id': qq_id, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getperexp(qq_id, to_obj):
    """ 取个人说明
	:param qq_id: 响应QQ  文本型
	:param to_obj: 对象QQ  文本型
    :return: 文本型
    """
    global message_socket
    order = {'func': "getperexp", 'qq_id': qq_id, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getsign(qq_id, to_obj):
    """ 取个人签名
	:param qq_id: 响应QQ  文本型
	:param to_obj: 对象QQ  文本型
    :return: 文本型
    """
    global message_socket
    order = {'func': "getsign", 'qq_id': qq_id, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getemail(qq_id, to_obj):
    """ 取邮箱，获取对象QQ资料内邮箱栏为邮箱时返回
	:param qq_id: 响应QQ  文本型
	:param to_obj: 对象QQ  文本型
    :return: 文本型
    """
    global message_socket
    order = {'func': "getemail", 'qq_id': qq_id, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getgroupname(qq_id, to_group):
    """ 取QQ群名
	:param qq_id: 响应QQ  文本型
	:param to_group: 群号  文本型
    :return: 文本型
    """
    global message_socket
    order = {'func': "getgroupname", 'qq_id': qq_id, 'to_group': to_group}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getver():
    """ 取框架版本号

    :return: 文本型
    """
    global message_socket
    order = {'func': "getver"}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getqqlist():
    """ 取框架所有QQ号 换行符分割

    :return: 文本型
    """
    global message_socket
    order = {'func': "getqqlist"}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getonlinelist():
    """ 取框架在线QQ号 换行符分割

    :return: 文本型
    """
    global message_socket
    order = {'func': "getonlinelist"}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getofflinelist():
    """ 取框架离线QQ号 （Pro版可用）换行符分割

    :return: 文本型
    """
    global message_socket
    order = {'func': "getofflinelist"}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def addqq(qq_id, key_word, auto_login):
    """ 向框架帐号列表增加一个登录QQ 成功失败均返回理由（Pro版可用）
	:param qq_id: 帐号  文本型
	:param key_word: 密码  文本型
	:param auto_login: 自动登录 逻辑型 真 为自动登录
    :return: 文本型
    """
    global message_socket
    order = {'func': "addqq", 'qq_id': qq_id, 'key_word': key_word, 'auto_login': auto_login}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def delqq(qq_id):
    """ 删除框架帐号列表内指定QQ，不可在执行登录过程中删除QQ否则有几率引起错误（Pro版可用）
	:param qq_id: QQ号  文本型
    :return: 文本型
    """
    global message_socket
    order = {'func': "delqq", 'qq_id': qq_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def loginqq(qq_id):
    """ 登录指定QQ，应确保QQ号码在列表中已存在
	:param qq_id: 登录QQ  文本型
    :return:
    """
    global message_socket
    order = {'func': "loginqq", 'qq_id': qq_id}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def offlineqq(qq_id):
    """ 令指定QQ下线，应确保QQ号码已在列表中且在线
	:param qq_id: 响应QQ  文本型
    :return:
    """
    global message_socket
    order = {'func': "offlineqq", 'qq_id': qq_id}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def iffriend(qq_id, to_obj):
    """ 是否QQ好友 好友返回真 非好友或获取失败返回假
	:param qq_id: 响应QQ  文本型
	:param to_obj: 对象QQ  文本型
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "iffriend", 'qq_id': qq_id, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def setrinf(qq_id, type, msg):
    """ 修改机器人在线状态 昵称 个性签名 性别
	:param qq_id: 响应QQ  文本型
	:param type: 类型 整数型 1、我在线上 2、Q我吧 3、离开 4、忙碌 5、请勿打扰 6、隐身 7、修改昵称 8、修改个性签名 9、修改性别
	:param msg: 修改内容 文本型 类型为7和8时填写修改内容  类型9时“1”为男 “2”为女      其他填“”
    :return:
    """
    global message_socket
    order = {'func': "setrinf", 'qq_id': qq_id, 'type': type, 'msg': msg}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def getrinf(qq_id):
    """ 获取机器人状态信息，成功返回：昵称、帐号、在线状态、速度、收信、发信、在线时间，失败返回空
	:param qq_id: 响应QQ  文本型
    :return: 文本型
    """
    global message_socket
    order = {'func': "getrinf", 'qq_id': qq_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def delfriend(qq_id, to_obj):
    """ 删除好友 成功返回真 失败返回假
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_obj: 对象QQ 文本型 被删除对象
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "delfriend", 'qq_id': qq_id, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def addbklist(qq_id, to_obj):
    """ 将好友拉入黑名单  成功返回真 失败返回假
	:param qq_id: 响应QQ  文本型
	:param to_obj: 对象QQ  文本型
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "addbklist", 'qq_id': qq_id, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def delbklist(qq_id, to_obj):
    """ 解除好友黑名单
	:param qq_id: 响应QQ  文本型
	:param to_obj: 对象QQ  文本型
    :return:
    """
    global message_socket
    order = {'func': "delbklist", 'qq_id': qq_id, 'to_obj': to_obj}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def setshieldedgroup(qq_id, to_group, type):
    """ 屏蔽或接收某群消息
	:param qq_id: 响应QQ  文本型
	:param to_group: 群号  文本型
	:param type: 类型 逻辑型 真 为屏蔽接收  假为接收并提醒
    :return:
    """
    global message_socket
    order = {'func': "setshieldedgroup", 'qq_id': qq_id, 'to_group': to_group, 'type': type}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def sendvoice(qq_id, to_obj, voi_url):
    """ 好友语音上传并发送 （成功返回真 失败返回假）
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_obj: 接收QQ 文本型 接收语音人QQ
	:param voi_url: 语音地址 文本型 语音网络或本地地址（AMR Silk编码）
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "sendvoice", 'qq_id': qq_id, 'to_obj': to_obj, 'voi_url': voi_url}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def setadmin(qq_id, to_group, to_obj, dispose_type):
    """ 设置或取消群管理员   成功返回空  失败返回理由
	:param qq_id: 响应QQ  文本型
	:param to_group: 群号  文本型
	:param to_obj: 对象QQ  文本型
	:param dispose_type: 操作方式 逻辑型 真 为设置管理  假为取消管理
    :return: 文本型
    """
    global message_socket
    order = {'func': "setadmin", 'qq_id': qq_id, 'to_group': to_group, 'to_obj': to_obj, 'dispose_type': dispose_type}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def pbhomework(qq_id, to_group, job_name, title, msg):
    """ QQ群作业发布
	:param qq_id: 响应QQ  文本型
	:param to_group: 群号  文本型
	:param job_name: 作业名  文本型
	:param title: 标题  文本型
	:param msg: 内容  文本型
    :return:
    """
    global message_socket
    order = {'func': "pbhomework", 'qq_id': qq_id, 'to_group': to_group, 'job_name': job_name, 'title': title,
             'msg': msg}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def getlog():
    """ 取框架日志

    :return: 文本型
    """
    global message_socket
    order = {'func': "getlog"}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def isenable():
    """ 取得插件自身启用状态，启用真 禁用假

    :return: 逻辑型
    """
    global message_socket
    order = {'func': "isenable"}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def disabledplugin():
    """ 请求禁用插件自身

    :return:
    """
    global message_socket
    order = {'func': "disabledplugin"}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def withdrawmsg(qq_id, to_group, msg_serial, msg_id):
    """ 消息撤回（成功返回空，失败返回腾讯给出的理由）（Pro版可用）
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_group: 群号 文本型 需撤回消息群号
	:param msg_serial: 消息序号 文本型 需撤回消息序号
	:param msg_id: 消息ID 文本型 需撤回消息ID
    :return: 文本型
    """
    global message_socket
    order = {'func': "withdrawmsg", 'qq_id': qq_id, 'to_group': to_group, 'msg_serial': msg_serial, 'msg_id': msg_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def beinput(qq_id, to_obj):
    """ 置正在输入状态（发送消息后会打断状态）
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_obj: 对象QQ 文本型 置正在输入状态接收对象
    :return:
    """
    global message_socket
    order = {'func': "beinput", 'qq_id': qq_id, 'to_obj': to_obj}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def getqqaddmode(qq_id, to_obj):
    """ 取对象好友添加验证方式 （00 允许任何人  01 需要身份验证  03 需回答正确问题  04 需回答问题  99 已经是好友） （Pro版可用）
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_obj: 对象QQ 文本型 需获取对象QQ
    :return: 文本型
    """
    global message_socket
    order = {'func': "getqqaddmode", 'qq_id': qq_id, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def isonline(qq_id, to_obj):
    """ 查询对象是否在线
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_obj: 对象QQ 文本型 需获取对象QQ
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "isonline", 'qq_id': qq_id, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getonlinestate(qq_id, to_obj):
    """ 查询对象在线状态   返回 1、在线 2、Q我 3、离开 4、忙碌 5、勿扰 6、隐身或离线（Pro可用）
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_obj: 对象QQ 文本型 需获取对象QQ
    :return: 整数型
    """
    global message_socket
    order = {'func': "getonlinestate", 'qq_id': qq_id, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getgroupmembernum(qq_id, to_group):
    """ 查询对象群当前人数和上限人数
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_group: 群号 文本型 需查询的群号
    :return: 文本型
    """
    global message_socket
    order = {'func': "getgroupmembernum", 'qq_id': qq_id, 'to_group': to_group}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getwpa(qq_id, to_obj):
    """ 查询对方是否允许在线状态临时会话消息（非讨论组和群临时）（Pro版可用）
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_obj: 对象QQ 文本型 需查询的对象QQ
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "getwpa", 'qq_id': qq_id, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getgroupaddmode(qq_id, to_group):
    """ 查询对象群验证方式 1允许任何人 2需要验证消息 3不允许任何人加群 4需要正确回答问题 5需要回答问题并由管理员审核 6付费群 -1群号不存在（获取失败返回空）Pro版可用
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_group: 群号 文本型 需查询的群号
    :return: 文本型
    """
    global message_socket
    order = {'func': "getgroupaddmode", 'qq_id': qq_id, 'to_group': to_group}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getgrouplv(qq_id, to_group):
    """ 查询QQ群等级，成功返回等级（失败返回-1）Pro版可用
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_group: 群号 文本型 需查询的群号
    :return: 整数型
    """
    global message_socket
    order = {'func': "getgrouplv", 'qq_id': qq_id, 'to_group': to_group}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def setfriendsremark(qq_id, to_obj, note_name):
    """ 修改好友备注姓名
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_obj: 对象QQ 文本型 需获取对象好友QQ
	:param note_name: 备注 文本型 需要修改的备注姓名
    :return:
    """
    global message_socket
    order = {'func': "setfriendsremark", 'qq_id': qq_id, 'to_obj': to_obj, 'note_name': note_name}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def getfriendsremark(qq_id, to_obj):
    """ 取好友备注姓名（成功返回备注，失败或无备注返回空）Pro可用
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_obj: 对象QQ 文本型 需获取对象好友QQ
    :return: 文本型
    """
    global message_socket
    order = {'func': "getfriendsremark", 'qq_id': qq_id, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def signin(qq_id, to_group, local, content):
    """ QQ群签到（成功返回真 失败返回假）
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_group: 群号 文本型 QQ群号
	:param local: 地名 文本型 签到地名（Pro可自定义）
	:param content: 想说的话 文本型 想发表的内容
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "signin", 'qq_id': qq_id, 'to_group': to_group, 'local': local, 'content': content}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def takegift(qq_id):
    """ 抽取群礼物（返回结果Json，需群聊等级LV5后）Pro可用
	:param qq_id: 响应QQ 文本型 机器人QQ
    :return: 文本型
    """
    global message_socket
    order = {'func': "takegift", 'qq_id': qq_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def checkgift(qq_id):
    """ 查询我的群礼物（返回Json格式）Pro可用
	:param qq_id: 响应QQ 文本型 机器人QQ
    :return: 文本型
    """
    global message_socket
    order = {'func': "checkgift", 'qq_id': qq_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def givegift(qq_id, to_group, to_obj, pid):
    """ 送群礼物（成功返回1 失败返回-1）Pro可用
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_group: 群号 文本型 需送礼物群号
	:param to_obj: 对象QQ 文本型 赠予礼物对象
	:param pid: pid 文本型 礼物pid
    :return: 整数型
    """
    global message_socket
    order = {'func': "givegift", 'qq_id': qq_id, 'to_group': to_group, 'to_obj': to_obj, 'pid': pid}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getgroupchatlv(qq_id, to_group, to_obj):
    """ 查询对象或自身群聊等级（返回实际等级 失败返回-1）Pro可用
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_group: 群号 文本型 查询群号
	:param to_obj: 对象QQ 文本型 需查询对象或机器人QQ
    :return: 整数型
    """
    global message_socket
    order = {'func': "getgroupchatlv", 'qq_id': qq_id, 'to_group': to_group, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getexpertdays(qq_id, to_obj):
    """ 查询对象或自身QQ达人天数（返回实际天数 失败返回-1）Pro可用
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_obj: 对象QQ 文本型 需查询对象或机器人QQ
    :return: 整数型
    """
    global message_socket
    order = {'func': "getexpertdays", 'qq_id': qq_id, 'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def invitegroup_other(qq_id, from_group, to_group, to_obj):
    """ 邀请别人群成员加入自己群  Pro可用
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param from_group: 目标群号 文本型 要进入的群的群号
	:param to_group: 所在群号 文本型 被邀请人和机器人共同存在的群号
	:param to_obj: 邀请QQ 文本型 被邀请人的QQ 多个换行提交
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "invitegroup_other", 'qq_id': qq_id, 'from_group': from_group, 'to_group': to_group,
             'to_obj': to_obj}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getshieldedstate(qq_id, OQ_):
    """ 获取机器人QQ是否被屏蔽消息发送状态（真屏蔽 假未屏蔽）
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param OQ_: OQ_ 整数型 0在线临时会话 1好友 2群 3讨论组 4群临时会话 5讨论组临时会话 7好友验证回复会话
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "getshieldedstate", 'qq_id': qq_id, 'OQ_': OQ_}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def addfriend(qq_id, target_qq, var_msg):
    """ 加好友 易频繁 有问题验证无法添加
	:param qq_id: 响应QQ  文本型
	:param target_qq: 目标QQ  文本型
	:param var_msg: 验证信息  文本型
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "addfriend", 'qq_id': qq_id, 'target_qq': target_qq, 'var_msg': var_msg}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def addfriend_b(qq_id, to_obj, reason, to_group, source, version):
    """ ;Api_AddFriend_B ;
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_obj: 对象QQ 文本型 加谁
	:param reason: 附加理由 文本型 加好友提交的理由
	:param to_group: 群号 文本型 跟对方处于同一个群时可填，类似于加群好友 没有则填空
	:param source: 来源 整数型 1 QQ号查找、2来自QQ群、3来自QQ游戏、4来自多人聊天、5来自好友推荐、6可能认识的人
	:param version: 版本 整数型 1新版 2旧版 0随机
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "addfriend_b", 'qq_id': qq_id, 'to_obj': to_obj, 'reason': reason, 'to_group': to_group,
             'source': source, 'version': version}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def setvalidation(qq_id, set_type, question, answer, question1, question2, question3):
    """ 设置加好友验证
	:param qq_id: 响应QQ  文本型
	:param set_type: 设置类型 整数型 0允许任何人 1需要验证消息 2不允许任何人 3需要回答正确问题 4需要回答问题并由我确认
	:param question: 回答正确问题_问题 文本型 类型=3时填写 否则留空
	:param answer: 回答正确问题_答案 文本型 类型=3时填写 否则留空
	:param question1: 需要回答问题1 文本型 类型=4时填写 否则留空
	:param question2: 需要回答问题2 文本型 类型=4时填写 否则留空
	:param question3: 需要回答问题3 文本型 类型=4时填写 否则留空
    :return:
    """
    global message_socket
    order = {'func': "setvalidation", 'qq_id': qq_id, 'set_type': set_type, 'question': question, 'answer': answer,
             'question1': question1, 'question2': question2, 'question3': question3}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def handlefriendevent(qq_id, to_obj, dispose_type, msg):
    """ 处理好友添加请求
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_obj: 对象QQ 文本型 请求添加好友人QQ
	:param dispose_type: 处理方式 整数型 10同意 20拒绝 30忽略
	:param msg: 附加信息 文本型 拒绝添加好友 附加信息
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "handlefriendevent", 'qq_id': qq_id, 'to_obj': to_obj, 'dispose_type': dispose_type, 'msg': msg}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def upheadimg(qq_id, pic_path):
    """ 上传头像 QQ在线150秒后有效
	:param qq_id: 响应QQ  文本型
	:param pic_path: 图片路径 文本型 本地绝对路径
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "upheadimg", 'qq_id': qq_id, 'pic_path': pic_path}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getqrcode():
    """ 返回二维码标识和二维码图片base编码数据 换行符分割 第一行为二维码标识 第二行为二维码的base编码数据 标识用于查询当前二维码状态

    :return: 文本型
    """
    global message_socket
    order = {'func': "getqrcode"}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def checkqrcode(qr_id):
    """ 取二维码状态，-1二维码失效 0获取失败(网络超时异常等) 1正在等待扫码中 2已扫码等待确认 3已确认正在登陆
	:param qr_id: 二维码ID 文本型 二维码标识
    :return: 整数型
    """
    global message_socket
    order = {'func': "checkqrcode", 'qr_id': qr_id}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def setgroupcation(qq_id, to_group, type, question, answer):
    """ 设置群验证方式
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param to_group: 群号 文本型 需要设置的QQ群号 需要机器人为管理员
	:param type: 类型 整数型 1允许任何人 2需要验证信息 3需要回答问题 4需要正确回答问题 5禁止加群
	:param question: 设置问题 文本型 当类型为 3 4 时填写 问题 其他类型可空
	:param answer: 问题答案 文本型 当验证方式为 4 时写答案 其他类型可空
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "setgroupcation", 'qq_id': qq_id, 'to_group': to_group, 'type': type, 'question': question,
             'answer': answer}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getclientver():
    """ 客户端版本

    :return: 文本型
    """
    global message_socket
    order = {'func': "getclientver"}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getclienttype():
    """ 取客户端类型

    :return: 文本型
    """
    global message_socket
    order = {'func': "getclienttype"}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getreleaseno():
    """ 取发行版本号

    :return: 文本型
    """
    global message_socket
    order = {'func': "getreleaseno"}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def upphotowall(qq_id, pic_path):
    """ 上传照片墙
	:param qq_id: 响应QQ  文本型
	:param pic_path: 图片路径 文本型 本地绝对路径
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "upphotowall", 'qq_id': qq_id, 'pic_path': pic_path}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def upgroupfile(qq_id, target_group, file_path):
    """ 发送群文件 Pro可用
	:param qq_id: 响应QQ  文本型
	:param target_group: 目标群  文本型
	:param file_path: 本地文件路径  文本型
    :return:
    """
    global message_socket
    order = {'func': "upgroupfile", 'qq_id': qq_id, 'target_group': target_group, 'file_path': file_path}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def upfile(qq_id, target_group, obj, file_path):
    """ 发送文件 Pro可用
	:param qq_id: 响应QQ  文本型
	:param target_group: 目标群 文本型 发送群临时会话文件时填写
	:param obj: 对象  文本型
	:param file_path: 本地文件路径  文本型
    :return:
    """
    global message_socket
    order = {'func': "upfile", 'qq_id': qq_id, 'target_group': target_group, 'obj': obj, 'file_path': file_path}
    message_socket.send_message(json.dumps(order, ensure_ascii=False))


def ifgroupprivate(qq_id, target_group):
    """ 判断可否群私聊
	:param qq_id: 响应QQ  文本型
	:param target_group: 目标群  文本型
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "ifgroupprivate", 'qq_id': qq_id, 'target_group': target_group}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def iscreategroup(qq_id, target_group):
    """ 查询群是否支持群成员创建群聊 Pro可用
	:param qq_id: 响应QQ  文本型
	:param target_group: 目标群  文本型
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "iscreategroup", 'qq_id': qq_id, 'target_group': target_group}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def getanon(qq_id, target_group):
    """ 查询群是否支持匿名聊天 真为支持 假不支持
	:param qq_id: 响应QQ  文本型
	:param target_group: 目标群  文本型
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "getanon", 'qq_id': qq_id, 'target_group': target_group}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)


def setcover(qq_id, pic_path):
    """ 设置封面
	:param qq_id: 响应QQ 文本型 机器人QQ
	:param pic_path: 图片路径 文本型 本地图片路径
    :return: 逻辑型
    """
    global message_socket
    order = {'func': "setcover", 'qq_id': qq_id, 'pic_path': pic_path}
    message_id = message_socket.send_message(json.dumps(order, ensure_ascii=False))
    return message_socket.accept_message(message_id)
