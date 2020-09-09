from django.contrib import admin
from django.urls import path, include, re_path
from . import views

app_name = 'coffe_m'

urlpatterns = [
    path('', views.all_clients, name='clients'),
    path('reports', views.report_visits, name='report_visits'),
    path('useful_code', views.useful_code, name='useful_code'),
    path('useful_docs', views.useful_docs, name='useful_docs'),
    path('create_visit', views.Create_visit.as_view(), name='create_visit'),
    path('create_useful_code', views.Create_Useful_code.as_view(), name='create_useful_code'),
    path('create_useful_docs', views.Create_Useful_docs.as_view(), name='create_useful_docs'),
    path('create_visit/<int:create_visit_id>/', views.Create_visit.as_view(), name='create_visit'),
    path('accounts/', include('django.contrib.auth.urls')),

    # path('car/<int:car_id>', views.car_details, name='car_details'),
    # path('car/<int:car_id>/share/', views.share_car, name='share_car'),
]