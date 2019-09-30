from kashano import views
from django.urls import path, include
from django.conf.urls import url


urlpatterns = [
    path('', views.home, name='home'),
    path('kashano/get/', views.get, name='get'),
    path('kashano/', views.kashano, name='kashano'),
    path('kashano/view/', views.view_record, name='view_record'),
    path('kashano/export/', views.export_file, name='export_file'),
    path('kashano/delete/', views.delete_record, name='delete_record'),
    path('kashano/setting/', views.get_setting, name='kashano_setting'),
]