# my_project/my_app/serializers.py
from rest_framework import serializers

from my_app.models import MyModel

class MySerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'
