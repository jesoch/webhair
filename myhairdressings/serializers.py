from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers

class HairdressingSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Hairdressing
        fields = ('id', 'name', 'street', 'number', 'zipcode','phone', 'description', )

class HairdresserSerializer(HyperlinkedModelSerializer):
    Hairdressing = HyperlinkedIdentityField(view_name='hairdressing_detail')
    class Meta:
        model = Hairdresser
        fields = ('id', 'name', 'speciality', 'Hairdressing')

class ScheduleSerializer(HyperlinkedModelSerializer):
    hairdresser = HyperlinkedRelatedField(read_only=True,view_name='hairdresser_detail')
    class Meta:
        model = Schedule
        fields = ('id', 'day', 'hour', 'hairdresser')

class CitationSerializer(HyperlinkedModelSerializer):
    id_user = HyperlinkedRelatedField(read_only=True, view_name='user_detail')
    id_schedule = HyperlinkedRelatedField(read_only=True, view_name='schedule_detail')
    class Meta:
        model = Citation
        fields = ('id', 'id_user', 'id_schedule')

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',)
