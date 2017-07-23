from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from nusxchange.models import Profile
# from login_and_signup.models import Profile


# class UserForm(forms.ModelForm):
# 	password = forms.CharField(widget=forms.PasswordInput)#hide characters since password form
# 	class Meta:
# 		model = User
# 		fields = ['username','email','password']

# class UserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     age = forms.CharField(required=True)

#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2", "age")

#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.email = self.cleaned_data["email"]
#         user.age = self.cleaned_data["age"]
#         if commit:
#             user.save()
#         return user
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'nickname', 'gender', 'bio', 
            'accomodation', 'birth_date', 'age', 
            'school', 'university', 'major', 'nationality', 
            'interest', 'profile_picture'
            )
        bio = forms.CharField(widget=forms.Textarea)
        interest = forms.CharField(widget=forms.Textarea)
        widgets = {
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'btn btn-default dropdown-toggle'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows':'5'}), 
            'accomodation': forms.Select(attrs={'class': 'btn btn-default dropdown-toggle'}),
            'birth_date': forms.TextInput(attrs={'class': 'form-control'}),               
            'age': forms.TextInput(attrs={'class': 'form-control'}), 
            'school': forms.Select(attrs={'class': 'btn btn-default dropdown-toggle'}),
            'university': forms.TextInput(attrs={'class': 'form-control'}), 
            'major': forms.TextInput(attrs={'class': 'form-control'}), 
            'nationality': forms.Select(attrs={'tag': 'dropdown'}), 
            'interest': forms.TextInput(attrs={'class': 'form-control'}), 
        }
