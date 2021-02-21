from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request,'index.html')


def login_user(request):
    return render(request, 'ercp_admin/login.html')


def logout_user(request):
    logout(request)
    return redirect(login_user)


@login_required(login_url='/login/')
def option(request):
    return render(request, 'ercp_admin/option.html')


@login_required(login_url='/login/')
def card_form(request):
    return render(request, 'ercp_admin/formCard.html')


@login_required(login_url='/login/')
def add_card(request):

    if request.method == 'POST':

        own_name = request.POST.get('own_name')
        fathers_name = request.POST.get('fathers_name')
        surname = request.POST.get('surname')
        name = own_name+" "+fathers_name+" "+surname
        category = request.POST.get('category')
        academic_class = request.POST.get('academic_class')
        roll_no = request.POST.get('roll_no')
        div = request.POST.get('div')
        dob = request.POST.get('dob')
        years = request.POST.get('years')
        months = request.POST.get('months')
        addr = request.POST.get('addr')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        taluka = request.POST.get('taluka')
        district = request.POST.get('district')
        state = request.POST.get('state')
        railway_line = request.POST.get('railway_line')
        jour_from = request.POST.get('jour_from')
        jour_to = request.POST.get('jour_to')
        via = request.POST.get('via',None)

        CardDetail.objects.create(user_id=request.user, user_name=name, category=category, academic_class=academic_class, roll_no=roll_no, division=div, date_of_birth=dob, years=years, months=months, residential_addr=addr, city=city, zip_code=zip_code, taluka=taluka, district=district, state=state, journey_from=jour_from, journey_to=jour_to, via=via,railway_line=railway_line)

        return redirect(student_card)


@login_required(login_url='/login/')
def student_card(request):
    return render(request, 'ercp_admin/card.html')

        
@login_required(login_url='/login/')
def concession_form(request):

    # ucard = CardDetail.objects.()
    return render(request, 'ercp_admin/formConcession.html')


@login_required(login_url='/login/')
def add_concession(request):

    if request.method == 'POST':

        railway_class = request.POST.get('railway_class')
        duration = request.POST.get('duration')
        issue_date = request.POST.get('issue_date')

        FormDetail.objects.create(railway_class=railway_class, duration=duration, issue_date=issue_date)
        return redirect(student_concession)


@login_required(login_url='/login/')
def student_concession(request):
    return render(request, 'ercp_admin/concession.html')


def authenticate_user(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect(option)
        else:
            return render(request, "ercp_admin/login.html", {"error": "Invalid Credentials"})

    return render(request, "ercp_admin/login.html")