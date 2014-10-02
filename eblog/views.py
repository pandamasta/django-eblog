from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DateDetailView, YearArchiveView, MonthArchiveView, DayArchiveView
from eblog.models import *

class ArchiveView(ListView):
    template_name = "eblog/entry_archive.html"
    model = Entry
    context_object_name = 'latest'
    queryset=Entry.online_objects.order_by('-publication_date')


class YearsView(YearArchiveView):
    template_name = "eblog/entry_archive_year.html"
    month_format='%m'
    date_field='publication_date'
    allow_future = True
    queryset=Entry.online_objects.all()
    make_object_list=True
    model = Entry

class MonthView(MonthArchiveView):
    template_name = "eblog/entry_archive_month.html"
    month_format='%m'
    queryset = Entry.online_objects.all()
    date_field = "publication_date"
    make_object_list = True
    allow_future = True

class DayView(DayArchiveView):
    template_name = "eblog/entry_archive_day.html"
    month_format='%m'
    queryset = Entry.online_objects.all()
    date_field = "publication_date"
    make_object_list = True
    allow_future = True

class DetailView(DateDetailView):
    template_name = "eblog/entry_detail.html"
    model = Entry
    context_object_name = 'article'
    month_format='%m'
    date_field='publication_date'
    slug_field='slug'

class CategoryView(ListView):
    template_name = "eblog/category_detail.html"
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['slug'] = self.kwargs['slug']
        context['list_article'] = Entry.online_objects.filter(category__name=self.kwargs['slug'])
        return context
