from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from users.models import Extend, StudentExtend
from users.models import Profile, Extend, StudentExtend
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    user = get_object_or_404(User, username=request.user.username)
    user_id = user.id
    extend = get_object_or_404(Extend, user_id=user_id)
    context={}
    if extend.tag == "teacher":
        context.update({'posts':Post.objects.filter(instructor=user)})
    else:
        stud_extend = get_object_or_404(StudentExtend, user_id=user_id)
        context.update({'posts':Post.objects.filter(section=stud_extend.section)})
    return render(request, 'blog/home.html', context)

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        user_id = user.id
        extend = get_object_or_404(Extend, user_id=user_id)
        if extend.tag == "teacher":
            return Post.objects.filter(instructor=user)
        else:
            stud_extend = get_object_or_404(StudentExtend, user_id=user_id)
            return Post.objects.filter(section=stud_extend.section)

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['subject', 'section']

    def form_valid(self, form):
        form.instance.instructor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.extend.tag == "teacher":
            return True
        return False

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['subject', 'section']

    def form_valid(self, form):
        form.instance.instructor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.instructor:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.instructor:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
