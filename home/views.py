from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .models import *
from .forms import EmployeeForm 
from datetime import date, time
from django.core.exceptions import ValidationError

def loginPage(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

    if not (username and password):
        return render(request, 'login.html', {'error_message': "Both username and password are required."})

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'home.html')
    else:
        return render(request, 'login.html', {'error_message': "Invalid credentials."})
    return render(request, 'login.html')

def sign_up(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            full_name = request.POST['full_name']
            phone_number = request.POST['phone_number']
            address = request.POST['address']
            age = request.POST['age']
            pin_code = request.POST['pin_code']

            # Validate data here if needed

            # Create user with provided information
            user = User.objects.create_user(
                username=username,
                password=password,
                full_name=full_name,
                phone_number=phone_number,
                address=address,
                age=age,
                pin_code=pin_code
            )

            # You can perform additional actions after user creation if needed

            return render(request, 'home.html')

        except ValidationError as e:
            # Handle validation errors
            error_message = f"Validation error: {str(e)}"
            return render(request, 'signup.html', {'error_message': error_message})

        except Exception as e:
            # Handle other exceptions, you can log the error for debugging purposes
            error_message = f"An error occurred: {str(e)}"
            return render(request, 'signup.html', {'error_message': error_message})

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

        return render(request, 'appointment.html', {'appointment': appointment})
    else:
        # Redirect to login page if the user is not authenticated
        return redirect('login')

