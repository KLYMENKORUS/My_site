from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [

    path('', include('django.contrib.auth.urls')),
    # Страница регистрации
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    # Редактирование профиля
    path('edit/profile/', views.edit_profile, name='edit_profile'),
    # Страница профиля
    path('profile/', views.profile, name='profile'),

]
