# from django.urls import path
# from accounts import views
# urlpatterns = [
#     path('', views.index,name='index'),
#     path('user_register/', views.user_register,name='user_register'),
#     path('register_restaurant/', views.register_restaurant,name='register_restaurant'),
# ]

from django.urls import path
from accounts import views

urlpatterns = [
    path("",views.index),
    path("RegResturant",views.registerResturant,name='RegResturant'),
    path('userreg',views.userRegister,name='userreg'),
]