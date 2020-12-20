#!/usr/bin/python3
# -*- coding: utf-8 -*-
import threading
import time
from server import TcpServer


def recv_msg(client_socket):
    while True:
        recv_content = client_socket.recv(1024)
        if recv_content:
            #    包头     发动机启动    变速箱   加速减速    转向   包尾
            #      #         1          0        0        0       $
            print("开始小车控制...")
            recv_content = recv_content.decode("utf-8")
        else:
            # 关闭发动机
            break


def send_msg(client_socket):
    while True:
        # 如果线程数小于等于2，则说明发动机关闭，结束发送速度信息
        threading_num = len(threading.enumerate())
        if threading_num <= 2:
            break
        print("发送速度信息...")
        time.sleep(1)


class CarCtrlServer(TcpServer):
    """小车控制服务器"""
    def __init__(self, server_address):
        super().__init__(server_address)

    def service(self, client_socket, client_addr):
        print("%s小车控制进程启动..."  % str(client_addr))

        thread_recv = threading.Thread(target=recv_msg, args=(client_socket,))
        thread_send = threading.Thread(target=send_msg, args=(client_socket,))
        # 接收消息子线程
        thread_recv.start()
        # 发送消息子线程
        thread_send.start()

        while True:
            threading_num = len(threading.enumerate())
            if threading_num <= 1:
                print("%s小车控制进程结束" % str(client_addr))
                break


# 设定小车控制的IP和端口
SERVER_ADDR = (HOST, PORT) = "192.168.0.114", 10000


def car_ctrl():
    """小车控制程序"""
    car_controller = CarCtrlServer(SERVER_ADDR)
    car_controller.run_forever()


if __name__ == "__main__":
    car_ctrl()
