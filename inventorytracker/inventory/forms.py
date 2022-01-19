from django import forms
from .models import Location


class CreateItemForm(forms.Form):
    your_name = forms.CharField(label='Name of item', max_length=50)
    your_description = forms.CharField(label='Description', max_length=200)
    your_count = forms.IntegerField(label='Count (How many items?)')
    your_location = forms.ModelChoiceField(label="Your location", widget=forms.Select, queryset=Location.objects.all())


class LocationForm(forms.Form):
    your_city_name = forms.CharField(label='City name', max_length=50)