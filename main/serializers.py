from rest_framework import serializers
from .models import *


class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = UserCustom
        fields = '__all__'

class MedicoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class PasienteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Pasiente
        fields = '__all__'

class AreaSerializer (serializers.ModelSerializer):
    class Meta:
        model = AreasMedicasabs
        fields = '__all__'

class RecetasSerializer (serializers.ModelSerializer):
    class Meta:
        model = Recetas
        fields = '__all__'
