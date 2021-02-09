from django import forms

class HellmailForm( forms.Form):
    subject = forms.CharField( label= "相手の名前", widget=forms.TextInput(attrs={"autocomplete":"off"}))
    sender = forms.EmailField( label = "あなたのメールアドレス", widget=forms.TextInput(attrs={"autocomplete":"off"}))