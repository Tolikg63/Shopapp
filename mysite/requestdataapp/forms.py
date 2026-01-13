from django import forms


class UserBioForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    age = forms.IntegerField(required=True, min_value=1, max_value=100)