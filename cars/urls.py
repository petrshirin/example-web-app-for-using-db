from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('color/', ColorList.as_view()),
    path('color/edit/<int:pk>', ColorUpdate.as_view()),
    path('color/create/', ColorCreate.as_view()),
    path('color/delete/<int:pk>', ColorDelete.as_view()),

    path('car/', CarList.as_view()),
    path('car/edit/<int:pk>', CarUpdate.as_view()),
    path('car/create/', CarCreate.as_view()),
    path('car/delete/<int:pk>', CarDelete.as_view()),

    path('client/', ClientList.as_view()),
    path('client/edit/<int:pk>', ClientUpdate.as_view()),
    path('client/create/', ClientCreate.as_view()),
    path('client/delete/<int:pk>', ClientDelete.as_view()),

    path('client_passport_data/', ClientPassportDataList.as_view()),
    path('client_passport_data/edit/<int:pk>', ClientPassportDataUpdate.as_view()),
    path('client_passport_data/create/', ClientPassportDataCreate.as_view()),
    path('client_passport_data/delete/<int:pk>', ClientPassportDataDelete.as_view()),

    path('manager/', ManagerList.as_view()),
    path('manager/edit/<int:pk>', ManagerUpdate.as_view()),
    path('manager/create/', ManagerCreate.as_view()),
    path('manager/delete/<int:pk>', ManagerDelete.as_view()),

    path('order/', OrderList.as_view()),
    path('order/edit/<int:pk>', OrderUpdate.as_view()),
    path('order/create/', OrderCreate.as_view()),
    path('order/delete/<int:pk>', OrderDelete.as_view()),
]
