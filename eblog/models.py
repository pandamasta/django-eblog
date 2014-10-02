from django.db import models

"""
Models of ``blog`` application.
"""

from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from managers import CategoryOnlineManager
from managers import EntryOnlineManager

from django.core.urlresolvers import reverse


class Category(models.Model):
    """
    A blog category.
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    online_objects = CategoryOnlineManager()

    def __unicode__(self):
         return self.name

    @models.permalink #Deprecated in django 1.6
    def get_absolute_url(self):
        return ('blog_category_detail', (), {
            'slug': self.slug,
        })


    def _get_online_entries(self):
        """
        Returns entries in this category with status of "online".
        Access this through the property ``online_entry_set``.
        """
        from blog.models import Entry
        return self.objects.filter(status=Entry.STATUS_ONLINE)

    online_entry_set = property(_get_online_entries)


class Entry(models.Model):
    """
    A blog entry.
    """
    STATUS_OFFLINE = 0
    STATUS_ONLINE = 1
    STATUS_DEFAULT = STATUS_OFFLINE
    STATUS_CHOICES = (
        (STATUS_OFFLINE, 'Offline'),
        (STATUS_ONLINE, 'Online'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='publication_date')
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    publication_date = models.DateTimeField(default=datetime.now(), db_index=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_DEFAULT, db_index=True)
    body = models.TextField()

    author = models.ForeignKey('auth.User')
    category = models.ForeignKey(Category)

    objects = models.Manager()
    online_objects = EntryOnlineManager()

    def __unicode__(self):
         return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog_detail', (), {
            'year': self.publication_date.strftime('%Y'),
            'month': self.publication_date.strftime('%m'),
            'day': self.publication_date.strftime('%d'),
            'slug': self.slug,
        })
