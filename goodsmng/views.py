from django.shortcuts import render
# from django.views.generic import ListView, DetailView
from django.views.generic import ListView
from django.views.generic.edit import FormView
# from django.utils.decorators import method_decorator
# from rest_framework import generics
# from rest_framework import mixins
#
# from fcuser.decorators import admin_required
from .models import GoodsModel
from .forms import RegisterForm
# from .serializers import ProductSerializer
# from order.forms import RegisterForm as OrderForm

# Create your views here.

# class ProductListAPI(generics.GenericAPIView, mixins.ListModelMixin):
#     serializer_class = ProductSerializer
#
#     def get_queryset(self):
#         return Product.objects.all().order_by('id')
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#
# class ProductDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
#     serializer_class = ProductSerializer
#
#     def get_queryset(self):
#         return Product.objects.all().order_by('id')
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


class GoodsList(ListView):
    model = GoodsModel
    template_name = 'goods.html'
    context_object_name = 'goods_list'

# @method_decorator(admin_required, name='dispatch')
class GoodsCreate(FormView):
    template_name = 'register_goods.html'
    form_class = RegisterForm
    success_url = '/goodsmng/'

    def form_valid(self, form):
        goods = GoodsModel(
            goods_cd=form.data.get('goods_cd'),
            goods_nm=form.data.get('goods_nm'),
            sub_clas_cd=form.data.get('sub_clas_cd'),
            sub_clas_nm=form.data.get('sub_clas_nm'),
            maj_clas_cd=form.data.get('maj_clas_cd'),
            maj_clas_nm = form.data.get('maj_clas_nm'),
            goods_at = form.data.get('goods_at'),
            goods_amt = form.data.get('goods_amt')
        )
        goods.save()
        return super().form_valid(form)

# class ProductDetail(DetailView):
#     template_name = 'product_detail.html'
#     queryset = Product.objects.all()
#     context_object_name = 'product'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = OrderForm(self.request)
#         return context