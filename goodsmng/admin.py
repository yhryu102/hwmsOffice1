from django.contrib import admin
from django.utils.html import format_html
from django.contrib.humanize.templatetags.humanize import intcomma
from .models import GoodsModel


class GoodsmngAdmin(admin.ModelAdmin):
    list_display = ('goods_cd', 'goods_nm', 'sub_clas_nm', 'goods_at', 'goods_amt', 'tera_at', 'frst_reg_dttm')

    # def price_format(self, obj):
    #     price = intcomma(obj.price)
    #     return f'{price} vtd(동)'
    #
    # # def styled_stock(self, obj):
    # #     stock = obj.stock
    # #     if stock <= 50:
    # #         stock = intcomma(stock)
    # #         return format_html(f'<b><span style="color:red">{stock} 개</span></b>')
    # #     return f'{intcomma(stock)} 개'
    #
    # def changelist_view(self, request, extra_context=None):
    #     extra_context = { 'title': '상품 목록' }
    #     return super().changelist_view(request, extra_context)
    #     # return super(CstmngAdmin, self).changelist_view()
    #
    # def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
    #     goods = GoodsModel.objects.get(pk=object_id)
    #     extra_context = {'title': f'{goods.goods_nm} 상품 수정'}
    #     return super().changeform_view(request, object_id, form_url, extra_context)
    #
    # price_format.short_description = '가격'
    # # styled_stock.short_description = '재고'

admin.site.register(GoodsModel, GoodsmngAdmin)
