from django.shortcuts import render

from .models import Post
# Create your views here.
def post_list(request):
	posts=Post.objects.filter(status='published')
	return render(request, 'blog_app/index.html', {'posts':posts})
def post_detail(request, year, month, day, post):
	post=get_object_or_404(Post, slug=post, 
								 status='published',
								 publish_year=year,
								 publish_month=month,
								 publish_day=day)
	return render(request, 'blog_app/post/detail.html', {'post':post})