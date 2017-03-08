from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^vad-finns-gjomt-i-koden/$', views.VadFinnsGjomtIKoden.as_view(), name='vad-finns-gjomt-i-koden'),
    url(r'^matematik/$', views.Matematik.as_view(), name='matematik'),
    url(r'^274877906944/$', views.Kryptering.as_view(), name='kryptering'),
    url(r'^networking/$', views.TheEnd.as_view(), name='the-end'),
]
