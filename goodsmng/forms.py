from django import forms
from .models import GoodsModel


class RegisterForm(forms.Form):
    goods_cd = forms.CharField(
        error_messages={
            'required': '상품코드를 입력해주세요.'
        },
        max_length=10, label='상품코드'
    )
    goods_nm = forms.CharField(
        error_messages={
            'required': '상품명을 입력해주세요.'
        },
        max_length=100, label='상품명'
    )
    sub_clas_cd = forms.CharField(
        error_messages={
            'required': '대분류코드를 입력해주세요.'
        },
        max_length=10, label='대분류코드'
    )
    sub_clas_nm = forms.CharField(
        error_messages={
            'required': '대분류명을 입력해주세요.'
        },
        max_length=60, label='대분류명'
    )
    maj_clas_cd = forms.CharField(
        error_messages={
            'required': '범주코드를 입력해주세요.'
        },
        max_length=10, label='범주코드'
    )
    maj_clas_nm = forms.CharField(
        error_messages={
            'required': '범주명을 입력해주세요.'
        },
        max_length=60, label='범주명'
    )
    goods_at = forms.CharField(
        error_messages={
            'required': '일반/이벤트 상품 구분을 선택해주세요.'
        },
        max_length=1, label='이벤트구분'
    )
    goods_amt = forms.IntegerField(
        error_messages={
            'required': '상품가격을 입력해주세요.'
        }, label='상품가격'
    )
    # description = forms.CharField(
    #     error_messages={
    #         'required': '상품설명을 입력해주세요.'
    #     }, label='상품설명'
    # )
    # stock = forms.IntegerField(
    #     error_messages={
    #         'required': '재고를 입력해주세요.'
    #     }, label='재고'
    # )

    def clean(self):
        cleaned_data = super().clean()
        goods_cd = cleaned_data.get('goods_cd')
        goods_nm = cleaned_data.get('goods_nm')
        maj_clas_cd = cleaned_data.get('maj_clas_cd')
        maj_clas_nm = cleaned_data.get('maj_clas_nm')
        sub_clas_cd = cleaned_data.get('sub_clas_cd')
        sub_clas_nm = cleaned_data.get('sub_clas_nm')
        goods_at = cleaned_data.get('goods_at')
        goods_amt = cleaned_data.get('goods_amt')

        if not (goods_cd and goods_nm and maj_clas_cd and maj_clas_nm and sub_clas_cd and sub_clas_nm and goods_at and goods_amt):
            self.add_error('goods_cd', '상품코드값이 없습니다')
            self.add_error('goods_nm', '상품명이 없습니다')
            self.add_error('maj_clas_cd', '범주코드값이 없습니다')
            self.add_error('maj_clas_nm', '범주명이 없습니다')
            self.add_error('sub_clas_cd', '대분류코드값이 없습니다')
            self.add_error('sub_clas_nm', '대분류명이 없습니다')
            self.add_error('goods_at', '이벤트구분값이 없습니다')
            self.add_error('goods_amt', '상품가격이 없습니다')
        else:
            goods = GoodsModel(
                goods_cd=goods_cd,
                goods_nm=goods_nm,
                maj_clas_cd=maj_clas_cd,
                maj_clas_nm=maj_clas_nm,
                sub_clas_cd=sub_clas_cd,
                sub_clas_nm=sub_clas_nm,
                goods_at=goods_at,
                goods_amt=goods_amt
            )
            goods.save()
