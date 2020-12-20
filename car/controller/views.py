from django.views.generic import View
from django.http import JsonResponse
import socket

class ControllerView(View):
    def get(self, request):
        # 接收数据
        signal = request.GET.get('c2vsignal')
        # 业务处理
        # 创建套接字
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 链接
        tcp_socket.connect(("192.168.0.112", 10000))
        # 收发数据
        tcp_socket.send(signal)
        # 关闭套接字
        tcp_socket.close()
        # 返回应答
        return JsonResponse({'msg': signal})