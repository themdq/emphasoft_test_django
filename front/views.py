# hello_django/calc/views.py
from django.shortcuts import render
from django.template import loader
from django.db.models import Q
def index(request):
    return render(request, 'front/home.html')


from django.views.generic import ListView

from hotel_app.models import Room

class SearchResultsView(ListView):
    model = Room
    paginate_by = 12
    template_name = 'front/search_results.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        return (Room.objects.filter(
            Q(is_booked__icontains=False,room_size__icontains=query)
        ))

class AllRooms(ListView):
    model = Room
    paginate_by = 12
    template_name = 'front/search_results.html'
    def get_ordering(self):
        ordering = self.request.GET.get('orderby')
        return ordering