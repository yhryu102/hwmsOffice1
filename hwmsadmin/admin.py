from django.contrib import admin
from django.utils.safestring import mark_safe
from rangefilter.filter import DateRangeFilter

from .models import TbSumUserInfo, TbSmmAuthorInfo, Photo


# Register your models here.

class DisplayTbSumUserInfo(admin.ModelAdmin):
    fields = ('user_sn', 'user_nm', 'user_ty', 'work_branch', 'telno', 'email', 'brthdy')
    list_display = ('user_sn', 'user_nm', 'user_ty', 'work_branch', 'telno', 'email', 'brthdy')
    search_fields = ['user_nm']
    list_filter = ('work_branch', 'user_ty', ('brthdy', DateRangeFilter))
    ordering = ('user_nm', 'user_ty', 'frst_reg_dttm',)

    # readonly_fields = ['user_sn', 'user_nm']


class DisplayTbSmmAuthorInfo(admin.ModelAdmin):
    fields = ('author_code', 'author_nm')
    list_display = ('author_code', 'author_nm')
    # readonly_fields = ('author_code',)


class DisplayPhoto(admin.ModelAdmin):
    fields = ('user_nm', 'user_ty', 'photo')
    list_display = ('user_nm', 'user_ty', 'photo', 'get_image')

    def get_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height="{height}" />'.format(
            url=obj.photo.url,
            width=obj.photo.width,
            height=obj.photo.height,
        )
        )

admin.site.register(TbSumUserInfo, DisplayTbSumUserInfo)
admin.site.register(TbSmmAuthorInfo)
admin.site.register(Photo, DisplayPhoto)
