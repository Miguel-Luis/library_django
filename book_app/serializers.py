from rest_framework import serializers
from .models import Category

'''Estos serializadores permiten que Django Rest Framework
convierta automáticamente los objetos Category o Book en un JSON
y viceversa. Esto facilita el envío y la recepción de datos a través de la API'''
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('created_at', 'id', 'name', 'description')
        read_only_fields = ('created_at', )