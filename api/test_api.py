import json

import requests
from loguru import logger
import os
import time
import pytest

from api import base


class TestApi:
    @pytest.fixture(scope="class", autouse=True)
    def pytest_config(self):
        # 转盘抽奖1、2、3天的奖品数是变化的
        day = 1
        yield day

    def test_activity_lottery_get_lottery_array(self, pytest_config) -> None:
        """
        获取当天的总中奖数，与对应的天进行数据比对
        """
        day = pytest_config
        baseapi = base.BaseAPI()
        lottery_array = list(baseapi.activity_lottery_get_lottery_array()['data'])
        logger.info(f"lottery_array={lottery_array}")
        A_number = 0
        B_number = 0
        C_number = 0
        D_number = 0
        E_number = 0
        F_number = 0
        G_number = 0
        H_number = 0
        # first_2000_gift_list = lottery_array[0:2000]
        gift_count = 0
        for new_gift in lottery_array:
            # logger.info(gift)
            gift_count += 1
            if new_gift == 'A':
                A_number += 1
                print(f"A_奖品出现在第{gift_count}次")
            elif new_gift == 'B':
                B_number += 1
                print(f"B_奖品出现在第{gift_count}次")
            elif new_gift == 'C':
                C_number += 1
                # print(f"C_奖品出现在第{gift_count}次")
            elif new_gift == 'D':
                D_number += 1
            elif new_gift == 'E':
                E_number += 1
            elif new_gift == 'F':
                F_number += 1
                print(f"F_奖品出现在第{gift_count}次")
            elif new_gift == 'G':
                G_number += 1
            elif new_gift == 'H':
                H_number += 1
        print(f"A_number={A_number},B_number={B_number},C_number={C_number},D_number={D_number},"
              f"E_number={E_number},F_number={F_number},G_number={G_number},H_number={H_number}")

        # if day == 1:
        #     assert A_number == 3
        #     assert B_number == 3
        #     assert C_number == 100
        #     assert D_number == 50
        #     assert E_number == 300
        #     assert F_number == 300
        #     assert G_number == 1300
        # elif day == 2:
        #     assert A_number == 3
        #     assert B_number == 3
        #     assert C_number == 100
        #     assert D_number == 50
        #     assert E_number == 300
        #     assert F_number == 300
        #     assert G_number == 1300
        # elif day == 3:
        #     assert A_number == 4
        #     assert B_number == 4
        #     assert C_number == 100
        #     assert D_number == 50
        #     assert E_number == 399
        #     assert F_number == 399
        #     assert G_number == 1300

    @pytest.mark.parametrize("iteration", range(39))
    def test_activity_lottery_add_lottery_record(self, iteration) -> None:
        """
        操作抽奖
        """

        baseapi = base.BaseAPI()

        # 获取当前的游标数
        cursor_response = baseapi.activity_lottery_get_lottery_cursor()
        logger.info(f"cursor={cursor_response}")
        cursor = cursor_response['data']['lpPrizeCursor']
        logger.info(f"当前cursor={cursor}")

        # 获取下一个奖品数 = 当前游标+1对应的 奖品数
        lottery_array = list(baseapi.activity_lottery_get_lottery_array()['data'])
        logger.info(f"lottery_array={lottery_array}")

        lottery = lottery_array[cursor]
        logger.info(f"当前奖品lottery={lottery}")

        add_response = baseapi.activity_lottery_add_lottery_record(lottery)
        logger.info(f"add_response={add_response}")
        assert add_response['data'] == True

        cursor_response = baseapi.activity_lottery_get_lottery_cursor()
        cursor = cursor_response['data']['lpPrizeCursor']
        logger.info(f"当前cursor={cursor}")

        time.sleep(1)
