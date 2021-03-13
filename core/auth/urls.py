from django.urls import path
from . import views

urlpatterns = [
    path('register',views.Registration.as_view(), name='api-register' ),
    path('login',views.LoginView.as_view(), name='api-register' ),
]