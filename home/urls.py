from django.urls import path, include
from .views import *
from django.views.generic.base import TemplateView


urlpatterns = [
    path('login/', loginPage, name='login'),
    path('signup/', sign_up, name='signup'),
    path('create_employee/', create_employee, name='create_employee'),
    path('book_service/<int:service_id>/', book_service, name='book_service'),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]