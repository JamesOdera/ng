from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.album_of_day,name='albumToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_album,name = 'pastAlbum')
]