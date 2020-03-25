from django import forms
from .models import Tshirt

class TshirtForm(forms.ModelForm):

    class Meta:
        model = Tshirt
        fields = ['brand', 'design', 'size', 'video', 'image']
