from rest_framework import serializers
from coffee_chat.models import Application

class Serializers(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'name', 'target', 'place', 'time', 'contents')