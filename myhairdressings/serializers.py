from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import AdminHairDressing

class HairdressingSerializer(HyperlinkedModelSerializer):
    #url = HyperlinkedIdentityField(view_name='hairdressing')
    #flight = HyperlinkedRelatedField(many=True, read_only=True, view_name='hairdressing-detail')
    name = CharField(read_only=True)
    class Meta:
        model = AdminHairDressing
        fields = ('id', 'name', 'street', 'number')
