import requests


def send_something_to_dingding(self):
    """
    发送一些内容给钉钉机器人
    :return:
    """
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'way': 'WEB'
    }
    body = {
        "text": {
            "content":"开始执行UI自动化用例：Android:test_mepass_regist,test_mepass_kycUser_login"
        },
        "msgtype":"text"
    }
    response = requests.post("https://oapi.dingtalk.com/robot/"
                             "send?access_token=2e7f78358944bfe597d78042c0a9ed15dcabbf8c47378683e8637a5af7c89228",
                             data=body)
    return response.json()



if __name__ == '__main__':
    send_something_to_dingding()