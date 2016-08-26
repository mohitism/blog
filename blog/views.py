from django.shortcuts import render
from blog.models import Post

# Create your views here.

def tagpage(request,tag) :
	posts = Post.objects.filter(tags__name=tag)
	return render(request,"blog/tagpage.html",{"posts":posts,"tag":tag})
