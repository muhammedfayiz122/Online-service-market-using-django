from django.urls import path, include
from .views import *
from django.views.generic.base import TemplateView


urlpatterns = [
    path('login/', loginPage, name='login'),
    path('services/', services, name='services'),
    # path('workers/', workers, name='workers'),
    path('workers_profile/<int:service_id>/', workers_profile, name='workers_profile'),
    path('serviceDetails/<int:service_id>/', service_details, name='service_details'),
    path('appointment/<int:service_id>/<int:employee_id>/', appointment, name='appointment'),
    path('success/<int:service_id>/<int:employee_id>/', success, name='success'),
    path('signup/', sign_up, name='signup'),
    path('create_employee/', create_employee, name='create_employee'),
    path('book_service/<int:service_id>/', book_service, name='book_service'),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("", home, name='Gohome'),
]