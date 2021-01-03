# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class TbSmmAuthorInfo(models.Model):
    author_code = models.CharField(primary_key=True, max_length=30)
    author_nm = models.CharField(max_length=60)
    author_dc = models.CharField(max_length=1000, blank=True, null=True)
    spri_inner_author_at = models.IntegerField()
    delete_at = models.IntegerField(blank=True, null=True)
    dltr_sn = models.PositiveIntegerField(blank=True, null=True)
    delete_dt = models.DateTimeField(blank=True, null=True)
    frst_reg_ip = models.CharField(max_length=20)
    frst_reg_dttm = models.DateTimeField()
    frst_reg_id = models.CharField(max_length=20)
    last_upd_ip = models.CharField(max_length=20)
    last_upd_dttm = models.DateTimeField()
    last_upd_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tb_smm_authorinfo'

    def __str__(self):
        return 'Author-Code: %s, Author-Name: %s' % (self.author_code, self.author_nm)


class TbSumUserInfo(models.Model):
    user_sn = models.PositiveIntegerField(primary_key=True, verbose_name='사용자번호')
    user_nm = models.CharField(max_length=60, blank=True, null=True, verbose_name='이름')
    user_id = models.CharField(max_length=20, blank=True, null=True, verbose_name='직분')
    user_se = models.CharField(max_length=20, blank=True, null=True)

    # WORKAREA_ID = (
    #     ('7Q', 'Fumyhung'),
    #     ('2Q', 'Branch-#2'),
    # )
    # work_branch = models.CharField(max_length=4, choices=WORKAREA_ID, defalut='7Q')

    work_branch = models.CharField(max_length=4, blank=True, null=True,
                                   choices=(
                                       ('7Q', 'Fumyhung'),
                                       ('2Q', 'Branch-#2'),
                                   ), verbose_name='소속병원')

    # WORKTY_ID = (
    #     ('DR', 'Doctor'),
    #     ('NU', 'Nulse'),
    #     ('SC', 'Skincare'),
    #     ('CD', 'Coordinator'),
    # )
    # user_ty = models.CharField(max_length=15, choices=WORKTY_ID, blank=True, null=True, defalut='CD')
    user_ty = models.CharField(max_length=15, blank=True, null=True,
                               choices=(
                                   ('DR', 'Doctor'),
                                   ('NU', 'Nulse'),
                                   ('SC', 'Skincare'),
                                   ('CD', 'Coordinator'),
                               ))

    # GENDER_ID = (
    #     ('Male', 'Male'),
    #     ('Female', 'Female'),
    # )
    # gender = models.CharField(max_length=1, choices=GENDER_ID, blank=True, null=True, defalut='Female')
    gender = models.CharField(max_length=1, blank=True, null=True,
                              choices=(
                                  ('M', 'Male'),
                                  ('F', 'Female'),
                              ))

    company_nm = models.CharField(max_length=60, blank=True, null=True)
    telno = models.CharField(max_length=60, blank=True, null=True, verbose_name='전화번호')
    email = models.CharField(max_length=60, blank=True, null=True, verbose_name='이메일')
    password = models.CharField(max_length=60, blank=True, null=True, verbose_name='패스워드')
    new_password = models.CharField(max_length=60, blank=True, null=True)

    STAGREE_ID = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    stplat_agre_at = models.CharField(max_length=1, choices=STAGREE_ID, blank=True, null=True, default='Y')
    # stplat_agre_at = models.CharField(max_length=1, blank=True, null=True, default='Y',
    #     choices = (
    #         ('Y', 'Yes'),
    #         ('N', 'No'),
    #     ))
    #
    # stplat_agre_dt = models.DateTimeField(blank=True, null=True)

    INDVAGREE_ID = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    indvdlinfo_agre_at = models.CharField(max_length=1, choices=INDVAGREE_ID, blank=True, null=True, default='Y')
    # indvdlinfo_agre_at = models.CharField(max_length=1, blank=True, null=True, default='Y',
    #     choices = (
    #         ('Y', 'Yes'),
    #         ('N', 'No'),
    #     ))

    indvdlinfo_agre_dt = models.DateTimeField(blank=True, null=True)
    login_failr_co = models.PositiveSmallIntegerField(blank=True, null=True)
    last_login_dt = models.DateTimeField(blank=True, null=True)
    back_last_login_dt = models.DateTimeField(blank=True, null=True)
    secsn_at = models.CharField(max_length=1, blank=True, null=True)
    secsn_dt = models.DateTimeField(blank=True, null=True)
    lcns_no = models.CharField(max_length=60, blank=True, null=True)
    zip = models.CharField(max_length=6)
    bass_adres = models.CharField(max_length=100)
    detail_adres = models.CharField(max_length=100)
    brthdy = models.DateField(blank=True, null=True)
    # photo = models.ImageField(null=True, blank=True, upload_to='%Y/%m/%d')
    frst_reg_ip = models.CharField(max_length=20)
    frst_reg_dttm = models.DateTimeField(auto_now_add=True)
    frst_reg_id = models.CharField(max_length=20)
    last_upd_ip = models.CharField(max_length=20)
    last_upd_dttm = models.DateTimeField(auto_now_add=True)
    last_upd_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tb_sum_user_info'
        verbose_name = '직원명단'

    def __str__(self):
        return 'name: %s, title: %s' % (self.user_nm, self.user_ty)


class Photo(models.Model):
    user_nm = models.CharField(max_length=60)
    user_ty = models.CharField(max_length=15)
    photo = models.ImageField(null=True, blank=True, upload_to='cats_photo/')

    def __str__(self):
        return 'Name: %s title: %s' % (self.user_nm, self.user_ty)
