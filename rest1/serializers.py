from rest_framework import routers, serializers, viewsets
from rest1.models import *
# Serializers define the API representation.
class DataSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSheet
        fields = ['id','descripcion','historical_data']
        
class CustomerSerializer(serializers.ModelSerializer):
    num_professions =serializers.SerializerMethodField()
    data_sheet= DataSheetSerializer()
    class Meta:
        model = Customer
        fields = ['id','name','address','profession',
        'num_professions','data_sheet','active',
        'status_message']
    def get_num_professions(self,obj):
        return obj.num_professions()
class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['id','descripcion']




class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Document
        fields = ['id','dtype','doc_number','customer']
