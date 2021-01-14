import datetime
from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.contrib import admin
from django.template.response import TemplateResponse
from django.utils.html import format_html
from django.db import transaction
from django.urls import path
from .models import Rsvmng

# Register your modes here.
def rsv_cancel(modeladmin, request, queryset):
    with transaction.atomic():
        qs = queryset.filter(~Q(rsv_stt_cd='예약취소'))

        ct = ContentType.objects.get_for_model(queryset.model)
        for obj in qs:
            # obj.product.stock += obj.quantity         # 재고관리에서 재고수량 가감의 예일 뿐
            # obj.product.save()

            # 화면의 최근활동-나의활동을 트랜젝션 단위까지 로그남기기
            LogEntry.objects.log_action(
                user_id=request.user.id,
                content_type_id=ct.pk,
                object_id=obj.pk,
                object_repr='예약취소',
                action_flag=CHANGE,
                change_message='예약취소'
            )
        qs.update(rsv_stt_cd='예약취소')

rsv_cancel.short_description = '환불'
# 여기까지 커스톰 액션 추가하기

class RsvmngAdmin(admin.ModelAdmin):
    list_filter = ('rsv_stt_cd',)
    list_display = ('user_sn', 'rsv_sn', 'rsv_dt', 'rsv_time', 'goods_nm', 'ds_class', 'frst_reg_dttm')
    # list_display = ('user_sn', 'rsv_sn', 'rsv_dt', 'rsv_time', 'goods_nm', 'ds_class', 'frst_reg_dttm', 'action')
    # change_list_template = 'admin/rsv_change_list.html'
    # change_form_template = 'admin/rsv_change_form.html'
    #
    # actions = [
    #     rsv_cancel
    # ]
    #
    # def action(self, obj):
    #     if obj.rsv_stt_cd != '예약취소':
    #         # return format_html(f'<input type="button" value="예약취소" onclick="order_refund_submit({obj.id})" class="btn btn-primary btn-sm">')
    #         return format_html(
    #             f'<input type="button" value="예약취소" onclick="rsv_cancel_submit({obj.id})" class="btn btn-primary btn-sm">')
    #
    # def styled_status(self, obj):
    #     if obj.rsv_stt_cd == '예약취소':
    #         return format_html(f'<span style="color:red">{obj.rsv_stt_cd}</span>')
    #     if obj.rsv_stt_cd == '결제완료':
    #         return format_html(f'<span style="color:green">{obj.rsv_stt_cd}</span>')
    #     return obj.rsv_stt_cd
    #
    #
    # def changelist_view(self, request, extra_context=None):
    #     extra_context = { 'title': '예약 목록' }
    #
    #     if request.method == 'POST':
    #         obj_id = request.POST.get('obj_id')
    #         if obj_id:
    #             qs = Rsvmng.objects.filter(pk=obj_id)
    #             ct = ContentType.objects.get_for_model(qs.model)
    #             for obj in qs:
    #                 # obj.product.stock += obj.quantity         # 재고관리에서 재고수량 가감의 예일 뿐
    #                 # obj.product.save()
    #
    #                 LogEntry.objects.log_action(
    #                     user_id=request.user.id,
    #                     content_type_id=ct.pk,
    #                     object_id=obj.pk,
    #                     object_repr='예약취소',
    #                     action_flag=CHANGE,
    #                     change_message='예약취소',
    #                 )
    #             qs.update(rsv_stt_cd='예약취소')
    #
    #     return super().changelist_view(request, extra_context)
    #
    # # yyh : pk 필드 에러 문제 해결 후 풀었음(12일오후 13시)
    # def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
    #     rsvmng = Rsvmng.objects.get(pk=object_id)
    #     extra_context = { 'title': f"'{rsvmng.cstmng.user_sn}'의 '{rsvmng.goodscdmng.goods_nm}' 예약 수정" }
    #     extra_context['show_save_and_add_another'] = False
    #     extra_context['show_save_and_continue'] = False
    #     return super().changeform_view(request, object_id, form_url, extra_context)
    #
    # def get_urls(self):
    #     urls = super().get_urls()
    #     date_urls = [
    #         path('date_view/', self.date_view)
    #     ]
    #     return date_urls + urls
    #
    # def date_view(self, request):
    #     week_date = datetime.datetime.now() - datetime.timedelta(days=7)
    #     week_data = Rsvmng.objects.filter(frst_reg_dttm__gte=week_date)
    #     data = Rsvmng.objects.filter(frst_reg_dttm__lt=week_date)
    #     context = dict(
    #         self.admin_site.each_context(request),
    #         week_data=week_data,
    #         data=data
    #     )
    #     return TemplateResponse(request, 'admin/rsvmng_date_view.html', context)

admin.site.register(Rsvmng, RsvmngAdmin)
