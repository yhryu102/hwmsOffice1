from django.contrib import admin
from .models import GoodsModel


class GoodsmngAdmin(admin.ModelAdmin):
    list_display = ('goods_cd', 'goods_nm', 'sub_clas_nm', 'goods_at', 'goods_amt', 'tera_at', 'frst_reg_dttm')

    def changelist_view(self, request, extra_context=None):
        extra_context = { 'title': '상품 목록' }
        return super().changelist_view(request, extra_context)
        # return super(CstmngAdmin, self).changelist_view()

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        goods = GoodsModel.objects.get(pk=object_id)
        extra_context = {'title': f'{goods.goods_nm} 상품 수정'}
        return super().changeform_view(request, object_id, form_url, extra_context)

admin.site.register(GoodsModel, GoodsmngAdmin)
