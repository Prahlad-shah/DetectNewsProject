from django.urls import path
from . import views

app_name = 'apiapp'
urlpatterns = [
    path("detect",views.index,name = 'detect'),
]