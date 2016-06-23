from django import forms


class LoginForm(forms.Form):

    username = forms.SlugField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'required': 'true',
            }
        ),
        label="Username",
    )

    password = forms.CharField(
        max_length=50, 
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'required': 'true',
            }
        ),
        label="Password",
    )


class RegisterForm(forms.Form):

    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'required': 'true',
            },
        ),
        label='First name',
    )

    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'required': 'true',
            },
        ),
        label='Last name',
        required=True,
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'required': 'true',
            },
        ),
        label='Email',
        required=True,
    )

    username = forms.SlugField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'required': 'true',
            }
        ),
        label="Username",
        required=True,
    )

    password = forms.CharField(
        max_length=50, 
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'required': 'true',
            }
        ),
        label="Password",
        required=True,
    )