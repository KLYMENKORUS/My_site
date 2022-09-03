from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login
from .forms import UserEditForm, ProfileEditForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.views import View


# Create your views here.
class RegistrationView(View):
    form_class = UserRegistrationForm
    initial = {'key': 'value'}
    template_name = 'registration/registration.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/')

        return super(RegistrationView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))

        return render(request, self.template_name, {'form': form})


@login_required()
def profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, request.FILES,
                                       instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('blog:post_list'))
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    context = {'user_form': user_form,
               'profile_form': profile_form, }
    return render(request, 'registration/profile.html', context)


@login_required()
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render(request, 'registration/register_done.html')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    context = {'user_form': user_form,
               'profile_form': profile_form, }
    return render(request, 'registration/edit_profile.html', context)
