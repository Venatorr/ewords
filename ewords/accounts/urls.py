from . import views
from django.urls import path, include

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register_view, name="register")
]