#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import threading
from server import TcpServer


def recv_msg(client_socket):
    while True:
        recv_content = client_socket.recv(1024)
        if recv_content:
            print("开始视频控制...")
        else:
            # 关闭摄像头
            break


def send_msg(client_socket):
    while True:
        # 如果线程数小于等于2，则说明摄像头关闭，结束发送视频信息
        threading_num = len(threading.enumerate())
        if threading_num <= 2:
            break
        print("发送视频信息...")
        time.sleep(1)


class VideoCtrlServer(TcpServer):
    """视频采集服务器"""
    def __init__(self, server_address):
        super().__init__(server_address)

    def service(self, client_socket, client_addr):
        print("%s视频采集进程启动..." % str(client_addr))

        thread_recv = threading.Thread(target=recv_msg, args=(client_socket,))
        thread_send = threading.Thread(target=send_msg, args=(client_socket,))
        # 接收消息子线程
        thread_recv.start()
        # 发送消息子线程
        thread_send.start()

        while True:
            threading_num = len(threading.enumerate())
            if threading_num <= 1:
                print("%s视频采集进程结束" % str(client_addr))
                break


# 设定小车控制的IP和端口
SERVER_ADDR = (HOST, PORT) = "192.168.0.114", 20000


def video_ctrl():
    """视频采集程序"""
    video_controller = VideoCtrlServer(SERVER_ADDR)
    video_controller.run_forever()


if __name__ == "__main__":
    video_ctrl()
