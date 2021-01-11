from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from hwmsuser.decorators import login_required
from django.db import transaction
from .forms import RegisterForm
from .models import Rsvmng
from goodsmng.models import GoodsModel
from hwmsuser.models import Hwmsuser

# Create your views here.

@method_decorator(login_required, name='dispatch')
class RsvCreate(FormView):
    form_class = RegisterForm
    success_url = '/goodsmng/'

    def form_valid(self, form):
        # goods = GoodsModel.objects.get(pk=form.data.get('rsvmng'))
        # goods = GoodsModel.objects.get(pk=form.data.get('goods_nm'))
        goods = GoodsModel.objects.get(pk=form.data.get('goods_nm'))
        rsv = Rsvmng(
            # goods_nm=form.data.get('goods_nm'),
            ds_class=form.data.get('ds_class'),
            rsv_dt=form.data.get('rsv_dt'),
            rsv_time=form.data.get('rsv_time'),
            goods_nm=goods,
            # product=goods,
            hwmsuser=Hwmsuser.objects.get(email=self.request.session.get('user'))
        )
        rsv.save()

        return super().form_valid(form)


    # def form_valid(self, form):
    #     with transaction.atomic():
    #         # goods = GoodsModel.objects.get(pk=form.data.get('rsvmng'))
    #         # goods = GoodsModel.objects.get(pk=form.data.get('goods_nm'))
    #         goods = GoodsModel.objects.get(pk=form.data.get('goods_nm'))
    #         rsv = Rsvmng(
    #             # goods_nm=form.data.get('goods_nm'),
    #             ds_class=form.data.get('ds_class'),
    #             rsv_dt=form.data.get('rsv_dt'),
    #             rsv_time=form.data.get('rsv_time'),
    #             goods_nm=goods,
    #             # product=goods,
    #             hwmsuser=Hwmsuser.objects.get(email=self.request.session.get('user'))
    #         )
    #         rsv.save()
    #         # prod.stock -= int(form.data.get('quantity'))
    #         # prod.save()
    #
    #     return super().form_valid(form)


    def form_invalid(self, form):
        return redirect('/goodsmng/' + str(form.data.get('goods_nm')))

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw

@method_decorator(login_required, name='dispatch')
class RsvList(ListView):
    template_name = 'rsv.html'
    context_object_name = 'rsv_list'

    print('decor에 갔다가 여기 온건지??????????????')

    def get_queryset(self, **kwargs):
        queryset = Rsvmng.objects.filter(goods_nm=self.request.session.get('user'))
        # queryset = Rsvmng.objects.filter(hwmsuser__email=self.request.session.get('user'))
        return queryset
