from django.contrib import admin
from django.urls import path
from malumot.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fan/', fanlar),
    path('fan/<int:pk>/tahrirlash/', fan_tahrirlash),
    path('yonalish/', yonalishlar),
    path('yonalish/<int:pk>/tahrirlash/', yonalish_tahrirlash),
    path('ustoz/', ustozlar),
    path('ustoz/<int:pk>/tahrirlash/', ustoz_tahrirlash),

]
