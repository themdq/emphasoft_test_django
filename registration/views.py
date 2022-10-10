from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from hotel_app.models import Booking

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

class BookingList(ListView):
    model = Booking
    template_name = 'registration/profile.html'
    def get_queryset(self):
        query = Booking.objects.filter(guest__user__username=self.request.user)
        for item in query:
            print(item.checkin_date)
        return query

