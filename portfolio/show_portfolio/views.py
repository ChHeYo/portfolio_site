from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import (
    TemplateView, ListView,
    CreateView, DetailView,
    UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.utils import timezone

from .forms import PostForm
from .models import Post
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'base.html'


class DataView(ListView):
    model = Post
    template_name = 'posts/data_post_list.html'
    context_object_name = 'data_post_list'

    def get_queryset(self):
        return Post.objects.filter(
            date_added__lte=timezone.now(), post_type='Data').order_by('-date_added')


class PyJavaView(ListView):
    model = Post
    template_name = 'posts/pyjava_post_list.html'
    context_object_name = 'pyjava_post_list'

    def get_queryset(self):
        return Post.objects.filter(
            date_added__lte=timezone.now(), post_type='PyJava').order_by('-date_added')


class iOSView(ListView):
    model = Post
    template_name = 'posts/ios_post_list.html'
    context_object_name = 'ios_post_list'

    def get_queryset(self):
        return Post.objects.filter(
            date_added__lte=timezone.now(), post_type='iOS/Misc').order_by('-date_added')


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'individual_post'


class CreatePost(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'base.html'
    form_class = PostForm
    model = Post
    template_name = 'posts/post_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.date_added = timezone.now()
        self.object.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'posts/post_update.html'
    form_class = PostForm
    model = Post
    template_name = 'posts/post_update.html'


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('homepage')
    template_name = 'posts/post_delete.html'