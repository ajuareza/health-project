from django.conf.urls import url, include
from . import views

app_name= 'myapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pic/(?P<c>[a-z])/$', views.pic, name='pic_col'),
    url(r'^pic/$', views.pic, name='pic'),
    #url(r'^form/$', views.form, name = "form"),
]
