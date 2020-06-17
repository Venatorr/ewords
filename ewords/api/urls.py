from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'words', views.WordsViewset, basename='word')
router.register(r'languages', views.LanguagesViewset, basename='language')

urlpatterns = router.urls
