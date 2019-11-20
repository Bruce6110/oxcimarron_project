from django.urls import path


from . import views

  #note, the include() function in the project urls file prepends "reading" to these patterns
urlpatterns = [
    path('git',views.git,name='git'),
     path('',views.git,name='techstuff'),


]