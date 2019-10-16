from django import forms

class MakeAttack(forms.Form):
    name = forms.CharField(label="Name", max_length=16)
    check = forms.BooleanField()