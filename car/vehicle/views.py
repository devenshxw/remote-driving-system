from django.views.generic import View
from django.http import JsonResponse
from vehicle.models import Vehicles
import socket


class LoginView(View):
    def get(self, request):
        # 接收数据
        vin = request.GET.get('vincode')
        pwd = request.GET.get('password')
        # 校验数据
        if not all([vin, pwd]):
            return JsonResponse({'msg': '0数据不完整'})
        # 业务处理
        # user = authenticate(username='vin', password='pwd')
        # if user is not None:
        #     if user.is_active:
        #         # 用户已激活
        #         # 记录用户的登录状态
        #         login(request, user)
        #         # 返回登录成功提示
        #         return JsonResponse({'msg': '登录成功'})
        #     else:
        #         # 用户未激活
        #         return JsonResponse({'msg': '账户未激活'})
        # else:
        #     return JsonResponse({'msg': 'VIN或密码错误'})
        try:
            ret = Vehicles.objects.get(vin=vin, pwd=pwd)
        except Exception:
            return JsonResponse({'msg': '1VIN或密码错误'})
        else:
            if ret:
                # 创建套接字
                tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # 链接
                tcp_socket.connect(("192.168.0.112", 8888))
                # 收发数据
                tcp_socket.send(ret)

                return JsonResponse({'msg': '2登录成功'})
                # 关闭套接字
                tcp_socket.close()

