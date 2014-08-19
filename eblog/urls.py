from django.conf.urls import *
from django.views.generic import TemplateView
from blog.views import *
from blog.models import Entry
from blog.models import Category


urlpatterns = patterns('',
    url(r'^(?P<year>\d{4})/$', YearsView.as_view(), name="blog_years"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', MonthView.as_view(), name="blog_archive_month"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', DayView.as_view(), name="blog_archive_day"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[\w-]+)/$',DetailView.as_view(), name="blog_detail"),
    url(r'^category/(?P<slug>[\w-]+)/$', CategoryView.as_view(), name="blog_category_detail"),
    url(r'^$', ArchiveView.as_view(), name="blog_archive"),
    );

