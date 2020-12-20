from django.conf.urls import url
from vehicle.views import LoginView


urlpatterns = [
    url(r'^$', LoginView.as_view()),
]
