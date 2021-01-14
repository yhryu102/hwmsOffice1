from django import forms
# from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.hashers import check_password
from .models import CstModel

class RegisterForm(forms.Form):
    cst_nm = forms.CharField(
        error_messages={
            'required': '고객명을 입력해주세요.'
        },
        max_length=60, label='고객명'
    )
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요.'
        },
        max_length=64, label='이메일'
    )
    chart_no = forms.CharField(
        error_messages={
            'required': '차트번호를 입력해주세요.'
        },
        max_length=10, label='차트번호'
    )
    # country_cd = forms.CharField(
    #     error_messages={
    #         'required': '국가번호를 입력해주세요.'
    #     },
    #     max_length=3, label='국가번호'
    # )
    tel_no = forms.CharField(
        error_messages={
            'required': '전화번호를 입력해주세요.'
        },
        max_length=60, label='전화번호'
    )
    # nation_nm = forms.CharField(
    #     error_messages={
    #         'required': '국적을 입력해주세요.'
    #     },
    #     max_length=3, label='국적'
    # )
    gender_cd = forms.CharField(
        error_messages={
            'required': '성별을 입력해주세요.'
        },
        max_length=16, label='성별'
    )
    brth_dt = forms.DateField(
        error_messages={
            'required': '생년월일을 입력해주세요.'
        },
        label='생년월일'
    )
    vip_level = forms.CharField(
        error_messages={
            'required': 'VIP 등급을 입력해주세요.'
        },
        max_length=60, label='VIP 등급'
    )
    reg_baranch = forms.CharField(
        error_messages={
            'required': '초진했던 사업장을 입력해주세요.'
        },
        max_length=60, label='초진사업장'
    )

    def clean(self):
        cleaned_data = super().clean()

        cst_nm = cleaned_data.get('cst_nm')
        email = cleaned_data.get('email')
        chart_no = cleaned_data.get('chart_no')
        country_cd = cleaned_data.get('country_cd')
        tel_no = cleaned_data.get('tel_no')
        nation_nm = cleaned_data.get('nation_nm')
        gender_cd = cleaned_data.get('gender_cd')
        adit_desc = cleaned_data.get('adit_desc')
        vip_level = cleaned_data.get('vip_level')
        reg_baranch = cleaned_data.get('reg_baranch')
        frst_reg_dttm = cleaned_data.get('frst_reg_dttm')

        if not (
                cst_nm and email and tel_no and nation_nm and gender_cd and vip_level and reg_baranch):
            self.add_error('cst_nm', '고객명이 없습니다')
            self.add_error('email', '이메일이 없습니다')
            self.add_error('tel_no', '전화번호가 없습니다')
            self.add_error('nation_nm', '국적이 없습니다')
            self.add_error('gender_cd', '성별이 없습니다')
            self.add_error('vip_level', 'VIP 등급이 없습니다')
            self.add_error('reg_baranch', '초진사업장이 없습니다')
