from django.shortcuts import render

# Create your views here.
from crud_demo.models import CrudDemoModel
from crud_demo.serializers import CrudDemoModelSerializer, CrudDemoModelCreateUpdateSerializer, \
    CrudDemoModelImportSerializer, ExportCrudDemoSerializer
from dvadmin.utils.viewset import CustomModelViewSet


class CrudDemoModelViewSet(CustomModelViewSet):
    """
        list:查询
        create:新增
        update:修改
        retrieve:单例
        destroy:删除
    """
    # 功能说明:导入的配置
    import_field_dict = {
        "goods": "商品",
        "inventory": "库存量",
        "goods_price": "商品定价",
        "purchase_goods_date": "进货时间",
    }
    import_serializer_class = CrudDemoModelImportSerializer
    queryset = CrudDemoModel.objects.all()
    serializer_class = CrudDemoModelSerializer
    create_serializer_class = CrudDemoModelCreateUpdateSerializer
    update_serializer_class = CrudDemoModelCreateUpdateSerializer

    export_serializer_class = ExportCrudDemoSerializer
    export_field_label = {
        "goods": "商品",
        "inventory": "库存量",
        'goods_price': "商品定价",
        "purchase_goods_date": "进货时间",
    }
