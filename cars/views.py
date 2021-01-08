from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Color, Car, Client, ClientPassportData, Manager, Order
from django.forms import ModelForm


class ColorList(ListView):
    model = Color
    template_name = 'cars/color_list.html'


class ColorCreate(CreateView):
    model = Color
    template_name = 'create_instance.html'
    success_url = '/db_viewer/color/'
    fields = ['name']


class ColorUpdate(UpdateView):
    model = Color
    template_name = 'update_instance.html'
    success_url = '/db_viewer/color/'
    fields = ['name']


class ColorDelete(DeleteView):
    model = Color
    template_name = 'delete_instance.html'
    success_url = '/db_viewer/color/'


class CarList(ListView):
    model = Car
    template_name = 'cars/car_list.html'


class CarCreate(CreateView):
    model = Car
    template_name = 'create_instance.html'
    success_url = '/db_viewer/car/'
    fields = ['car_model',
              'color',
              'production_date',
              'is_free',
              'price']


class CarUpdate(UpdateView):
    model = Car
    template_name = 'update_instance.html'
    success_url = '/db_viewer/car/'
    fields = ['car_model',
              'color',
              'production_date',
              'is_free',
              'price']


class CarDelete(DeleteView):
    model = Car
    template_name = 'delete_instance.html'
    success_url = '/db_viewer/car/'


class ClientList(ListView):
    model = Client
    template_name = 'cars/client_list.html'


class ClientCreate(CreateView):
    model = Client
    template_name = 'create_instance.html'
    success_url = '/db_viewer/client/'
    fields = ['FIO',
              'car',
              ]


class ClientUpdate(UpdateView):
    model = Client
    template_name = 'update_instance.html'
    success_url = '/db_viewer/client/'
    fields = ['FIO',
              # 'car',
              ]


class ClientDelete(DeleteView):
    model = Client
    template_name = 'delete_instance.html'
    success_url = '/db_viewer/client/'


class ClientPassportDataList(ListView):
    model = ClientPassportData
    template_name = 'cars/client_passport_data_list.html'


class ClientPassportDataCreate(CreateView):
    model = ClientPassportData
    template_name = 'create_instance.html'
    success_url = '/db_viewer/client_passport_data/'
    fields = ['client',
              'series',
              'number',
              'issued_by_whom',
              ]


class ClientPassportDataUpdate(UpdateView):
    model = ClientPassportData
    template_name = 'update_instance.html'
    success_url = '/db_viewer/client_passport_data/'
    fields = ['client',
              'series',
              'number',
              'issued_by_whom',
              ]


class ClientPassportDataDelete(DeleteView):
    model = ClientPassportData
    template_name = 'delete_instance.html'
    success_url = '/db_viewer/client_passport_data/'


class ManagerList(ListView):
    model = Manager
    template_name = 'cars/manager_list.html'


class ManagerCreate(CreateView):
    model = Manager
    template_name = 'create_instance.html'
    success_url = '/db_viewer/manager/'
    fields = ['FIO',
              'salary',
              ]


class ManagerUpdate(UpdateView):
    model = Manager
    template_name = 'update_instance.html'
    success_url = '/db_viewer/manager/'
    fields = ['FIO',
              'salary',
              ]


class ManagerDelete(DeleteView):
    model = Manager
    template_name = 'delete_instance.html'
    success_url = '/db_viewer/manager/'


class OrderList(ListView):
    model = Order
    template_name = 'cars/order_list.html'


class OrderCreate(CreateView):
    model = Order
    template_name = 'create_instance.html'
    success_url = '/db_viewer/order/'
    fields = ['manager',
              'client',
              'car',
              'days_to_use',
              'closed',
              ]


class OrderUpdate(UpdateView):
    model = Order
    template_name = 'update_instance.html'
    success_url = '/db_viewer/order/'
    fields = ['manager',
              'client',
              'car',
              'date_created',
              'days_to_use',
              'closed',
              ]


class OrderDelete(DeleteView):
    model = Order
    template_name = 'delete_instance.html'
    success_url = '/db_viewer/order/'
