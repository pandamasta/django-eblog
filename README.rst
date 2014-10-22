=====
django-eblog
=====

        [ !! APP NOT FINISHED TO BE USED AS EXPECTED !! ]
     [ !! README WILL BE UPDATED WHEN ALL WILL BE READY !! ]


django-eblog is a simple blog system.


Quick start
-----------

1.1 Install django-wysiwyg-redactor:

    pip install django-wysiwyg-redactor

1.2 Add the app eblog + django-redactor to your INSTALLED_APPS  in settings.py: 

      INSTALLED_APPS = (
          'eblog', 
          'django_summernote',
      )

2. Add default config in settings.py

    REDACTOR_OPTIONS = {'lang': 'en'}
    REDACTOR_UPLOAD = 'uploads/'

3. Include the eblog URLconf in your project urls.py like this:

      url(r'^eblog/', include('eblog.urls')),
      url(r'^redactor/', include('redactor.urls')))



