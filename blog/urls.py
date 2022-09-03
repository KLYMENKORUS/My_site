from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    # Главная страница блога
    path('index/', views.index, name='post_index'),
    # path('', views.post_list, name='post_list'),
    # Страница постов
    path('', views.PostListView.as_view(), name='post_list'),
    # Информация о статье
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # Страница отправки e-mail
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    # Страница для добавления нового поста
    path('new/post/', views.new_post, name='new_post'),
    # Страница редактирования поста
    path('edit/<int:pk>/post/', views.post_edit, name='post_edit'),
    # Удаление поста
    path('delete/<int:pk>/post', views.PostDeleteView.as_view(), name='delete_post'),

]
