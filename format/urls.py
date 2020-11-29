from django.urls import path
from format import views

app_name = 'format'

urlpatterns = [
    path('', views.format_docx, name='format')
]