from django.forms import ModelForm, TextInput
from .models import Good


class GoodForm(ModelForm):
    class Meta:
        model = Good
        fields = '__all__'
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'good_name'
            })
        }