from django import forms

class info(forms.Form):
    comentario=forms.CharField(max_length=200,widget=forms.Textarea(attrs={'class': 'input'}))
    