from django.shortcuts import render
from blog.models import Blog
from django.contrib.syndication.views import Feed

def viewBlog(request):
	params = {
		'blogs': Blog.objects.order_by('time')
	}
	return render(request, 'blogs.html', params)

def viewPost(request, postId):
	params = {
		'post': Blog.objects.get(id=postId)
	}
	return render(request, 'post.html', params)

class rssFeed(Feed):
	title = 'David Mattia\'s ethics blog'
	link = '/'
	
	def items(self):
		return Blog.objects.all()

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.body
