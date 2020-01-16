from django import forms

class idname_uid(forms.Form):
    idname = forms.CharField()
    uid = forms.CharField()