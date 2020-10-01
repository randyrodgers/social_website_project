from django.urls import path
from . import views

urlpatterns = [
    # POST views
    path( 'login/', views.user_login, name = 'login' ),
]
