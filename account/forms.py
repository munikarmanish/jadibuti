from django import forms


class LoginForm(forms.Form):

    username = forms.SlugField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'required': 'true',
                'placeholder': 'Enter your username',
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
                'placeholder': 'Enter your password',
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
                'placeholder': 'Eg: John',
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
                'placeholder': 'Eg: Doe',
            },
        ),
        label='Last name',
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'required': 'true',
                'placeholder': 'Eg: john@doe.com',
            },
        ),
        label='Email',    )

    username = forms.SlugField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'required': 'true',
                'placeholder': 'Eg: johndoe',
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
                'placeholder': 'Make it secure',
            }
        ),
        label="Password",
    )