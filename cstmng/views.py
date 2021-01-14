from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from rest_framework import generics
from rest_framework import mixins

from hwmsuser.decorators import admin_required
from .models import CstModel
from .forms import RegisterForm
# from .serializers import CstSerializer
from rsvmng.forms import RegisterForm as RsvmngForm

# Create your views here.

class CstList(ListView):
    model = CstModel
    template_name = 'cst.html'
    context_object_name = 'cst_list'

@method_decorator(admin_required, name='dispatch')
class CstCreate(FormView):
    template_name = 'register_cst.html'
    form_class = RegisterForm
    success_url = '/cstmng/'

    def form_valid(self, form):
        cst = CstModel(
            user_sn=models.PositiveIntegerField(primary_key=True, verbose_name='고객번호'),
            cst_nm=form.data.get('cst_nm'),
            email=form.data.get('email'),
            chart_no=form.data.get('chart_no'),
            country_cd=form.data.get('country_cd'),
            tel_no=form.data.get('tel_no'),
            nation_nm=form.data.get('nation_nm'),
            gender_cd=form.data.get('gender_cd'),
            brth_dt=form.data.get('brth_dt'),
            adit_desc=form.data.get('adit_desc'),
            vip_level=form.data.get('vip_level'),
            reg_baranch=form.data.get('reg_baranch'),
            frst_reg_dttm=form.data.get('frst_reg_dttm')
        )
        cst.save()
        return super().form_valid(form)

class CstDetail(DetailView):
    template_name = 'cst_detail.html'
    queryset = CstModel.objects.all()
    context_object_name = 'cst'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RsvmngForm(self.request)
        return context