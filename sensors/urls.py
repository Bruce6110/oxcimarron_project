from django.urls import path


from . import views

  #note, the include() function in the project urls file prepends "reading" to these patterns
urlpatterns = [
    path('compass',views.compass,name='compass'),
    path('gravity',views.gravity,name='gravity'),
    path('cooking',views.cooking,name='cooking'),
    path('speech_recognition',views.speech_recognition,name='speech_recognition'),
    path('speech_synthesis',views.speech_synthesis,name='speech_synthesis'),


]