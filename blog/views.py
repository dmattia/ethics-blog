from django.shortcuts import render
from blog.models import Blog, Comment
from blog.forms import CommentForm
from django.contrib.syndication.views import Feed

def viewBlog(request):
	params = {
		'blogs': Blog.objects.order_by('-id') # Order by decreasing id
	}
	return render(request, 'blogs.html', params)

def viewPost(request, postId):
	post = Blog.objects.get(id=postId)
	params = {
		'post': post,
		'comments': Comment.objects.filter(post=post),
		'form': CommentForm()
	}
	return render(request, 'post.html', params)

def addComment(request, postId):
	print "Add comment url visited"
	if request.method == 'POST':
		print "Post request received"
		form = CommentForm(request.POST)
		if form.is_valid():
			newComment = Comment()
			newComment.post = Blog.objects.get(id=postId)		
			newComment.body = form.cleaned_data['body']
			newComment.created_by = form.cleaned_data['created_by']
			newComment.save()
			print "Comment saved"
		else:
			print form.errors
	return viewPost(request, postId)

class rssFeed(Feed):
	title = 'David Mattia\'s ethics blog'
	link = '/'
	
	def items(self):
		return Blog.objects.all()

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.body
