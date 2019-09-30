from one import views
from django.urls import path, include
from django.conf.urls import url


urlpatterns = [
    path('admin/kashano', views.kashano, name='kashano'),
    path('admin/kashano/send', views.send, name='send'),
    path('admin/kashano/get', views.get, name='get'),
    path('admin/kashano/setting_get', views.setting_get, name='setting_get'),
    path('admin/kashano/setting_metraj', views.setting_metraj, name='setting_metraj'),
    path('admin/kashano/setting_kashano', views.setting_kashano, name='setting_kashano'),
]
