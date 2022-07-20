from rest_framework import serializers
from .models import Code,Category


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Code
        fields= ('__all__')
        
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields= ('__all__')
        

