from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from datetime import datetime, timedelta 
from .models import *
from .forms import *
from django.utils import timezone

# Create your views here.

def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')


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
    uname = CardDetail.objects.all()
    return render(request, 'ercp_admin/Card/formCard.html',{'uname':uname})


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

        city_source = city.split()
        new_list = []
        for c in city_source:
            new_list.append(c.lower())

        if any(c in jour_from.lower() for c in new_list):
            CardDetail.objects.create(user_id=request.user, user_name=name, category=category, academic_class=academic_class, roll_no=roll_no, division=div, date_of_birth=dob, years=years, months=months, residential_addr=addr, city=city, zip_code=zip_code, taluka=taluka, district=district, state=state, journey_from=jour_from, journey_to=jour_to, via=via,railway_line=railway_line)
            request.user.has_card = True
            request.user.save()
            return redirect(student_card)
        else:
            return render(request, 'ercp_admin/Card/formCard.html', {"warning": "Entered City should match with Source station"} )



@login_required(login_url='/login/')
def student_card(request):

    try:
        card = CardDetail.objects.get(user_id=request.user)
        return render(request, 'ercp_admin/Card/card.html', {'card':card})

    except CardDetail.DoesNotExist:
        return render(request, "ercp_admin/option.html")

    return None



@login_required(login_url='/login/')
def concession_form(request):
    return render(request, 'ercp_admin/Form/formConcession.html')


@login_required(login_url='/login/')
def add_concession(request):

    if request.method == 'POST':

        if not request.user.has_card:
           return render(request, 'ercp_admin/Card/formCard.html')

        railway_class = request.POST.get('railway_class')
        duration = request.POST.get('duration')
        issue_date = request.POST.get('issue_date')
        user_card = CardDetail.objects.get(user_id=request.user)

        date_format = "%Y-%m-%d"
        dt_now = datetime.strptime(str(datetime.now().date()), date_format)
        issue_date_ts = datetime.strptime(str(issue_date), date_format)
        timediff = issue_date_ts - dt_now

        if timediff.days <= 3 and timediff.days > 0:
            FormDetail.objects.create(user_card=user_card, railway_class=railway_class, duration=duration, issue_date=issue_date)
            return redirect(student_concession)
        else:
             return render(request, 'ercp_admin/Form/formConcession.html', {"warning": "Issue date should be between the next 3 days."})



@login_required(login_url='/login/')
def student_concession(request):

      try:
          user_card = CardDetail.objects.get(user_id=request.user)
          concessions = FormDetail.objects.filter(user_card=user_card)
          return render(request, 'ercp_admin/Form/concession.html', {'concessions':concessions})

      except FormDetail.DoesNotExist and CardDetail.DoesNotExist:
          return render(request, "ercp_admin/option.html")

      return None


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