from django.urls import path
from .views import HomePageView
from .views import AboutPageView
from .views import skidays_by_resort, skidays_by_year, skistats_by_trip
from .views import SkiDayListView, SkiDayUpdateView, SkiDayCreateView, SkiDayDeleteView, ResortListView,    ResortUpdateView, ResortCreateView, ResortDeleteView


# note, the include() function in the project urls file prepends "reading" to these patterns
urlpatterns = [
    path('', SkiDayListView.as_view(), name='skiday-list'),
    path('about/', AboutPageView.as_view(), name='skiing-about'),
    path('skiday-list/', SkiDayListView.as_view(), name='skiday-list'),
    path('skiday/<int:pk>/update',
         SkiDayUpdateView.as_view(),  name='skiday-update'),
    path('skiday/<int:pk>/delete',
         SkiDayDeleteView.as_view(),  name='skiday-delete'),
    path('skiday/new/', SkiDayCreateView.as_view(), name='skiday-create'),
    path('resort-list/', ResortListView.as_view(), name='resort-list'),
    path('resort/<int:pk>/update',
         ResortUpdateView.as_view(),  name='resort-update'),
    path('resort/<int:pk>/delete',
         ResortDeleteView.as_view(),  name='resort-delete'),
    path('resort/new/', ResortCreateView.as_view(), name='resort-create'),
    path('skidays-by-resort', skidays_by_resort, name='skidays-by-resort'),
    path('skidays-by-year', skidays_by_year, name='skidays-by-year'),
    path('skistats-by-trip', skistats_by_trip, name='skistats-by-trip'),
    # Note: The name attrib is what the {% url %} tag needs


    # path('ski_days_by_year',views.ski_days_by_year,name='ski_days_by_year'),
    # path('ski_days_by_resort',views.ski_days_by_resort,name='ski_days_by_resort'),
    # path('',views.home,name='ski_days'),
    # path('<int:blog_id>/',views.detail,name='detail'),

]
