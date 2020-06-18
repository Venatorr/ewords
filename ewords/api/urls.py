from rest_framework.routers import DefaultRouter
from django.urls.conf import path
from . import views
from rest_framework_jwt.views import (obtain_jwt_token,
    refresh_jwt_token, verify_jwt_token)
from django.conf.urls import url

router = DefaultRouter()
router.register(r'words', views.WordsViewset, basename='word')
router.register(r'languages', views.LanguagesViewset, basename='language')

urlpatterns = router.urls
urlpatterns = [
    path('signup/', views.CreateUserAPIView.as_view()),
    url(r'^obtain-jwt-token/', obtain_jwt_token),
    url(r'^refresh-jwt-token/', refresh_jwt_token),
    url(r'^verify-jwt-token/', verify_jwt_token),
              ] + urlpatterns
