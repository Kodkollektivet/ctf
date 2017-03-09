from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^M6qLX5eBMhcTKVG2/$', views.VadFinnsGjomtIKoden.as_view(), name='vad-finns-gjomt-i-koden'),
    url(r'^170gNoAXEs1Xwl3B/$', views.Matematik.as_view(), name='matematik'),
    url(r'^ydLaW0X9lIzvsF3m/$', views.Password.as_view(), name='password'),
    url(r'^eeUcfNK0aoYfYRni/$', views.Time.as_view(), name='time'),
    url(r'^7zLKy90bYmm7fr50/$', views.Hash.as_view(), name='hash'),
    url(r'^4mtVd5dm1ptzAkle/$', views.Kryptering.as_view(), name='kryptering'),
    url(r'^GHMDT3GVB0P7a76I/$', views.TheEnd.as_view(), name='the_end'),
]
