from django.contrib.auth import logout, authenticate, login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from .models import Post


User = get_user_model()


class MainPageView(View):

    def get(self, request):
        # context = {
        #     'posts': Post.objects.all().order_by('-id')
        # }
        # return render(request, 'main_page.html', context)

        object_list = Post.objects.all().order_by('-id')
        paginator = Paginator(object_list, 2)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(request, 'main_page.html',
                      {'page': page,
                       'posts': posts})


class Login(View):

    def get(self, request):
        if request.user.is_anonymous:
            return render(request, 'login.html')
        else:
            return redirect('/')

    def post(self, request):
        user = authenticate(
            username=User.objects.get(email=request.POST.get('email')).username,
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect("/")
        return render(request, 'login.html', {'error': 'ай-яй-яй!'})


def logout_func(request):
    logout(request)
    return redirect('/login')


class RegistrationView(View):

    def get(self, request):
        if request.user.is_anonymous:
            return render(request, 'register.html')
        else:
            return redirect('/')

    def post(self, request):
        if request.POST.get('password') == request.POST.get('re_password'):
            user = User.objects.create_user(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                username=request.POST.get('username'),
                email=request.POST.get('email'),
                password=request.POST.get('password'),
            )
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'register.html', {'re_password': "password not match"})


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def post(self, request):
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect('/')

