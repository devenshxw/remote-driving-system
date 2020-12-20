from django.conf.urls import url
from controller.views import ControllerView


urlpatterns = [
    url(r'^ss/$', ControllerView.as_view()),
    url(r'^tm/$', ControllerView.as_view()),
    url(r'^turnLeft/$', ControllerView.as_view()),
    url(r'^turnRight/$', ControllerView.as_view()),
    url(r'^speedDown/$', ControllerView.as_view()),
    url(r'^speedUp/$', ControllerView.as_view()),
]
