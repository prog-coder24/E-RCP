from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('login/', login_user),
    path('success/', authenticate_user),
    path('option/',option),
    path('cardForm/',card_form),
    path('concessionForm/',concession_form),
    path('logout/', logout_user),
]