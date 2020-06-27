
from django.contrib import admin
from django.urls import path
from adoptions import views
from django.conf.urls import url

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.home, name = 'home'),
    url(r'^adoptions/(\d+)/', views.pet_detail, name = 'pet_detail')
]
