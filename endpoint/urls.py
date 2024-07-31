from django.urls import path
from api.views import show

urlpatterns = [
    path('show/', show, name='show'),
]