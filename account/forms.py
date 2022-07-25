# my import
from django import forms
from django.contrib.auth.models import User
from account.models import Profile

# --authentication of user against database--|
# --PasswordInput widget render the password HTML element,
# --This will include type="password" in the HTML so browser treats it as a password input
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# --User Registration model form 
# --with two additional fields password and password2
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)

    # -- In form include only this fields of the model.
    # --This fields will be validated based on their corresponding model field
    # -- username is a field defined with unique=True
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    # --method to check password match with each other 
    # --and not let form validate if password don't match
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'nt match. ')
        return cd['password'] 

# -------Users edits there profile------|
# --This will allow users to edit their first name, last name and email
# -- which are attribute of the build-in Django user model
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
# --This will allow users to edit the profile data that save in the custom Profile model
# -- Users will be able to edits the fields below
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_if_birth', 'photo')