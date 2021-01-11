from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.edit import FormView
# from django.contrib.auth.hashers import make_password
from .forms import RegisterForm, LoginForm
from .models import CstModel

# Create your views here.

def index(request):
    return render(request, 'index.html', { 'user_sn': request.session.get('user') })


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        cstmng = CstModel(
            email=form.data.get('email'),
            # password=make_password(form.data.get('password')),
            password=form.data.get('password'),
            user_se='사용자'
        )
        cstmng.save()

        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.data.get('user_sn')
        # self.request.session['user'] = form.user_sn

        return super().form_valid(form)

def logout(request):
    if 'user' in request.session:
        del (request.session['user'])

    return redirect('/')