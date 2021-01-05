from django.db import models


# Create your models here.


class Hwmsuser(models.Model):
    user_sn = models.AutoField(primary_key=True)
    email = models.CharField(max_length=128, blank=True, null=True, verbose_name='이메일')
    password = models.CharField(max_length=128, blank=True, null=True, verbose_name='패스워드')
    user_se = models.CharField(max_length=8, verbose_name='사용자구분',
        choices=(
            ('admin', 'admin'),
            ('user', 'user')
        ))

    frst_reg_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')


    def __str__(self):
        return self.email

    class Meta:
        db_table = 'hwmsuser'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'


'''   나중에 사용할 수 있을 듯 하여 남겨 놓음.   
class Cstmng(models.Model):
    chart_no = models.CharField(primary_key=True, max_length=10, verbose_name='차트번호')
    # cst_nm = models.CharField(primary_key=True, max_length=60, verbose_name='고객명')
    cst_nm = models.CharField(max_length=60, verbose_name='고객명')

    COUNTRY_ID = (
        ('00', '미확인'),
        ('82', '한국'),
        ('84', '베트남'),
        ('86', '중국'),
        ('66', '태국')
    )
    country_cd = models.CharField(max_length=3, choices=COUNTRY_ID, blank=True, null=True, default='82',
                                  verbose_name='국가번호')

    tel_no = models.CharField(max_length=60, verbose_name='전화번호')

    NATION_ID = (
        ('00', '미확인'),
        ('82', '한국'),
        ('84', '베트남'),
        ('86', '중국'),
        ('66', '태국')
    )
    nation_nm = models.CharField(max_length=60, choices=NATION_ID, blank=True, null=True, default='82',
                                  verbose_name='국적')

    GENDER_ID = (
        ('남', '남성'),
        ('여', '여성'),
    )
    gender_cd = models.CharField(max_length=16, choices=GENDER_ID, blank=True, null=True, default='여',
                                 verbose_name='성별')

    brth_dt = models.DateField(verbose_name='생년월일')
    adit_desc = models.TextField(verbose_name='고객정보 추가사항')

    VIP_ID = (
        ('프리미엄', '프리미엄'),
        ('VVIP', 'VVIP'),
        ('VIP', 'VIP'),
    )
    vip_level = models.CharField(max_length=60, choices=VIP_ID, blank=True, null=True,
                                 verbose_name='VIP등급')

    RBRANCH_ID = (
        ('푸미흥점', '푸미흥점'),
        ('2Q점', '2Q점'),
    )
    reg_baranch = models.CharField(max_length=60, choices=RBRANCH_ID, blank=True, null=True,
                                verbose_name='초진사업장')

    frst_reg_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return 'Chart-no: %s Customer-name : %s' % (self.chart_no, self.cst_nm)

    class Meta:
        db_table = 'cstmng'
        verbose_name = '고객관리'
        verbose_name_plural = '고객관리'
'''