from rest_framework import serializers

from goods.models import SKU, GoodsCategory, SPUSpecification, SpecificationOption


class SKUSerialzier(serializers.ModelSerializer):
    """
        sku序列化器
    """

    class Meta:
        model = SKU
        fields = "__all__"


class GoodsCategorySerializer(serializers.ModelSerializer):
    """
        商品分类序列化器
    """

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class SpecificationOptionSerializer(serializers.ModelSerializer):
    # SPU规格序选项列化器
    class Meta:
        model = SpecificationOption
        fields = '__all__'


class SPUSpecificationSerializer(serializers.ModelSerializer):
    """
        SPU规格序列化器
    """
    options = SpecificationOptionSerializer(many=True)
    # specificationoption_set=SpecificationOption(many=True)

    class Meta:
        model = SPUSpecification
        fields = '__all__'
