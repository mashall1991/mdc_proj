# 登录

# 登录请求
loginReq = {
    "msg_id": "loginReq",
    "username": "string",
    "password": "string"
}
# 登录回复
loginAck = {
    "msg_id": "loginAck",
    "errCode": "number",  # errCode为0成功，非零失败。 99用户名或密码错误
    "errMsg": "string",  # 错误信息
}
# 管理员

# 增加药品
addMdcReq = {
    "msg_id": "addMdcReq",
    "name": "string",  # 药品名
    "price": "number",  # 价格/g
    "stock": "number",  # 库存g,显示时换算成kg
}

addMdcAck = {
    "msg_id": "addMdcAck",
    "errCode": "number",  # 药品已存在 errCode = 100
    "errMsg": "string",
}

# 修改药品

modifyMdcReq = {
    "msg_id": "modifyMdcReq",
    "name": "string",  # 要修改的药品名
    "price": "number",  # 修改后的价格 optional选填
    "stock": "number",  # 修改后的库存 optional
}
modifyMdcAck = {
    "msg_id": "modifyMdcAck",
    "errCode": "number",  # 药品不存在 errCode = 101
    "errMsg": "string",
}

# 删除药品
deleteMdcReq = {
    "msg_id": "deleteMdcReq",
    "name": "string"  # 删除的药品名
}
deleteMdcAck = {
    "msg_id": "deleteMdcAck",
    "errCode": "number",  # 药品不存在 101
    "errMsg": "string"
}
# 药品type
mdc = {
    "name": "string",
    "price": "number",
    "stock": "number"
}
# 获得所有药品
getAllMdcReq = {
    "msg_id": "getAllMdcReq",
}

getAllMdcAck = {
    "msg_id": "getAllMdcAck",
    "errCode": "number",  # 一般情况下都为0
    "errMsg": "number",
    "msg_data": "[mdc]",  # []表示数组，[]内部表示数组的元素类型，此处为mdc类型
}


