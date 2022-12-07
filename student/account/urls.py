from django.urls import path
from .import views

urlpatterns = [
    path('', views.mainhome,name='mainhome'),
    path('course',views.course,name='course'),
    path('signup', views.signup,name='signup'),
    path('signin', views.signin,name='signin'),
    path('forgot', views.forgot,name='forgot'),


    

    

    
]
