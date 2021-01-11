from django import forms
from .models import Rsvmng
from goodsmng.models import GoodsModel
from hwmsuser.models import Hwmsuser
from django.db import transaction


class RegisterForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    # rsv_sn = forms.DateField(
    #     error_messages={
    #         'required': '예약일을 입력해주세요.'
    #     }, label='예약일'
    # )
    rsv_dt = forms.DateField(
        error_messages={
            'required': '예약일을 입력해주세요.'
        }, label='예약일'
    )
    rsv_time = forms.CharField(
        error_messages={
            'required': '시간을 입력해주세요.'
        }, label='시간'
    )
    ds_srop_desc = forms.CharField(
        error_messages={
            'required': '고객희망 시술내용을 입력해주세요.'
        }, label='희망시술'
    )
    ds_class = forms.CharField(
        error_messages={
            'required': '고객희망 대분류를 입력해주세요.'
        }, label='대분류명'
    )

    # quantity = forms.IntegerField(
    #     error_messages={
    #         'required': '수량을 입력해주세요.'
    #     }, label='수량'
    # )
    # product = forms.IntegerField(
    #     error_messages={
    #         'required': '상품설명을 입력해주세요.'
    #     }, label='상품설명', widget=forms.HiddenInput
    # )

    def clean(self):
        cleaned_data = super().clean()
        rsv_sn = cleaned_data.get('rsv_sn')
        rsv_dt = cleaned_data.get('rsv_dt')
        rsv_time = cleaned_data.get('rsv_time')
        ds_srop_desc = cleaned_data.get('ds_srop_desc')
        ds_class = cleaned_data.get('ds_class')

        if not (ds_srop_desc and ds_class and rsv_dt and rsv_time):
            self.add_error('ds_srop_desc', '값이 없습니다')
            self.add_error('ds_class', '값이 없습니다')
            self.add_error('rsv_dt', '값이 없습니다')
            self.add_error('rsv_time', '값이 없습니다')