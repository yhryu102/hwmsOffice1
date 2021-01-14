from django.db import models


# Create your models here.

class Rsvmng(models.Model):
    # cst = models.ForeignKey('cst~~.Hwmsuser', on_delete=models.CASCADE, verbose_name='사용자')

    user_sn = models.PositiveIntegerField(verbose_name='등록번호')
    rsv_sn = models.PositiveIntegerField(primary_key=True, verbose_name='예약번호')
    cst_nm = models.CharField(max_length=60, verbose_name='고객명')
    chart_no = models.CharField(max_length=10, verbose_name='차트번호')
    rsv_dt = models.DateField(verbose_name='예약날짜')

    RSV_TIME = (
        ('10:30', '10:30'),
        ('11:00', '11:00'),
        ('11:30', '11:30'),
        ('13:00', '13:00'),
        ('13:30', '13:30'),
        ('14:00', '14:00'),
        ('14:30', '14:30'),
        ('15:00', '15:00'),
        ('15:30', '15:30'),
        ('16:00', '16:00'),
        ('16:30', '16:30'),
        ('17:00', '17:00'),
        ('17:30', '17:30'),
    )
    rsv_time = models.CharField(max_length=5, choices=RSV_TIME, blank=True, null=True, default='',
                                  verbose_name='예약시간')
    # rsv_time = models.CharField(max_length=5, verbose_name='예약시간')

    goods_nm = models.CharField(max_length=100, verbose_name='고객희망시술내용')
    ds_class = models.CharField(max_length=60, verbose_name='대분류')
    # goods_nm = models.ForeignKey('goodsmng.GoodsModel', on_delete=models.CASCADE, verbose_name='고객희망시술내용')
    CLNIC_ID = (
        ('초진', '초진'),
        ('재진', '재진'),
    )
    clnic_cd = models.CharField(max_length=16, choices=CLNIC_ID, verbose_name='초/재진')

    STT_CD = (
        ('예약', '예약'),
        ('접수', '접수'),
        ('수납대기', '수납대기'),
        ('시술중', '시술중'),
        ('시술완료', '시술완료'),
        ('수납완료', '수납완료'),
        ('예약취소', '예약취소'),
        ('미방문', '미방문'),
    )
    rsv_stt_cd = models.CharField(max_length=16, choices=STT_CD, blank=True, null=True, default='',
                                  verbose_name='현재상태')

    frst_reg_dttm = models.DateTimeField(auto_now_add=True, verbose_name='주문날짜')

    def __str__(self):
        return str(self.ds_class) + ' ' + str(self.goods_nm)
        # yyh 수정
        # return str(self.hwmsuser) + ' ' + str(self.goods_nm)
        # return self.email

    class Meta:
        db_table = 'rsvmng'
        verbose_name = '주문'
        verbose_name_plural = '주문'




'''
    rsv_sn = models.IntegerField(primary_key=True, verbose_name='예약순번')
    chart_no = models.CharField( max_length=10, verbose_name='차트번호')
    cst_nm = models.CharField(max_length=60, verbose_name='고객명')

    BRANCH_ID = (
        ('푸미흥점', '푸미흥점'),
        ('2Q점', '2Q점'),
    )
    rsv_branch = models.CharField(max_length=60, choices=BRANCH_ID, blank=True, null=True,
                                verbose_name='예약사업장')

    rsv_dt = models.DateField(verbose_name='예약일')
    # 추가해야할 필드 : 요일 계산 함수에 의해 해당 요일 표기

    RSV_TIME = (
        ('10:30', '10:30'),
        ('11:00', '11:00'),
        ('11:30', '11:30'),
        ('13:00', '13:00'),
        ('13:30', '13:30'),
        ('14:00', '14:00'),
        ('14:30', '14:30'),
        ('15:00', '15:00'),
        ('15:30', '15:30'),
        ('16:00', '16:00'),
        ('16:30', '16:30'),
        ('17:00', '17:00'),
        ('17:30', '17:30'),
    )
    rsv_time = models.CharField(max_length=5, choices=RSV_TIME, blank=True, null=True, default='',
                                  verbose_name='예약시간')

    goods_nm = models.CharField(max_length=100, verbose_name='고객희망시술내용')

    CLINIC_ID = (
        ('초진', '초진'),
        ('재진', '재진'),
    )
    clnic_cd = models.CharField(max_length=16, choices=CLINIC_ID, blank=True, null=True, default='재진',
                                verbose_name='초진재진구분')

    STATUS_ID = (
        ('예약', '예약'),
        ('접수', '접수'),
        ('수납대기', '수납대기'),
        ('시술', '시술'),
        ('수납완료', '수납완료'),
        ('예약취소', '예약취소'),
        ('미방문', '미방문'),
    )
    rsv_stt_cd = models.CharField(max_length=16, choices=STATUS_ID, blank=True, null=True, default='예약',
                                  verbose_name='현재상태')

    frst_reg_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    # def __str__(self):
    #     return self.chart_no

    def __str__(self):
        return 'Name: %s title: %s' % (self.chart_no, self.cst_nm)

    class Meta:
        db_table = 'rsvmng'
        verbose_name = '예약관리'
        verbose_name_plural = '예약관리'
'''