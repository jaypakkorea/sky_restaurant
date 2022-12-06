from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _
from .custom_widgets import PreviewImageFileWidget


class RestaurantForm(forms.ModelForm):

    name = forms.CharField(
    label='Name',
    widget=forms.TextInput(
        attrs={
            'placeholder': 'name',
            'maxlength': 20,
            'size': 40,
            }
        )
    )


    adress = forms.CharField(
        label='Adress',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'adress',
                'maxlength': 50,
                'size': 40,
                }
            ),
        )


    stars = forms.IntegerField(
    label='Stars',
    widget=forms.NumberInput(
        attrs={
            'placeholder': '-',
            'min': 0,
            'max' : 3,
            }
        )
    )

    bestMenu = forms.CharField(
    label='Best Menu',
    widget=forms.TextInput(
        attrs={
            'placeholder': 'Best Menu',
            'maxlength': 100,
            'size': 40,
            }
        )
    )

    reason = forms.CharField(
    label='Comment',
    widget=forms.Textarea(
        attrs={
            'placeholder': 'Reason',
            'maxlength': 200,
            'rows' :4,
            'cols' :42,
            }
        )
    )

    mainImage = forms.ImageField(
    required = True,
    label='Image',
    widget=forms.ClearableFileInput(
        ),
    error_messages={
        'required': '사진을 입력하세요.',
    })

    class Meta:
        model = Restaurant
        exclude = ['user',]


class CommentForm(forms.ModelForm):
    
    content = forms.CharField(
    label='Comment',
    widget=forms.TextInput(
        attrs={
            'placeholder': 'plz share your opinion',
            'maxlength': 100,
            'size': 40,
            }
        )
    )
    class Meta:
        model = Comment
        exclude = ["restaurant",]
 
class ImageForm(forms.ModelForm):

    image = forms.ImageField(
    required = True,
    label='Image',
    widget=forms.ClearableFileInput(attrs={'multiple': True}),
    error_messages={
        'required': '사진을 입력하세요.',
    })

    
    class Meta:
        model = Images
        fields = ('image', )
        labels = {
            'image': _('Image'),
        }
        