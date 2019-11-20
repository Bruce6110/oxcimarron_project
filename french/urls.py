from django.urls import path


from . import views

  #note, the include() function in the project urls file prepends "reading" to these patterns
urlpatterns = [
    path('exercises',views.exercises,name='exercises'),
    path('',views.home,name='french'),

]