from django.conf.urls import url
from django.conf.urls import include
from django.urls import path

from rest_framework import routers

from . import views

#from courses import views

from rest_framework.routers import DefaultRouter



router = routers.DefaultRouter()

router.register('languages', views.LanguageView)
router.register('paradigms', views.ParadigmView)
router.register('programmers', views.ProgrammerView)
#router.register('review-view', views.ReviewViewSet)
#urlpatterns = router.urls




urlpatterns = [


    path('', include(router.urls)),



]