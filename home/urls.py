from django.urls import path, include
from .views import *


urlpatterns = [
    path('login/', loginPage, name='login'),
    path('signup/', sign_up, name='signup'),
    path('create_employee/', create_employee, name='create_employee'),
    path('book_service/<int:service_id>/', book_service, name='book_service'),
]