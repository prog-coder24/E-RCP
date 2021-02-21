from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('login/', login_user),
    path('success/', authenticate_user),
    path('option/',option),
    path('cardForm/',card_form),
    path('add_card/',add_card),
    path('student_card/',student_card),
    path('concessionForm/',concession_form),
    path('add_concession/',add_concession),
    path('student_concession/',student_concession),    
    path('logout/', logout_user),
]