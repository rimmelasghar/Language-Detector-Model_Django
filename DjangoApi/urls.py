
from django.urls import path , include
from .views import formView, home
urlpatterns = [
    path('',home,name = 'home'),
    path('form/',formView,name='formview'),
]
