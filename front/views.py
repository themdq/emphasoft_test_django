# hello_django/calc/views.py
from django.shortcuts import render
from django.template import loader
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from itertools import chain
from django.core.cache import cache


def index(request):
    return render(request, 'front/home.html')


from django.views.generic import ListView
from hotel_app.models import Room, Booking

class SearchResultsView(ListView):
    model = Room
    template_name = 'front/search_results.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        checkin = self.request.GET.get('checkin')
        checkout = self.request.GET.get('checkout')
        cache.set('checkout', checkout)
        cache.set('checkin', checkin)
        cache.set('num', query)
        # case 1: a room is booked before the check_in date, and checks out after the requested check_in date
        case_1 = Booking.objects.filter(checkin_date__lte=checkin, checkout_date__gte=checkin)

        # case 2: a room is booked before the requested check_out date and check_out date is after requested check_out date
        case_2 = Booking.objects.filter(checkin_date__lte=checkout, checkout_date__gte=checkout)

        case_3 = Booking.objects.filter(checkin_date__gte=checkin, checkout_date__lte=checkout)
        result = list(chain(case_3,case_2,case_1))
        booked_rooms = []
        for item in result:
            if str(item.room) not in booked_rooms:
                booked_rooms.append(str(item.room))

        return (Room.objects.filter(
            Q(is_booked__icontains=False,room_size__icontains=query)&~Q(room_no__in=booked_rooms)
        ))

class AllRooms(ListView):
    model = Room
    template_name = 'front/look_results.html'
    def get_ordering(self):
        ordering = self.request.GET.get('orderby')
        return ordering

def book(request):
    checkin = cache.get('checkin')
    num = cache.get('num')
    checkout = cache.get('checkout')
    cache.delete('checkin')
    cache.delete('checkout')
    cache.delete('num')
    print(request.user)
    #Booking.objects.create(guest='Dmitriy')
    return render(request, 'front/home.html')