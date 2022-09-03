from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.views.generic import ListView, DeleteView
from .forms import EmailPostForm, CommentForm, PostForm
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/list.html'


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Список активных комментариев для этой статьи.
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        # Пользователь отправил комментарий.
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Создаем комментарий, но пока не сохраняем в базе данных
            new_comment = comment_form.save(commit=False)
            # Привязываем комментарий к текущей статье.
            new_comment.post = post
            # Сохраняем комментарий в базе данных.
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blog/detail.html', {'post': post,
                                                'comments': comments,
                                                'new_comment': new_comment,
                                                'comment_form': comment_form,
                                                })


@login_required()
def post_share(request, post_id):
    """Получение статьи по идентификатору"""
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        # Форма была отправлена на сохранение.
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Все поля формы прошли валидацию.
            cd = form.cleaned_data
            # Отправка электронной почты.
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = (f'{cd["name"]}({cd["email"]}) recommends you reading', post.title)
            message = f'Read {post.title} at {post_url}\n\n{cd["name"]}\'s comments:' \
                      f'{cd["comments"]}.'
            send_mail(subject, message, 'klimenkoruslan11@gmail.com', [cd['to']])
            sent = True

    else:
        form = EmailPostForm()
    return render(request, 'blog/share.html',
                  {'post': post, 'form': form, 'sent': sent})


@login_required()
def new_post(request):
    """Определяем новый пост"""
    if request.method == 'POST':
        # Отправлены данные POST, обработать данные
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    # Вывести пустую или недействительную форму
    context = {'form': form}
    return render(request, 'blog/new_post.html', context)


@login_required()
def post_edit(request, pk):
    """Редактирование поста"""
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        context = {'form': form}
        return render(request, 'blog/post_edit.html', context)


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



