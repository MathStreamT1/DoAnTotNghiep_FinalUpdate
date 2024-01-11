from django import forms
from .models import OLP,ICPC,PROCON

class OLPForm(forms.ModelForm):
    class Meta:
        model = OLP
        fields = ['rank', 'description', 'khoa', 'system', 'year', 'certificate']

class OLPDeleteForm(forms.Form):
    confirm = forms.BooleanField(required=True, initial=False, widget=forms.HiddenInput)


class ICPCForm(forms.ModelForm):
    class Meta:
        model = ICPC
        fields = ['khoa','team_name', 'result', 'scope', 'year', 'certificate']


class ICPCDeleteForm(forms.Form):
    confirm = forms.BooleanField(required=True, initial=False, widget=forms.HiddenInput)


class PROCONForm(forms.ModelForm):
    class Meta:
        model = PROCON
        fields = ['year','team_name', 'result','certificate']

class PROCONDeleteForm(forms.Form):
    confirm = forms.BooleanField(required=True, initial=False, widget=forms.HiddenInput)