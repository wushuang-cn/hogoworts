#! /usr/bin/env python
# -*- coding:utf-8 -*-
# date：2021-03-22 22:24
# author：WuShuang5
import json

import mitmproxy.http
from mitmproxy import http


class Events:
    def http_connect(self, flow: mitmproxy.http.HTTPFlow):
        """
            An HTTP CONNECT request was received. Setting a non 2xx response on
            the flow will return the response to the client abort the
            connection. CONNECT requests and responses do not generate the usual
            HTTP handler events. CONNECT requests are only valid in regular and
            upstream proxy modes.
        """
        pass

    def requestheaders(self, flow: mitmproxy.http.HTTPFlow):
        """
            HTTP request headers were successfully read. At this point, the body
            is empty.
        """
        pass

    def request(self, flow: mitmproxy.http.HTTPFlow):

        pass
        #模拟map local
        #返回的格式是json
        # if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
        #     with open('./xueqiu.json','r',encoding='utf-8') as f:
        #         flow.response=http.HTTPResponse.make(200,f.read(),{"Content-Type":"text/html"}
        #                                              )


    def responseheaders(self, flow: mitmproxy.http.HTTPFlow):
        """
            HTTP response headers were successfully read. At this point, the body
            is empty.
        """
        pass

    def response(self, flow: mitmproxy.http.HTTPFlow):
        pass

        #  指定url为雪球
        #   模拟rewrite 模式，修改响应体内容
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            # print(f"看这里啊{flow.response.text}")
            # mydata=json.loads(flow.response.text)   #是str类型,需要反序列化
            with open('./xueqiu.json','r',encoding='utf-8') as f:
                flow.response.text=f.read()

            # self.handle_data(mydata)
            # flow.response.text=json.dumps(self.handle_data(mydata))

    def handle_data(self, data):
        if isinstance(data, dict):
            for k, v in data.items():
                data[k] = self.handle_data(v)
        elif isinstance(data, list):
            for one in data:
                self.handle_data(one)
        elif isinstance(data, str):
            data = data
        elif isinstance(data, (int, float)):
            data = data * 1000
        else:
            pass
        return data


    def error(self, flow: mitmproxy.http.HTTPFlow):
        """
            An HTTP error has occurred, e.g. invalid server responses, or
            interrupted connections. This is distinct from a valid server HTTP
            error response, which is simply a response with an HTTP error code.
        """
        pass

addons = [
    Events()
]
