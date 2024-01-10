from django.urls import path,include
from .views import *
urlpatterns = [
    path('',ListE1),
    path('add/',postE1),
    path('update/<int:job_id>/',putE1 ),
    path('delete/<int:job_id>/', DeleteE1),
]