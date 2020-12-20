from django.views.generic import View
from django.http import JsonResponse


class ControllerView(View):
    def get(self, request):
        # 接收数据
        signal = request.GET.get('c2vsignal')
        # 业务处理

        # 返回应答
        return JsonResponse({'msg': signal})