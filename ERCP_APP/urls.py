from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('login/', login_user),
    path('success/', authenticate_user),
    path('option/',option),
    path('logout/', logout_user),
]