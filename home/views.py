from django.shortcuts import render, redirect, get_object_or_404
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
        return render(request, 'home.html', {'user_name':username})
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

            return render(request, 'home.html', {'user_name':'username'})

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

# to display services page
def services(request):
    if request.method == 'GET':
        category = Category.objects.all()
        services = Service.objects.all()
        # services = Service.objects.all()
        return render(request, 'services.html',{
            'category': category,
            'services': services
        })

# def workers_profile(request, service_id):
#     if request.method == 'GET':
#         employees = Employee.objects.all()
#         print(employees)
#         return render(request, 'workerprofS3.html', {
#             'employees': employees
#             })
    
def workers_profile(request, service_id):
    if request.method == 'GET':
        print("service id = ")
        print(service_id)
        # Retrieve the service using the service_id, or return a 404 response if not found
        service = get_object_or_404(Service, ServiceID=service_id)
        

        # Retrieve all employees associated with the service
        # employees = Employee.objects.filter(ServiceID=service)
        employees = Employee.objects.all()
        return render(request, 'workerprofS3.html',  {
             'employees': employees,
              'service_id': service_id
                })
    
def service_details(request, service_id):
    if request.method == 'GET':
        print("service id = ")
        print(service_id)
        # Retrieve the service using the service_id, or return a 404 response if not found
        service = get_object_or_404(Service, ServiceID=service_id)
        service_name = service.ServiceName
        service_details = service.Description
        short_description = service.ShortDescription

        # Retrieve all employees associated with the service
        # employees = Employee.objects.filter(ServiceID=service)
        employees = Employee.objects.all()
        
        return render(request, 'service_details.html',  {
              'service_id': service_id,
              'service_name': service_name,
              'short_description': short_description,
              'service_discription': service_details,
                })

def appointment(request, service_id, employee_id):
    service = get_object_or_404(Service, ServiceID=service_id)
    service_name = service.ServiceName
    employee = get_object_or_404(Employee, EmployeeID=employee_id)
    employee_name = employee.Employee_name
            

    if request.method == 'GET':
        # Retrieve the service using the service_id, or return a 404 response if not found
        print(f"service id = {service_id}")
        print(f"employee id = {employee_id}")
        print(f"service name = {service_name}")
        return render(request, 'appointment.html', {
            'employee_name': employee_name,
            'service_name': service_name,
            'service_id': service_id,
            'employee_id': employee_id,
        })
            
def success(request, service_id, employee_id):
    print(f"service id = {service_id} and employee id = {employee_id}")
    service = get_object_or_404(Service, ServiceID=service_id)
    service_name = service.ServiceName
    employee = get_object_or_404(Employee, EmployeeID=employee_id)
    employee_name = employee.Employee_name
    if request.method == 'GET':
        # Retrieve the service using the service_id, or return a 404 response if not found
        print(f"service id = {service_id}")
        return render(request, 'success.html')
    if request.method == 'POST':
        try:
            address1 = request.POST['Address1']
            address2 = request.POST['Address2']
            appntmnt_date = request.POST['Appointment_date']
            state = request.POST['State']
            country = request.POST['Country']
            city = request.POST['City']
            pincode = request.POST['Pincode']

            
            user = request.user
            service = Service.objects.get(ServiceID=service_id)

            # Assuming you want to book the service for the current date and time
            appointment_date = date.today()
            appointment_time = time()

            location = Location.objects.create(
                # locationId = ,
                address1 = address1,
                address2 = address2,
                state = state,
                country = country,
                city = city,
                postcode = pincode 
            )

            employee = get_object_or_404(Employee, EmployeeID=employee_id)
            appointment = Appointment.objects.create(
                UserID=user,
                EmployeeID=employee, 
                ServiceID=service,
                locationId = location,
                ServiceDate = appntmnt_date,
                AppointmentDate=appointment_date,
                AppointmentTime=appointment_time
            )
            print(f"service name = {service_name}")
            return render(request, 'success.html',{
                'service_name':service_name,
                'date':appntmnt_date
             })

        except ValidationError as e:
            # Handle validation errors
            error_message = f"Validation error: {str(e)}"
            print(error_message)
            return render(request, 'appointment.html', {
                'employee_name': employee_name,
                'service_name': service_name,
                'service_id': service_id,
                'employee_id': employee_id,
            })

        # except Exception as e:
        #     # Handle other exceptions, you can log the error for debugging purposes
        #     print(f"service id = {service_id} and employee id = {employee_id}")
        #     error_message = f"An error occurred: {str(e)}"
        #     print(error_message)
        #     return render(request, 'appointment.html', {
        #         'service_id': service_id,
        #         'employee_id': employee_id,
        #     })

    return render(request, 'appointment.html', {
                'employee_name': employee_name,
                'service_name': service_name,
                'service_id': service_id,
                'employee_id': employee_id,
            })


def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    