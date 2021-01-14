from django import forms
from .models import Rsvmng
from goodsmng.models import GoodsModel
from cstmng.models import CstModel
from django.db import transaction


class RegisterForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    # 예약번호는 자동생성됨.
    rsv_sn = forms.IntegerField(
        error_messages={
            'required': '예약번호을 입력해주세요.'
        }, label='예약번호', widget=forms.HiddenInput
    )

    # 여기서의 user_sn은 고객등록번호임(사용자와 혼동하지 말것).
    # foreign key 고객등록번호는 사용자에게 보이지 않음.
    user_sn = form.IntegerField(
        error_messages={
            'required': '고객번호를 입력해주세요.'
        }, label='고객번호', widget=forms.HiddenInput
    )
    cst_nm = form.CharField(
        error_messages={
            'required': '고객명을 입력해주세요.'
        }, label='고객명'
    )
    chart_no = form.CharField(
        error_messages={
            'required': '차트번호를 입력해주세요.'
        }, label='차트번호'
    )
    rsv_dt = forms.DateField(
        error_messages={
            'required': '예약일을 입력해주세요.'
        }, label='예약일'
    )
    rsv_time = forms.CharField(
        error_messages={
            'required': '예약시간을 입력해주세요.'
        }, label='예약시간'
    )

    # foreign key 제품명은 앞의 폼에서 가져옴으로 입력받지 않음.
    good_nm = form.CharField(
        error_messages={
            'required': '고객희망 상품명을 선택해주세요.'
        }, label='고객희망 상품명'
    )

    ds_class = forms.CharField(
        error_messages={
            'required': '고객희망 상품대분류를 입력해주세요.'
        }, label='대분류명'
    )
    clnic_cd = forms.CharField(
        error_messages={
            'required': '초/재진 구분을 입력해주세요.'
        }, label='초/재진 구분'
    )
    rsv_stt_cd = forms.CharField(
        error_messages={
            'required': '고객 현재상태를 선택해주세요.'
        }, label='현재상태'
    )

    def clean(self):
        cleaned_data = super().clean()
        rsv_sn = cleaned_data.get('rsv_sn')
        rsv_dt = cleaned_data.get('rsv_dt')
        rsv_time = cleaned_data.get('rsv_time')
        goods_nm = cleaned_data.get('goods_nm')
        ds_class = cleaned_data.get('ds_class')

        if not (goods_nm and ds_class and rsv_dt and rsv_time):
            self.add_error('goods_nm', '값이 없습니다')
            self.add_error('ds_class', '값이 없습니다')
            self.add_error('rsv_dt', '값이 없습니다')
            self.add_error('rsv_time', '값이 없습니다')