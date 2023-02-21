import sys
import os
from django.shortcuts import render
from django.db.models import Sum
from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import SkiDay, Resort
from django.contrib.auth.models import User, Group
from django.db import connection
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class HomePageView(TemplateView):
    template_name = 'skiing/home.html'


class AboutPageView(TemplateView):
    template_name = 'skiing/about.html'


class SkiDayListView(ListView):
    model = SkiDay
    template_name = 'skiing/skiday-list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SkiDayListView, self).get_context_data(
            *args, **kwargs)
        context["page_title"] = "Ski Days"
        return context


# inherit from Django's DeleteView
class SkiDayDeleteView(LoginRequiredMixin, DeleteView):
    model = SkiDay
    login_url = '/users/login'

    def get_context_data(self, *args, **kwargs):
        context = super(SkiDayDeleteView, self).get_context_data(
            *args, **kwargs)
        context["page_title"] = "Delete Ski Day"
        return context

    #redirect_field_name = '/skiing/skiday-list'
    # currently, book list view is the default reading view
    success_url = '/skiing/skiday-list'  # ie, go to skiday list upon delete

# Class-based view
# inherit from Django's CreateView


class SkiDayCreateView(LoginRequiredMixin, CreateView):
    login_url = '/users/login'
    #success_url = '/skiing/skiday-list'
    model = SkiDay
    fields = ['skidate', 'trip_no', 'resort',  'miles',
              'vertical_feet', 'top_speed']
    # overrides default in CreateView

    def get_context_data(self, *args, **kwargs):
        context = super(SkiDayCreateView, self).get_context_data(
            *args, **kwargs)
        context["page_title"] = "Add Ski Day"
        return context

    def form_valid(self, form):
        # do whatever else here:

        # then:
        return super().form_valid(form)


class SkiDayUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/users/login'

    model = SkiDay
    fields = ['skidate',  'trip_no', 'resort',  'miles',
              'vertical_feet', 'top_speed', ]

    #success_url = '/skiing/skiday-list'

    def get_context_data(self, *args, **kwargs):
        context = super(SkiDayUpdateView, self).get_context_data(
            *args, **kwargs)
        context["page_title"] = "Ski Day Detail"
        return context

    def form_valid(self, form):
        # do whatever else here:

        # then:
        return super().form_valid(form)

    def test_func(self):
        # happens if you use security mixins

        skiday = self.get_object()
        if self.request.user == 'BH':  # not currently functional 9/2019
            return True
        return False


class ResortListView(ListView):
    model = Resort

    fields = ['resort_name', 'location', 'skiable_acres', 'base_elevation',
              'vertical_feet', 'longest_run', 'personal_rating', 'id']

    # TODO: see how to do this more easily than redefining the method in every CBV
    def get_context_data(self, *args, **kwargs):
        context = super(ResortListView, self).get_context_data(*args, **kwargs)
        context["page_title"] = "Ski Resorts Visited"
        return context

    template_name = 'skiing/resort_list.html'


class ResortUpdateView(LoginRequiredMixin, UpdateView):
   # Note that lack of a trailing slash.  This override was necessary in order to correctly format the full url, eg "/users/login?next=etcetc".
    login_url = '/users/login'

    model = Resort
    fields = ['resort_name', 'location', 'skiable_acres', 'base_elevation',
              'vertical_feet', 'longest_run', 'personal_rating']
    success_url = '/skiing/resort-list'

    def get_context_data(self, *args, **kwargs):

        context = super(ResortUpdateView, self).get_context_data(
            *args, **kwargs)
        context["page_title"] = "Ski Resort Detail"
        return context

    def form_valid(self, form):
        print("In resortupdateview.form_valid()")
        # do whatever else here:

        # then:
        return super().form_valid(form)


class ResortCreateView(LoginRequiredMixin, CreateView):
    login_url = '/users/login'
    fields = ['resort_name', 'location',
              'vertical_feet', 'skiable_acres', 'personal_rating']

    success_url = '/skiing/resort-list'

    model = Resort

    def get_context_data(self, *args, **kwargs):
        context = super(ResortCreateView, self).get_context_data(
            *args, **kwargs)
        context["page_title"] = "Add Ski Resort"
        return context

    # def get_absolute_url(self):
    #    return reverse('resort-update', args=[str(self.id)])

    def form_valid(self, form):
        # do whatever else here:

        # then:
        return super().form_valid(form)


class ResortDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/users/login'
    model = Resort

    #redirect_field_name = '/skiing/resort-list'
    # currently, book list view is the default reading view
    success_url = '/skiing/resort-list'

    def get_context_data(self, *args, **kwargs):
        context = super(ResortDeleteView, self).get_context_data(
            *args, **kwargs)
        context["page_title"] = "Delete Ski Resort"
        return context


def skidays_by_resort(request):

    cur = connection.cursor()

    sql = "select resort_Name, location, count(*), sum(a.vertical_feet),   avg(a.vertical_feet), max(a.vertical_feet),  sum(miles), max(top_speed), resort_id\
        from skiing_skiday a \
        left join skiing_resort b on a.resort_id = b.id \
        group by resort_name, location,resort_id  \
        order by 3 desc, 1"
    cur.execute(sql)
    rows = cur.fetchall()
    total = 0
    for row in rows:
        total += row[2]

    cur.close()
    # conn.close()

    return render(request, 'skiing/skidays_by_resort.html', {'rows': rows, 'page_title': 'Ski Days By Resort', 'total': total})


def skistats_by_trip(request):
    cur = connection.cursor()

    sql = "select trip_no, count(skidate) skidays,  count(distinct resort_id) resorts, min(skidate) startday, max(skidate) endday, 1+max(skidate)-min(skidate) daysintrip, sum(vertical_feet) totalvertical, avg(vertical_feet) averagevertical, sum(miles) totalmiles, max(top_speed) maxspeed from skiing_skiday group by trip_no order by trip_no desc"

    cur.execute(sql)
    rows = cur.fetchall()
    totaldays = 0
    totalvert = 0
    totalmiles = 0
    trackeddays = 0
    
    for row in rows:
        
        totaldays += row[1]
        if row[6]:
            totalvert += row[6]
            trackeddays += row[6]/row[7]
           
        if row[8]:
            totalmiles += row[8]
            
    avgvert = totalvert/trackeddays
    avgmiles=totalmiles/trackeddays
    untrackeddays=totaldays-trackeddays
    estgrandtotalvert = totalvert+(totaldays-trackeddays)*24000
    estgrandtotalmiles = totalmiles+(totaldays-trackeddays)*26
    
    estavgvert=estgrandtotalvert/totaldays
    estavgmiles=estgrandtotalmiles/totaldays
    
    cur.close()
    # conn.close()

    return render(request, 'skiing/skistats_by_trip.html', {'rows': rows, 'page_title': 'Ski Stats by Trip', 'totaldays': totaldays, 'totalmiles': totalmiles, 'totalvert': totalvert, 'trackeddays': trackeddays, 'avgvert': avgvert, 'avgmiles':avgmiles, 'estgrandtotalvert': estgrandtotalvert, 'estgrandtotalmiles': estgrandtotalmiles,'estavgvert':estavgvert,'estavgmiles': estavgmiles,'untrackeddays':untrackeddays})

def skidays_by_year(request):

    cur = connection.cursor()

    sql = "select cast(extract(year from skidate) as INTEGER), count(skidate),\
    count(distinct resort_id) resorts, sum(vertical_feet) totalvertical, avg(vertical_feet) averagevertical, sum(miles) totalmiles, max(top_speed) maxspeed from skiing_skiday group by cast(extract(year from skidate) as INTEGER)  \
    order by 1 desc"
    cur.execute(sql)
    rows = cur.fetchall()
    total = 0
    for row in rows:
        total += row[1]

    cur.close()
    # conn.close()

    return render(request, 'skiing/skidays_by_year.html', {'rows': rows, 'page_title': 'Ski Days By Year', 'total': total})
