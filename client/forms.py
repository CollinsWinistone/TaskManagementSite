from django import forms
from django.utils.text import slugify
from .models import Client

class ClientRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    phone_number = forms.CharField(max_length=15)
    description = forms.CharField(max_length=50)
    client_score = forms.IntegerField()

    class Meta:
        model = Client
        fields = '__all__'

    def save(self, commit=True):
        client = super(ClientRegistrationForm, self).save(commit=False)
        client.first_name = self.cleaned_data['first_name']
        client.last_name = self.cleaned_data['last_name']
        client.phone_number = self.cleaned_data['phone_number']
        client.description = self.cleaned_data['description']
        client.client_score = self.cleaned_data['client_score']
        client.save()
        print("client saved....")
    

        if commit:
            client.save()

        return client
    
    def __init__(self, *args, **kwargs):
        super(ClientRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Social Name'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Name'
        # self.fields['status'].widget.attrs['class'] = 'form-control'
        # self.fields['status'].widget.attrs['placeholder'] = 'Email'
        # self.fields['due'].widget.attrs['class'] = 'form-control'
        # self.fields['due'].widget.attrs['placeholder'] = 'City'
        # self.fields['assign'].widget.attrs['class'] = 'form-control'
        # self.fields['assign'].widget.attrs['placeholder'] = 'Found date'