"""hwmsOffice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import datetime
from datetime import date
from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path, include, re_path
from hwmsuser.views import index, logout, RegisterView, LoginView
from cstmng.views import CstList, CstCreate
from django.conf import settings
from django.conf.urls.static import static

# from goodsmng.views import GoodsList, GoodsCreate, GoodsDetail
from goodsmng.views import (
    GoodsList, GoodsCreate, GoodsDetail,
    GoodsListAPI, GoodsDetailAPI
)
from rsvmng.views import RsvCreate, RsvList
from django.views.generic import TemplateView

from rsvmng.models import Rsvmng
from .functions import get_exchange

import adminactions.actions as actions

# -------------------------------------------------------------
orig_index = admin.site.index

def auraclinic_index(request, extra_context=None):
    base_date = datetime.datetime.now() - datetime.timedelta(days=7)
    rsv_data = {}
    for i in range(7):
        target_dttm = base_date + datetime.timedelta(days=i)
        date_key = target_dttm.strftime('%Y-%m-%d')
        target_date = datetime.date(target_dttm.year, target_dttm.month, target_dttm.day)
        rsv_cnt = Rsvmng.objects.filter(frst_reg_dttm__date=target_date).count()
        rsv_data[date_key] = rsv_cnt

    extra_context = {
        'orders': rsv_data,
        'exchange': get_exchange()
    }

    return orig_index(request, extra_context)

admin.site.index = auraclinic_index
# -------------------------------

urlpatterns = [
    re_path(r'^admin/package/$',
            TemplateView.as_view(template_name='admin/package.html', extra_context={
        'title': '팩키지', 'site_title': 'Aura Clinic', 'site_header': 'Aura Clinic'})
            ),
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),

    path('', index),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', logout),
    path('cstmng/', CstList.as_view()),
    path('cstmng/create/', CstCreate.as_view()),
    path('goodsmng/', GoodsList.as_view()),
    path('goodsmng/<int:pk>/', GoodsDetail.as_view()),
    path('goodsmng/create/', GoodsCreate.as_view()),
    path('rsvmng/', RsvList.as_view()),
    path('rsvmng/create/', RsvCreate.as_view()),

    path('api/goodsmng/', GoodsListAPI.as_view()),
    path('api/goodsmng/<int:pk>/', GoodsDetailAPI.as_view()),
    path('adminactions/', include('adminactions.urls')),    # Graph
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# import adminactions.actions as actions
actions.add_to_site(admin.site)
