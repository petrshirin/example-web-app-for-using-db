from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.timezone import now


class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    car_model = models.CharField(max_length=255)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    production_date = models.PositiveIntegerField()
    is_free = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.car_model} {self.production_date} {self.color}'


class Client(models.Model):
    FIO = models.CharField(max_length=500)
    car = models.ManyToManyField(Car, blank=True)

    def __str__(self):
        return self.FIO


class ClientPassportData(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, null=True)
    series = models.CharField(max_length=4, null=True)
    number = models.CharField(max_length=6, null=True)
    issued_by_whom = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"passport data: {self.client}"


class Manager(models.Model):
    FIO = models.CharField(max_length=500)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.FIO


class Order(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(default=now, blank=True)
    days_to_use = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, editable=False)
    closed = models.BooleanField(default=False)


@receiver(post_save, sender=Client)
def create_user_passport_data(sender, instance, created, **kwargs):
    if created:
        ClientPassportData.objects.create(client=instance)


@receiver(post_save, sender=Client)
def save_user_passport_data(sender: Client, instance: Client, **kwargs):
    instance.clientpassportdata.save()


@receiver(post_save, sender=Client)
def update_cars(sender: Client, instance: Client, **kwargs):
    for car in instance.car.all():
        car.is_free = False
        car.save()


@receiver(pre_save, sender=Order)
def calculate_total_price(sender: Order, instance: Order, **kwargs):
    instance.total_price = instance.days_to_use * instance.car.price


@receiver(post_save, sender=Order)
def update_user_cars(sender: Order, instance: Order, **kwargs):
    if not instance.closed:
        instance.client.car.add(instance.car)
        instance.client.save()
    else:
        instance.client.car.remove(instance.car)
        instance.car.is_free = True
        instance.car.save()





