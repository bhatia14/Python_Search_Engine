'''
Created on Jun 7, 2015

@author: Rachit
'''
from django import forms
from myapp.models import Topic, ModelImageUpload
from django.conf.global_settings import EMAIL_BACKEND

TIME_CHOICES = (
        (0, 'No preference'),
        (1, 'Morning'),
        (2, 'Afternoon'),
        (3, 'Evening')
    )

INTERESTED = (
             (0, 'No'),
             (1, 'YES')
             )


class TopicForm(forms.ModelForm):
    class Meta:
        model= Topic
        fields=['subject','intro_course','time','avg_age']
        widgets={'time': forms.RadioSelect()}
        labels={
                'subject' : 'Subject',
                'intro_course' : 'This should be an intoductory level course',
                'time':'Preferred Time',
                'avg_age': 'What is your age?',
                }


class InterestForm(forms.Form):
    interested=forms.BooleanField(label='interested', required = False, widget=forms.RadioSelect(choices=INTERESTED))
   # name1 = forms.TextInput(attrs={'required': False})
    age =forms.IntegerField(label='age', initial=20)
    comments=forms.CharField(label='Additional Comments', widget=forms.Textarea, required=False, max_length=100)
    
    
    
class ForgotForm(forms.Form):
    email=forms.CharField(label="", required=True,max_length=100)
    
    
    
class RegisterForm(forms.Form):
    username=forms.CharField(label="Username:", required=True,max_length=20)
    firstname=forms.CharField(label="First Name:", required=True,max_length=20)
    lastname=forms.CharField(label="Last name:", required=True,max_length=20)
    email=forms.CharField(label="Email:", required=True,max_length=100)
    password=forms.CharField(label="Password:", required=True,max_length=20, widget=forms.PasswordInput)
    
    
class ModelImageUploadForm(forms.ModelForm):
    class Meta:
        model=ModelImageUpload
        fields=['name','image']
        widgets={'image': forms.ImageField()}
        
        