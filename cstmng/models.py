from django.db import models


# Create your models here.


class CstModel(models.Model):
    # user_sn = models.AutoField(primary_key=True)
    user_sn = models.PositiveIntegerField(primary_key=True, verbose_name='등록번호')
    cst_nm = models.CharField(max_length=60, verbose_name='고객명')
    email = models.CharField(max_length=64, verbose_name='이메일')
    chart_no = models.CharField(max_length=10, verbose_name='차트번호')

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
        ('일반', '일반'),
        ('VIP', 'VIP'),
        ('VVIP', 'VVIP'),
        ('프리미엄', '프리미엄')
    )
    vip_level = models.CharField(max_length=60, choices=VIP_ID, blank=True, null=True,
                                 verbose_name='VIP 등급')

    RBRANCH_ID = (
        ('1Q', '1Q'),
        ('7Q', '7Q'),
    )
    reg_baranch = models.CharField(max_length=60, choices=RBRANCH_ID, blank=True, null=True,
                                verbose_name='초진사업장')

    frst_reg_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return 'USER-NO: %d Customer-name : %s' % (self.user_sn, self.cst_nm)

    class Meta:
        db_table = 'cstmng'
        verbose_name = '고객'
        verbose_name_plural = '고객'