from django import forms
from .models import Tshirt, Story


class TshirtForm(forms.ModelForm):

    class Meta:
        model = Tshirt
        fields = ['brand', 'design', 'size', 'video', 'image']


class StoryForm(forms.ModelForm):
    '''
    This class will help adding story for a tshirt
    '''

    class Meta:
        model = Story
        fields = ['story', 'tshirt']


# TODO: add a way to add stories to T-shirts (1 T-shirt has multiple stories / story to user is 1:1)
