from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):

    username = forms.CharField(
        required = True,
        label='ID',
        widget=forms.TextInput(
            attrs={
                'class': 'username',
                'placeholder': 'Required',
                'maxlength': 255,
            }
        ),
        error_messages={
            'required': '아이디를 입력하세요.',
        }
    )

    email = forms.EmailField(
        required = True,
        label='E-mail',
        widget=forms.TextInput(
            attrs={
                'class': 'email',
                'placeholder': 'Required',
                'maxlength': 255,
            }
        ),
        error_messages={
            'required': '이메일을 입력하세요.',
        }
    )

    date_of_birth = forms.DateField(
    required = False,
    label='Date of Birth',
    widget=forms.DateInput(
        attrs={
            'placeholder': 'yy-mm-dd',
            'type' : 'date' ,
            'size': 40,
        }
    ))

    instagram_url = forms.CharField(
    required = False,
    label='Instagram',
    widget=forms.TextInput(
        attrs={
            'placeholder': 'option',
            'maxlength': 255,
            'size': 40,

        }
    ))

    twitter_url = forms.CharField(
    required = False,
    label='Twitter',
    widget=forms.TextInput(
        attrs={
            'placeholder': 'option',
            'maxlength': 255,
            'size': 40,

        }
    ))
    facebook_url = forms.CharField(
    required = False,
    label='Facebook',
    widget=forms.TextInput(
        attrs={
            'placeholder': 'option',
            'maxlength': 255,
            'size': 40,

        }
    ))
    youtube_url = forms.CharField(
    required = False,
    label='Youtube',
    widget=forms.TextInput(
        attrs={
            'placeholder': 'option',
            'maxlength': 255,
            'size': 40,

        }
    ))


    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email','date_of_birth','instagram_url','twitter_url','facebook_url','youtube_url','profile_pic')



class CustomUserChangeForm(forms.ModelForm):

    email = forms.EmailField(
        required = True,
        label='E-mail',
        widget=forms.TextInput(
            attrs={
                'class': 'email',
                'placeholder': 'Required',
                'maxlength': 255,
            }
        ),
        error_messages={
            'required': '이메일을 입력하세요.',
        }
    )

    date_of_birth = forms.DateField(
    required = False,
    label='Date of Birth',
    widget=forms.DateInput(
        attrs={
            'placeholder': 'yy-mm-dd',
            'type' : 'date' ,
            'size': 40,
        }
    ))

    instagram_url = forms.CharField(
    required = False,
    label='Instagram',
    widget=forms.TextInput(
        attrs={
            'placeholder': 'option',
            'maxlength': 255,
            'size': 40,

        }
    ))

    twitter_url = forms.CharField(
    required = False,
    label='Twitter',
    widget=forms.TextInput(
        attrs={
            'placeholder': 'option',
            'maxlength': 255,
            'size': 40,

        }
    ))
    facebook_url = forms.CharField(
    required = False,
    label='Facebook',
    widget=forms.TextInput(
        attrs={
            'placeholder': 'option',
            'maxlength': 255,
            'size': 40,

        }
    ))
    youtube_url = forms.CharField(
    required = False,
    label='Youtube',
    widget=forms.TextInput(
        attrs={
            'placeholder': 'option',
            'maxlength': 255,
            'size': 40,

        }
    ))



    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email','date_of_birth','instagram_url','twitter_url','facebook_url','youtube_url','profile_pic')
