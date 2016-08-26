"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.views.generic import ListView,DetailView
from blog.models import Post
from . import views
import feeds


urlpatterns = [ 
url(r'^$',ListView.as_view(queryset=Post.objects.all().order_by("-created")[:2],template_name="blog/blog.html")),
url(r'^(?P<pk>\d+)$',DetailView.as_view(model=Post,template_name="blog/post.html")),
url(r'^archives/$',ListView.as_view(queryset=Post.objects.all().order_by("-created"),template_name="blog/archives.html")),
url(r'^tag/(?P<tag>\w+)$',views.tagpage,name="tagpage"),
url(r'^feed/$',feeds.BlogFeed()),
]
