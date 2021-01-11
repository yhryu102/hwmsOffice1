from django.shortcuts import redirect
from .models import CstModel

def login_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')
        return function(request, *args, **kwargs)

    return wrap

def admin_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')
        
        user = CstModel.objects.get(user_sn=user)

        print('yyh / admin_required  ~~ user ?????????????????????????????????????', user)
        # yyh / 테스트 : 세션에 접근이 되는지 터미널에서 아래 수행 확인
        print('yyh / admin_required에서 세션에 접근이 되는지 터미널에서 아래 수행 확인 :', user)

        if user.user_se != 'admin':
            return redirect('/')

        return function(request, *args, **kwargs)

    return wrap
