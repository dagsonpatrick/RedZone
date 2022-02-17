from django import forms
from django.contrib.auth.forms import AuthenticationForm
from upload_validator import FileTypeValidator
from .models import Usuario
from django.core.exceptions import NON_FIELD_ERRORS
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import (
     password_validation
)
class UsuarioForm(forms.ModelForm):

    error_messages = {
        'password_mismatch': _("Os dois campos de senha não coincidem."),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Digite a mesma senha da anterior, para verificação."),
    )

    #password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    #password2 = forms.CharField(label='Confirmacao Senha', widget=forms.PasswordInput)

    profile_picture = forms.FileField(
        label='profile_picture', help_text = _("Formatos aceitos: JPEG ou PNG"), required = False,
        validators=[FileTypeValidator(
            allowed_types = ['image/jpeg','image/png']
        )]
    )


    class Meta:
        model = Usuario
        fields = [ 'email', 'first_name', 'last_name']
        exclude = ['profile_picture']

        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class ProfilePictureForm(forms.ModelForm):
    profile_picture = forms.FileField(
        help_text="Somente formatos de imagem são aceitos.",
        validators=[FileTypeValidator(
            allowed_types=['image/jpeg','image/png']
        )]
    )

    class Meta:
        model = Usuario
        fields = ['profile_picture']

class LoginForm(AuthenticationForm):
    username = forms.EmailField()
    class Meta:
        model = Usuario
        fields = ['username', 'password']