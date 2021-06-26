from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.StringRelatedField(many=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'parent', 'children']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"