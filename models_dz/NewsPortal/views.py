from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from .forms import PostForm
from .filters import NewsFilter
from django.urls import reverse_lazy
from .filters import NewsFilter


class NewsList(ListView):
    model = Post
    template_name = 'flatpages/post_list.html'
    context_object_name = 'posts'
    ordering = '-dateCreation'
    paginate_by = 2


class PostDetail(DeleteView):
    model = Post
    template_name = 'flatpages/post_detail.html'
    context_object_name = 'post'


# Переопределяем функцию получения списка товаров
def get_queryset(self):
    # Получаем обычный запрос
    queryset = super().get_queryset()
    self.filterset = NewsFilter(self.request.GET, queryset)
    return self.filterset.qs


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    # Добавляем в контекст объект фильтрации.
    context['filterset'] = self.filterset
    return context


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/post_edit.html'
    context_object_name = 'edit'


class PostDelete(DeleteView):
    model = Post
    template_name = 'flatpages/post_delete.html'
    context_object_name = 'delete'
    success_url = 'news_list'


class PostSearch(ListView):
    model = Post
    template_name = 'flatpages/post_search.html'
    context_object_name = 'search'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['time_now'] = datetime.now()
        return context


class PostCreate(CreateView):
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'flatpages/post_create.html'
    context_object_name = 'create'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/articles/create/':
            post.post.news = 'AR'
        return super().form_valid(form)
