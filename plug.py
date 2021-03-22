import api

def init(init_api: api):
    pass


def main(event):
    qq_id: str = event['qq_id']  # 用于判定哪个QQ接收到该消息
    type: int = event['type']  # 接收到消息类型，该类型可在常量表中查询具体定义，
    # 此处仅列举： -1 未定义事件 0,在线状态临时会话 1,好友信息 2,群信息 3,讨论组信息 4,群临时会话 5,讨论组临时会话 6,财付通转账 7,好友验证回复会话
    sub_type: int = event['sub_type']  # 此参数在不同ER_下，有不同的定义，暂定：接收财付通转账时 1待确认收款 0为已收款    有人请求入群时，不良成员这里为1
    source: str = event['source']  # 此消息的来源，如：群号、讨论组ID、临时会话QQ、好友QQ等
    from_obj: str = event['from_obj']  # 主动发送这条消息的QQ，踢人时为踢人管理员QQ
    to_obj: str = event['to_obj']  # 被动触发的QQ，如某人被踢出群，则此参数为被踢出人QQ
    msg: str = event['msg']  # 此参数有多重含义，常见为：对方发送的消息内容，但当ER_消息类型为 某人申请入群，则为入群申请理由,当消息类型为财付通转账时为 原始json
    serial: str = event['serial']  # 此参数暂定用于消息撤回
    msg_id: str = event['msg_id']  # 此参数暂定用于消息撤回
    seq: str = event['seq']  # UDP收到的原始信息，特殊情况下会返回JSON结构（入群事件时，这里为该事件seq）【原始消息会被阉割 这里可以看做就是seq】
    pointer: int = event['pointer']  # 此参数用于插件加载拒绝理由  【无用】

    