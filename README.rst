=====
django-eblog
=====

        [ !! APP NOT FINISHED TO BE USED AS EXPECTED !! ]
     [ !! README WILL BE UPDATED WHEN ALL WILL BE READY !! ]


django-eblog is a simple blog system.


Quick start
-----------


1. Add the app eblog + django-summernote to your INSTALLED_APPS  in settings.py: 

      INSTALLED_APPS = (
          'eblog', 
          'django_summernote',
      )

2. Include the eblog URLconf in your project urls.py like this:

      url(r'^eblog/', include('eblog.urls')),
      url(r'^summernote/', include('django_summernote.urls')),
