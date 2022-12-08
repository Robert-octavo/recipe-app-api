"""
URL mapping for the user API.
"""
from django.urls import path
from user import views

# use to reverse mapping in the test_user_api
app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
]