from django.urls import path

from practiceapp import views

app_name = 'practiceapp'

urlpatterns = [
    path('upload/', views.upload, name='upload')
]
