from crud_demo.models import CrudDemoModel
from dvadmin.utils.serializers import CustomModelSerializer


class CrudDemoModelSerializer(CustomModelSerializer):
    class Meta:
        model = CrudDemoModel
        fields = "__all__"


class CrudDemoModelCreateUpdateSerializer(CustomModelSerializer):
    """
       创建/更新时的列化器
    """

    class Meta:
        model = CrudDemoModel
        fields = "__all__"


class CrudDemoModelImportSerializer(CustomModelSerializer):
    class Meta:
        model = CrudDemoModel
        fields = "__all__"


class ExportCrudDemoSerializer(CustomModelSerializer):
    class Meta:
        model = CrudDemoModel
        fields = "__all__"
