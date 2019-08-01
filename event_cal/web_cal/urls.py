from django.conf.urls import url

from . import views

urlpatterns = [
		url(r'^all$', views.all, name='all'),
        url(r'^$', views.presentations, name='presentations'),
        url(r'^lasershows$', views.laser_shows, name='lasershows'),
        url(r'^djsets$', views.dj_sets, name='djsets'),
        # url(r'^updatedb$', views.update_db, name='updatedb'),
]

