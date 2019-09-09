from one import views
from django.urls import path, include
from django.conf.urls import url


urlpatterns = [
    path('admin/kashano', views.kashano, name='kashano'),
    path('admin/send', views.send, name='send'),
    path('admin/get', views.get, name='get'),
    path('admin/setting', views.setting, name='setting'),
]
