# !/usr/bin/python3
# -*- coding: utf-8 -*-
import socket


class TcpServer(object):
    """服务器"""
    # 创建套接字，等待客户端链接
    def __init__(self, server_address):
        # 创建tcp套接字
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 允许立即使用上次绑定的port
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定
        self.listen_socket.bind(server_address)
        # 变为被动，并制定队列的长度
        self.listen_socket.listen(128)

    def run_forever(self):
        """循环运行服务器，等待客户端的链接并为远程客户服务"""
        while True:
            # 客户端链接到来
            client_socket, client_addr = self.listen_socket.accept()
            print("客户端%s连接成功" % str(client_addr))

            # 为客户服务
            self.service(client_socket, client_addr)

            # 关闭客户端套接字
            client_socket.close()

    def service(self, client_socket, client_addr):
        print("服务主程序")
