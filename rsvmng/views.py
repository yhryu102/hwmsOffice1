from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from cstmng.decorators import login_required
from django.db import transaction
from .forms import RegisterForm
from .models import Rsvmng
from goodsmng.models import GoodsModel
from cstmng.models import CstModel

# Create your views here.

@method_decorator(login_required, name='dispatch')
class RsvCreate(FormView):
    form_class = RegisterForm
    success_url = '/goodsmng/'

    def form_valid(self, form):
        # goods = GoodsModel.objects.get(pk=form.data.get('rsvmng'))
        goods = GoodsModel.objects.get(pk=form.data.get('goods_nm'))
        # goods = GoodsModel.objects.get(pk=form.data.get('goodsmng'))
        rsv = Rsvmng(
            # ds_srop_desc=form.data.get('ds_srop_desc'),
            ds_class=form.data.get('ds_class'),
            rsv_dt=form.data.get('rsv_dt'),
            rsv_time=form.data.get('rsv_time'),
            goods_nm=goods,
            # product=goods,
            cstmng=CstModel.objects.get(user_sn=self.request.session.get('user'))
        )
        rsv.save()

        return super().form_valid(form)


    # def form_valid(self, form):
    #     with transaction.atomic():
    #         # goods = GoodsModel.objects.get(pk=form.data.get('rsvmng'))
    #         # goods = GoodsModel.objects.get(pk=form.data.get('ds_srop_desc'))
    #         goods = GoodsModel.objects.get(pk=form.data.get('goods_nm'))
    #         rsv = Rsvmng(
    #             # ds_srop_desc=form.data.get('ds_srop_desc'),
    #             ds_class=form.data.get('ds_class'),
    #             rsv_dt=form.data.get('rsv_dt'),
    #             rsv_time=form.data.get('rsv_time'),
    #             ds_srop_desc=goods,
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
        # return redirect('/goodsmng/' + str(form.data.get('goodsmng')))

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


    def get_queryset(self, **kwargs):
        # queryset = Rsvmng.objects.filter(goods_nm=self.request.session.get('user'))
        queryset = Rsvmng.objects.filter(cstmng__user_sn=self.request.session.get('user'))

        print('yyh test queryset ?????????????', queryset)

        return queryset