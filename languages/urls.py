from django.conf.urls import url
from django.conf.urls import include


from rest_framework import routers

from . import views

#from courses import views

from rest_framework.routers import DefaultRouter

#router = routers.SimpleRouter()
#router.register(r'courses', views.CourseViewSet)
#router.register(r'reviews', views.ReviewViewSet)

router = DefaultRouter()

#router.register('course-view', views.CourseViewSet)
#router.register('review-view', views.ReviewViewSet)
#urlpatterns = router.urls




urlpatterns = [


    url(r'', include(router.urls)),



]