from django.db import models

# Create your models here.

class GoodsModel(models.Model):
    # goods_cd = models.CharField(max_length=6, verbose_name='상품코드')
    # id = models.AutoField(primary_key=True)
    goods_cd = models.CharField(primary_key=True, max_length=10, verbose_name='상품코드')
    goods_nm = models.CharField(max_length=100, verbose_name='상품명')
    sub_clas_cd = models.CharField(max_length=10, verbose_name='대분류코드')
    sub_clas_nm = models.CharField(max_length=60, verbose_name='대분류명')
    maj_clas_cd = models.CharField(max_length=10, verbose_name='범주코드')
    maj_clas_nm = models.CharField(max_length=60, verbose_name='범주명')
    cat_cd = models.CharField(max_length=10, verbose_name='카테고리코드')
    cat_nm = models.CharField(max_length=60, verbose_name='카테고리명')


    GOODS_ID = (
        ('1', '일반상품'),
        ('2', '이벤트상품'),
    )
    goods_at = models.CharField(max_length=1, choices=GOODS_ID, blank=True, null=True, default='1', verbose_name='일반이벤트구분')

    goods_amt = models.IntegerField(verbose_name='상품가격')

    TAX_ID = (
        ('1', '과세'),
        ('2', '비과세'),
    )
    tax_at = models.CharField(max_length=1, choices=TAX_ID, blank=True, null=True, default='2', verbose_name='과세여부')

    TERA_ID = (
        ('1', '여'),
        ('2', '부'),
    )
    tera_at = models.CharField(max_length=1, choices=TERA_ID, blank=True, null=True, default='1', verbose_name='의사시술여부')

    tera_add_days = models.PositiveSmallIntegerField(verbose_name='시술추가일수')
    atpn_dsc = models.CharField(max_length=60, verbose_name='주의사항')
    inf_msg = models.CharField(max_length=60, verbose_name='안내메시지')
    sch_ltr_days = models.PositiveSmallIntegerField(verbose_name='이후안내예정일수')

    fac_nm = models.CharField(max_length=60, verbose_name='시설명')   # 코드테이블에서 읽어 리스트형으로 변환할 것.
    flor_nm = models.CharField(max_length=60, verbose_name='층명')   # 코드테이블에서 읽어 리스트형으로 변환할 것.
    bed_nm = models.CharField(max_length=60, verbose_name='베드명')   # 코드테이블에서 읽어 리스트형으로 변환할 것.

    adv_dtl_char = models.TextField(verbose_name='상품광고 설명')
    frst_reg_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')


    def __str__(self):
        return self.goods_nm

    class Meta:
        db_table = 'goodscdmng'
        verbose_name = '상품관리'
        verbose_name_plural = '상품관리'
