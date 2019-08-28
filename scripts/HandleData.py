class HandleData:
    @staticmethod
    def handle_data(data):
        msg_id = data["msg_id"]
        if not msg_id:
            d = (False, {"errCode": 1, "errMsg": "消息格式错误"})
            return d
        if msg_id == "loginReq":
            return HandleData.handle_login(data)
        elif msg_id == "addMdcReq":
            return HandleData.handle_add_mdc(data)

    @staticmethod
    def handle_login(data):
        username = data["username"]
        password = data["password"]
        if not username or not password:
            couple = (False, {"msg_id": "loginAck", "errCode": 99, "errMsg": "用户名或密码错误"})
            return couple
        if (username == "manager" and data["password"] == "888888")\
                or (username == "doctor" and data["password"] == "888888")\
                or (username == "user1" and data["password"] == "888888")\
                or (username == "user2" and data["password"] == "888888"):
            couple = (True, {"msg_id": "loginAck", "errCode": 0, "errMsg": ""}, {"username": username})  # 第一个元素为操作是否成功，第二个元素为消息体发送给客户端，如果操作成功，第三个元素为附加信息
            return couple
        else:
            couple = (False, {"msg_id": "loginAck", "errCode": 99, "errMsg": "用户名或密码错误"})
            return couple

    @staticmethod
    def handle_add_mdc(data):
        couple = (True, {"msg_id": "addMdcAck", "errCode": 0, "errMsg": ""})
        return couple
