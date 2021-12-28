from django.urls import path
from .views import index,login,register,treading,logout,showroom

app_name = 'autoapp'

urlpatterns = [
    path('',index,name = 'index'),
    path('login',login,name = 'login'),
    path('register', register, name='register'),
    path('treading',treading,name = 'treading'),
    path('logout', logout, name='logout'),
    path('showroom', showroom, name='showroom')
]
