from django.urls import path
from . import views 


app_name = 'netflix'



urlpatterns = [
    path('' , views.home , name='home'),
]
