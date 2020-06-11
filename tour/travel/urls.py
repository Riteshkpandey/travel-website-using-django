from django.urls import path
from travel import views
from django.views.generic.base import RedirectView
urlpatterns = [
    path('',RedirectView.as_view(url="home/")),
    
    path('home/',views.home),
    path('book_now/',views.book_now),
   
]
