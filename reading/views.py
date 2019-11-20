from django.shortcuts import render

from django.db import connection
from .models import Book
from .models import Author
from decimal import Decimal
from django.contrib.auth.models import User, Group

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from oxcimarron.utils import Utils


from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
import logging
login_url = '/users/login'


def pages_by_year(request):

    cur = connection.cursor()

    sql = "select year_read,(sum(standard_pages)) standard_pages,\
    round(cast(case when date_part('year',current_date)=year_read then sum(standard_pages)/extract(DOY FROM current_date) else \
    sum(standard_pages)/365.25 end as numeric),1) as pages_per_day,\
    count(id) books, round(avg(enjoyment),1) avg_enjoyment , \
    case when year_read=date_part('year',current_date) then round(sum(standard_pages)/(extract(DOY FROM current_date)/365.25))\
    else null end as pace \
    from reading_book \
    group by year_read order by sum(standard_pages) desc"
    cur.execute(sql)
    rows = cur.fetchall()
    total = 0
    for row in rows:
        total += row[1]
    # conn.commit()
    avg = Decimal(total/len(rows))
    avg = round(avg/10)*10

    cur.close()
    # conn.close()

    return render(request, 'reading/pages_by_year.html', {'rows': rows, 'page_title': 'Pages by Year', 'total': total, 'avg': avg})


# shows a simple book list
def home(request):
    # print("\n------STARTED ITERATING LOCALS-----------------------\n")
    # for field, possible_values in locals().items():
    #     print(field, possible_values)
    # print("\n------FINISHED-----------------------\n")

    cur = connection.cursor()
    sql = "SELECT b.id, b.title, a.first_name, a.last_name,\
         year_written, year_read, category, subcategory, standard_pages, enjoyment,\
         a.id author_id\
         FROM    reading_book b \
         LEFT outer join reading_author a on b.author_id=a.id \
        order by title,year_read  "
    cur.execute(sql)
    # Note: cur.fetchall() returns a list of tuples.  Each row is a tuple of values.
    books = cur.fetchall()
    # print(rows[0][2])  #Test: print the 3rd item of the first
    #Utils.printDictionary(globals(), 'Globals')
    print("am i here?")
    #Utils.printDictionary(locals(), 'Locals')

    return render(request, 'reading/home.html', {'books': books})

# Class-based view


class AuthorListView(ListView):  # inherit from Django's ListView
    model = Author
    fields = ['last_name', 'first_name', 'country_of_origin',
              'birth_year', 'death_year', 'picture']

    def get_context_data(self, *args, **kwargs):
        context = super(AuthorListView, self).get_context_data(
            *args, **kwargs)
        context["page_title"] = "Authors List"
        return context


# Class-based view
# inherit from Django's CreateView

class BookCreateView(LoginRequiredMixin, CreateView):
    login_url = '/users/login'
    model = Book
    fields = ['title', 'year_written', 'category', 'author',
              'subcategory', 'year_read', 'standard_pages', 'enjoyment']

    def get_context_data(self, *args, **kwargs):
        context = super(BookCreateView, self).get_context_data(
            *args, **kwargs)
        context["page_title"] = "Add New Book"
        return context

    # overrides default in CreateView

    def form_valid(self, form):
        # do whatever else here:
        print("I'm in BookCreateView.form_valid()")

        # then:
        return super().form_valid(form)


# Class-based view
# inherit from Django's CreateView
class BookUpdateView(LoginRequiredMixin,  UpdateView):
    login_url = '/users/login'
    model = Book
    fields = ['title', 'year_written', 'category', 'author',
              'subcategory', 'year_read', 'standard_pages', 'enjoyment']

    def get_context_data(self, *args, **kwargs):
        context = super(BookUpdateView, self).get_context_data(
            *args, **kwargs)
        context["page_title"] = "Book Detail"
        return context

    def form_valid(self, form):
        # do whatever else here:
        print("I'm in BookUpdateView.form_valid()")

        # then:
        return super().form_valid(form)


class BookDeleteView(LoginRequiredMixin, DeleteView):  # inherit from Django's DeleteView
    model = Book

    def get_context_data(self, *args, **kwargs):
        context = super(BookDeleteView, self).get_context_data(
            *args, **kwargs)
        context["page_title"] = "Delete Book"
        return context

    # currently, book list view is the default reading view
    success_url = '/reading'  # 'success_url' is for when you want to redirect upon success

# inherit from Django's DeleteView


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author

    success_url = '/reading/authors' #ie, go to authors list upon delete

    def get_context_data(self, *args, **kwargs):
        context = super(AuthorDeleteView, self).get_context_data(
            *args, **kwargs)
        context["page_title"] = "Delete Author"
        return context


# Class-based view
# inherit from Django's CreateView
class AuthorCreateView(LoginRequiredMixin, CreateView):
    login_url = '/users/login'
    model = Author
    fields = ['last_name', 'first_name', 'country_of_origin', 'birth_year',
              'death_year', 'picture']  # fields = ['title', 'year_written', 'category',
    # overrides default in CreateView

    def get_context_data(self, *args, **kwargs):
        context = super(AuthorCreateView, self).get_context_data(
            *args, **kwargs)
        context["page_title"] = "Add New Author"
        return context

    def form_valid(self, form):
        # do whatever else here:
        print("I'm in AuthorCreateView.form_valid()")

        # then:
        return super().form_valid(form)


# Class-based view

# inherit from Django's UpdateView
class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/users/login'

    model = Author
    fields = ['last_name', 'first_name', 'country_of_origin', 'birth_year',
              'death_year', 'picture']

    def get_context_data(self, *args, **kwargs):
        context = super(AuthorUpdateView, self).get_context_data(
            *args, **kwargs)
        context["page_title"] = "Author Detail"
        return context

    def form_valid(self, form):
        # do whatever else here:
        print("I'm in AuthorUpdateView.form_valid()")

        # then:
        return super().form_valid(form)

"""     def test_func(self):
        # this method required if you use security mixins?
        book = self.get_object()
        if self.request.user == 'BH':  # not currently functional 9/2019
            return True
        return False
 """

def books_by_year(request):

    cur = connection.cursor()

    sql = "SELECT year_read, b.title, a.last_name, a.first_name, category,\
         subcategory, year_written, standard_pages, enjoyment\
         FROM   reading_book b \
         LEFT outer join reading_author a on b.author_id=a.id \
        order by year_read, b.id  "
    cur.execute(sql)
    rows = cur.fetchall()
   # report = Utils.getAttributeReport(request.GET)
   # report=Utils.getAttributeReport(request)
    report = ""
    cur.close()

    return render(request, 'reading/books_by_year.html', {'test': 'this is a test', 'rows': rows, 'report':     report, 'page_title': 'Books by Year'})
