from django.contrib import admin
from .models import CstModel

class CstmngAdmin(admin.ModelAdmin):
    list_display = ('user_sn', 'cst_nm', 'email', 'chart_no', 'tel_no', 'gender_cd', 'vip_level', 'reg_baranch', 'frst_reg_dttm')

    # def changelist_view(self, request, extra_context=None):
    #     extra_context = { 'title': '고객 목록' }
    #     return super().changelist_view(request, extra_context)
    #     # return super(CstmngAdmin, self).changelist_view()
    #
    # def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
    #     cstmng = CstModel.objects.get(pk=object_id)
    #     extra_context = {'title': f'{cstmng.email} 로그인정보 수정'}
    #     return super().changeform_view(request, object_id, form_url, extra_context)

admin.site.register(CstModel, CstmngAdmin)
admin.site.site_header = 'AURA Clinic'
admin.site.index_title = 'AURA Clinic-1'
admin.site.site_title = 'AURA Clinic-2'