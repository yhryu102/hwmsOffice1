from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from rest_framework import generics
from rest_framework import mixins
#
from hwmsuser.decorators import admin_required
from .models import GoodsModel
from .forms import RegisterForm
from .serializers import GoodsSerializer
from rsvmng.forms import RegisterForm as RsvmngForm

# Create your views here.

class GoodsListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = GoodsSerializer

    def get_queryset(self):
        return GoodsModel.objects.all().order_by('goods_cd')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GoodsDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = GoodsSerializer

    def get_queryset(self):
        return GoodsModel.objects.all().order_by('goods_cd')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class GoodsList(ListView):
    model = GoodsModel
    template_name = 'goods.html'
    context_object_name = 'goods_list'

@method_decorator(admin_required, name='dispatch')
class GoodsCreate(FormView):
    template_name = 'register_goods.html'
    form_class = RegisterForm
    success_url = '/goodsmng/'

    def form_valid(self, form):
        goods = GoodsModel(
            goods_cd=form.data.get('goods_cd'),
            goods_nm=form.data.get('goods_nm'),
            maj_clas_cd=form.data.get('maj_clas_cd'),
            maj_clas_nm=form.data.get('maj_clas_nm'),
            sub_clas_cd=form.data.get('sub_clas_cd'),
            sub_clas_nm=form.data.get('sub_clas_nm'),
            goods_at=form.data.get('goods_at'),
            goods_amt=form.data.get('goods_amt')
        )
        goods.save()
        return super().form_valid(form)

class GoodsDetail(DetailView):
    template_name = 'goods_detail.html'
    queryset = GoodsModel.objects.all()
    context_object_name = 'goodsmng'
    # context_object_name = 'goods'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RsvmngForm(self.request)
        return context