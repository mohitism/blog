from django.contrib.syndication.views import Feed
from blog.models import Post


class BlogFeed(Feed) :
	title="MySite"	
	description="Some ramblings of mine"
	link="blog/feed/"

	def items(self):
		return Post.objects.all().order_by("-created")[:2]

	def item_title(self,item) :
		return item.title
	def item_description(self,item):
		return item.body
	def item_link(self, item) :
		return u"/blog/%d" % item.id
