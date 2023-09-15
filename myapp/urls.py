from django.urls import path
from.import views

urlpatterns = [
    path("", views.index, name="Index"),
    path("signup/",views.SignUp, name="SignUp"),
    path("login/",views.Login, name="Login"),
    path("logout/", views.Logout, name = "Logout"),
]
