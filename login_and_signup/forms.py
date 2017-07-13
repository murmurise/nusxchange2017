from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from login_and_signup.models import Profile


# class UserForm(forms.ModelForm):
# 	password = forms.CharField(widget=forms.PasswordInput)#hide characters since password form
# 	class Meta:
# 		model = User
# 		fields = ['username','email','password']

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    age = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "age")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.age = self.cleaned_data["age"]
        if commit:
            user.save()
        return user
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date')