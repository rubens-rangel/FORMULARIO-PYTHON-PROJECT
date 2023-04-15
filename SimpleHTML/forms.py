from django import forms


class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    telefone = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=100)
    mensagem = forms.CharField(widget=forms.Textarea)
