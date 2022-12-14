from datetime import timedelta, datetime
from django.db import models
from datetime import datetime
from registration.models import Profile


class Guest(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Room(models.Model):
    room_no = models.IntegerField(default=101)
    price = models.FloatField(default=1000.0)
    room_size = models.FloatField(default=1)
    is_booked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.room_no)


class Booking(models.Model):
    guest = models.ForeignKey(Profile, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    num_of_guest = models.IntegerField(default=1)
    checkin_date = models.DateField(default=datetime.now)
    checkout_date = models.DateField(default=datetime.now)
    is_checkout = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.guest.user.username

    def charge(self) -> float:
        return self.is_checkout * \
            (self.checkout_date - self.checkin_date + timedelta(1)).days * \
            self.room.price
