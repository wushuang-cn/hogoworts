#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-15 14:42
# author：WuShuang5
import logging
import logging.handlers


def loginit():
    # 设置格式
    log_format_str = '[%(asctime)s]  %(filename)s:%(lineno)d:%(funcName)s: %(message)s'

    format = logging.Formatter(log_format_str)

    # 根据 log 标识获取 log

    root = logging.getLogger("my_log")

    # 加入文件句柄 输出到文件

    h = logging.handlers.RotatingFileHandler("../logs/tmp.log", mode='a', encoding="utf-8")

    h.setFormatter(format)

    # 加入输出流句柄

    s = logging.StreamHandler()

    s.setFormatter(format)

    root.addHandler(h)

    root.addHandler(s)

    root.setLevel(logging.DEBUG)

# 获取 log

logger = logging.getLogger("my_log")
