from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("profile/<int:user_pk>", views.profile, name="profile"),
    path("update/<int:user_pk>", views.update, name="update"),
    path("delete/", views.delete, name="delete"),
    path("password/<int:user_pk>", views.change_password, name="change_password"),   

]
