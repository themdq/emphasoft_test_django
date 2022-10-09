from django.urls import path
from front import views
from .views import SearchResultsView,AllRooms
urlpatterns = [
    path('', views.index,name = 'index'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('look/', AllRooms.as_view(), name = 'look_results'),
]