from django.contrib import admin
from .models import CTbSumUserInfo, Cstmng

class CTbSumUserInfoAdmin(admin.ModelAdmin):
    list_display = ('email', )

class CstmngAdmin(admin.ModelAdmin):
    list_display = ('chart_no', 'cst_nm', 'country_cd', 'tel_no', 'nation_nm', 'gender_cd', 'brth_dt', 'frst_reg_dttm')


admin.site.register(CTbSumUserInfo, CTbSumUserInfoAdmin)
admin.site.register(Cstmng, CstmngAdmin)
