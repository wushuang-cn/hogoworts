#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-14 22:20
# author：WuShuang5
import os
import signal
import subprocess

import pytest


# 如果是windows 需要以管理员身份打开pycharm这个软件 再运行case
from UI_Framework.pages.log import loginit


# @pytest.fixture(scope="module",autouse=True)
# def luping():
#     loginit()# 对日志初始化
#
#     #windows将cmd的编码格式设置为utf-8
#     os.system('chcp 65001')
#     cmd='scrcpy -Nr ./tmp.mp4'
#     #执行cmd终端命令
#     p= subprocess.Popen(cmd,shell=True)
#     yield
#     #操作后 杀掉进程
#     os.kill(p.pid,signal.CTRL_C_EVENT)