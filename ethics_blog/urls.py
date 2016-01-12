from django.conf.urls import url, include
from django.contrib import admin
from blog import views as blogViews

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.viewBlog', name='home'),
    url(r'^viewPost/([0-9]+)$', 'blog.views.viewPost', name='post'),
    url(r'^add_comment/([0-9]+)$', 'blog.views.addComment', name='addComment'),
    url(r'^feed$', blogViews.rssFeed()),
]
