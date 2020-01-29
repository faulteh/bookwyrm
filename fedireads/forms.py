''' usin django model forms '''
from django.forms import ModelForm, PasswordInput

from fedireads import models


class LoginForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['username', 'password']
        help_texts = {f: None for f in fields}
        widgets = {
            'password': PasswordInput(),
        }


class RegisterForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['username', 'email', 'password']
        help_texts = {f: None for f in fields}
        widgets = {
            'password': PasswordInput(),
        }


class ReviewForm(ModelForm):
    class Meta:
        model = models.Review
        fields = ['name', 'review_content', 'rating']
        help_texts = {f: None for f in fields}
        labels = {
            'name': 'Title',
            'review_content': 'Review',
            'rating': 'Rating (out of 5)',
        }


class EditUserForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['avatar', 'name', 'summary']
        help_texts = {f: None for f in fields}