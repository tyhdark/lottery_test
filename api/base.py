import requests
from loguru import logger


class BaseAPI(object):
    def __init__(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'way': 'WEB'
        }

        # UAT
        url = "https://gateway.meuat.xyz"
        self.headers = headers
        self.url = url

    def activity_lottery_get_lottery_array(self):
        """
        获取总的中奖列表
        :return:
        """
        response = requests.get(f"{self.url}/activity/Lottery/getLotteryArray/2",
                                headers=self.headers)
        elapsed_time = response.elapsed.total_seconds()
        logger.info(f"/activity/Lottery/getLotteryArray/1 耗时——>{elapsed_time}")
        return response.json()

    def activity_lottery_get_lottery_cursor(self):
        """
        获取当前抽奖游标
        :return:
        """
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'way': 'WEB'
        }
        response = requests.post(f"{self.url}/activity/Lottery/getLotteryCursor/2",
                                 headers=self.headers)
        elapsed_time = response.elapsed.total_seconds()
        logger.info(f"/activity/Lottery/getLotteryCursor/2 耗时——>{elapsed_time}")
        return response.json()

    def activity_lottery_add_lottery_record(self, lrLcLabel):
        """
        添加中奖记录给服务端
        :param lrLcLabel:
        """
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'way': 'WEB'
        }
        data = "{\"lrAccount\":\"any\",\"lrName\":\"any\",\"lrLcLabel\":\"G\",\"activityType\":\"2\"}"
        data = data.replace("G", str(lrLcLabel))
        logger.info(f"传递给服务端的json={data}")
        response = requests.post(f"{self.url}/activity/Lottery/addLotteryRecord", data=data,
                                 headers=headers)
        # 获取耗时
        elapsed_time = response.elapsed.total_seconds()
        logger.info(f"/activity/Lottery/addLotteryRecord 耗时——>{elapsed_time}")
        return response.json()
