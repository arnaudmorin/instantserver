# instantserver
Create Instant Server for developpers using OpenStack API

## How to use
### Install & create a django project
This is a django application, so you should already have create a django project (see: https://docs.djangoproject.com/en/1.7/intro/tutorial01/). 

### Configure the project
Then you must configure your project to redirect every request to this application by modifying your projects' urls.py like this:

```python
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('instantserver.urls', namespace="instantserver")),
)

```

### Database
To let django build your database, just run:

```bash
python3 manage.py migrate
```

## Run

```bash
python3 manage.py runserver
```

The browse it with through http://127.0.0.1:8000/

