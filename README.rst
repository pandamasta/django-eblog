=====
django-eblog
=====

        [ !! APP NOT FINISHED TO BE USED AS EXPECTED !! ]
     [ !! README WILL BE UPDATED WHEN ALL WILL BE READY !! ]


django-eblog is a simple blog system.


Quick start
-----------


1. Add eblog to your INSTALLED_APPS setting like this

      INSTALLED_APPS = (
          'eblog', 
      )

2. Include the eblog URLconf in your project urls.py like this:

      url(r'^eblog/', include('eblog.urls')),
