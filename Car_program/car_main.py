#!/usr/bin/python3
# -*- coding: utf-8 -*-
import multiprocessing
import car_control
import video_control
from server import TcpServer


class CarServer(TcpServer):
    """小车服务器"""
    def __init__(self, server_address):
        super().__init__(server_address)

    def service(self, client_socket, client_addr):
        while True:
            request = client_socket.recv(1024)
            if request:
                print("启动小车控制、视频控制两个进程，为客户服务...")
                car_ctrl_process = multiprocessing.Process(target=car_control.car_ctrl)
                video_ctrl_process = multiprocessing.Process(target=video_control.video_ctrl)
                car_ctrl_process.start()
                video_ctrl_process.start()
            else:
                # 如果客户端关闭，终止子进程
                car_ctrl_process.terminate()
                video_ctrl_process.terminate()
                print("客户端%s退出" % str(client_addr))
                break


# 设定小车服务器的IP和端口
SERVER_ADDR = (HOST, PORT) = "192.168.0.114", 8888


def car_main():
    """小车主程序"""
    my_car = CarServer(SERVER_ADDR)
    my_car.run_forever()


if __name__ == "__main__":
    car_main()
