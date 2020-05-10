from django import forms
from .models import Tshirt

class TshirtForm(forms.ModelForm):

    class Meta:
        model = Tshirt
        fields = ['brand', 'design', 'size', 'video', 'image', ]

# TODO: add a way to add stories to T-shirts (1 T-shirt has multiple stories / story to user is 1:1)

#Contact form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True)
