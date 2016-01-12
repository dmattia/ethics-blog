from django.shortcuts import render
from blog.models import Blog

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
