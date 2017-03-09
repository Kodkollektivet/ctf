from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^M6qLX5eBMhcTKVG2/$', views.VadFinnsGjomtIKoden.as_view(), name='vad-finns-gjomt-i-koden'),
    url(r'^170gNoAXEs1Xwl3B/$', views.Matematik.as_view(), name='matematik'),
    url(r'^4mtVd5dm1ptzAkle/$', views.Kryptering.as_view(), name='kryptering'),
    url(r'^GHMDT3GVB0P7a76I/$', views.TheEnd.as_view(), name='networking'),
]
