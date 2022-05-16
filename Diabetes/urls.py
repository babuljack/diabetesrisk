from django.contrib import admin
from django.urls import path
from Calculate.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index.as_view()),
    path('Dcal',DiabetesCalculate.as_view(),name='DiabetesCalculate'),
]
