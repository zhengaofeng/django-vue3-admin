from django.db import models

# Create your models here.
from backend.dvadmin.utils.models import CoreModel


class CrudDemoModel(CoreModel):
    goods = models.CharField(max_length=255, verbose_name="商品名称")
    inventory = models.IntegerField(verbose_name="库存数量")
    goods_price = models.FloatField(verbose_name="商品价格")
    purchase_goods_date = models.DateTimeField(verbose_name="采购时间")

    class Meta:
        db_table = "goods"
        verbose_name = "商品表"
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)
