from django import forms

# --authentication of user against database--|
# --PasswordInput widget render the password HTML element,
# --This will include type="password" in the HTML so browser treats it as a password input
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)