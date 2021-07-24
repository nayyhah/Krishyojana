from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
)
from .models import Post
from users.views import cart_list

# Create your views here.
def home(request):
	return render(request, 'krishyojana/home.html')



def schemes(request):
	return render(request, 'krishyojana/schemes.html')



def emarket(request):
	posts = Post.objects.all()

	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'krishyojana/emarket.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'krishyojana/emarket.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 10

class UserPostListView(ListView):
	model = Post
	template_name = 'krishyojana/user_post.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 10

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


class ProfileDetailView(DetailView):
	model = Post
	template_name = 'krishyojana/profile_detail.html' # <app>/<model>_<viewtype>.html

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['crop_name', 'image', 'harvest_time', 'rate', 'amount_left']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['crop_name', 'image', 'harvest_time', 'rate', 'amount_left']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = "/krishyojana/emarket"

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False




def msp(request):
	return render(request, 'krishyojana/msp.html')