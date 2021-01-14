from django.db import models


# Create your models here.


class UserModel(models.Model):
    user_sn = models.PositiveIntegerField(primary_key=True, verbose_name='사용자번호')
    user_nm = models.CharField(max_length=60, verbose_name='이름')
    email = models.CharField(max_length=128, verbose_name='이메일')
    password = models.CharField(max_length=128, blank=True, null=True, verbose_name='패스워드')
    user_se = models.CharField(max_length=8, verbose_name='사용자구분',
        choices=(
            ('admin', 'admin'),
            ('사용자', '사용자')
        ))
    frst_reg_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'tb_sum_user_info'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
