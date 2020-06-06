from django.forms import ModelForm
from . models import RouterProperties

class RouterDataForm(ModelForm):
    class Meta:
        model = RouterProperties
        fields = ['SAPId', 'HOSTNAME', 'LoopBack', 'MacAddress']
