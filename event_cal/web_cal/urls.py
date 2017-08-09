from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.presentations, name='presentations'),
        url(r'^lasershows$', views.laser_shows, name='lasershows'),
        url(r'^djsets$', views.dj_sets, name='djsets'),
]

