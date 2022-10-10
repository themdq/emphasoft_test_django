from django.urls import path
from front import views
from .views import SearchResultsView, AllRooms, book, cancel_book
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('look/', AllRooms.as_view(), name='look_results'),
    path('book/', book, name='book'),
    path('cancel/', cancel_book, name='cancel')

]
