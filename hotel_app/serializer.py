from rest_framework import fields, serializers
from .models import Guest, Room , Booking


class GuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guest
        fields = ("name", "age", "phone", "email")


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("room_no", "price", "is_booked")


class BookingSerializer(serializers.ModelSerializer):
    guest = GuestSerializer
    room = RoomSerializer
    class Meta:
        model = Booking
        fields = ("guest", "room", "checkin_date", "checkout_date", "charge",)
