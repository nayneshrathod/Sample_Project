from django.urls import path
from Myblog.views import index

urlpatterns = [
    path('', index),
]
