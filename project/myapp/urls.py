from django.urls import path
from .views import *

urlpatterns = [
    path('', users_list),
    path('test/', check_name),
]