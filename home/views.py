from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from .models import *
from .forms import SignUpForm, EmployeeForm   # Assuming you have a SignUpForm defined
from datetime import date, time

def loginPage(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not (username and password):
            return render(request, 'login.html', {'error_message': "Both username and password are required."})

        user = User.objects.filter(username=username).first()
        if not user or not check_password(password, user.password):
            return render(request, 'login.html', {'error_message': "Invalid credentials."})

        # Perform the login action here (e.g., set a session variable, log the user in)
        return render(request, 'home.html')

    return render(request, 'login.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request,'services.html')
        else:
           
            return render(request,'services.html')
    return render(request, 'signup.html')

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        print(form)
        if form.is_valid():
            print("form is valid")
            form.save()
            # Redirect to 'home.html' after successful form submission
            return render(request, 'home.html')
        else:
            print("form is not valid")
            # Handle the case where the form is not valid
            return render(request, 'signup.html', {'form': form})

    # Handle the case when the request method is not POST
    form = EmployeeForm()
    return render(request, 'register_tmp.html', {'form': form})

def book_service(request, service_id):
    if request.user.is_authenticated:
        user = request.user
        service = Service.objects.get(ServiceID=service_id)

        # Assuming you want to book the service for the current date and time
        appointment_date = date.today()
        appointment_time = time()

        appointment = Appointment.objects.create(
            UserID=user,
            ServiceID=service,
            AppointmentDate=appointment_date,
            AppointmentTime=appointment_time
        )

        # You can add additional logic here if needed

        return render(request, 'success.html', {'appointment': appointment})
    else:
        # Redirect to login page if the user is not authenticated
        return redirect('login')

