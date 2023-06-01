from django.urls import path
from .views import IndexView, AboutUs

urlpatterns = [
    # path('endereco/', minhaView.as_view(), name = 'nome-da-url')
    path('',IndexView.as_view(), name='index'),
    path('about_us.html', AboutUs.as_view(), name='about_us' )
]