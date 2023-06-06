# task.urls.py

from django.urls import path
from generateTranscript import views
 
urlpatterns = [
    path('generateTranscript/',views.generateTranscript, name='generateTranscript'),
]