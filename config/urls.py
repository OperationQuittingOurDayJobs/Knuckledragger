from django.urls import path, include
from django.contrib import admin

admin.autodiscover()

import knuckledragger.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", knuckledragger.views.index, name="index"),
    path("admin/", admin.site.urls),
]
