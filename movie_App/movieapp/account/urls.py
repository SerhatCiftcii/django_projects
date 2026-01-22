from . import views
from django.urls import path


urlpatterns = [
    path("login", views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path("change_password", views.change_password, name="change_password"),
    path("logout", views.logout_request, name="logout"),
    path("change_password", views.change_password, name="change_password"),
    path("profile", views.profile, name="profile"),
    path("watch_list", views.watch_list, name="watch_list")
   

    
]
