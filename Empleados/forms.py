from .models import *
from django import forms
from django.forms import ModelForm

class formulario_empleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['username', 'first_name', 'last_name', 'email', 'dni', 'dirección', 'telefono']

    def __init__(self, *args, **kwargs):
        super(formulario_empleado, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input-estilo'})

class crear_empleado(forms.ModelForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=True)
    password_confirm = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput, required=True)

    class Meta:
        model = Empleado
        fields = ['username', 'first_name', 'last_name', 'email', 'dni', 'dirección', 'telefono', 'password', 'password_confirm']

    def __init__(self, *args, **kwargs):
        super(crear_empleado, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input-estilo'})

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password != password_confirm:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

    def save(self):
        empleado = super().save(commit=False)
        empleado.set_password(self.cleaned_data['password'])
        empleado.save()
        return empleado


class Cambiar_Password(forms.ModelForm):
    password_actual = forms.CharField(label="Contraseña Actual", widget=forms.PasswordInput, required=True)
    password = forms.CharField(label="Nueva Contraseña", widget=forms.PasswordInput, required=True)
    password_confirm = forms.CharField(label="Confirmar Nueva Contraseña", widget=forms.PasswordInput, required=True)

    class Meta:
        model = Empleado
        fields = ['password_actual', 'password', 'password_confirm']

    def __init__(self, *args, **kwargs):
        super(Cambiar_Password, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input-estilo'})

    def clean(self):
        cleaned_data = super().clean()
        password_actual = cleaned_data.get("password_actual")
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        username = self.instance.username  
        if password:
            if password_actual and not self.instance.check_password(password_actual):
                raise forms.ValidationError("La contraseña actual es incorrecta.")
            if password and password != password_confirm:
                raise forms.ValidationError("Las contraseñas no coinciden.")
            if len(password) < 8:
                raise forms.ValidationError("La nueva contraseña debe tener al menos 8 caracteres.")
            if not any(char.isdigit() for char in password):
                raise forms.ValidationError("La nueva contraseña debe contener al menos un número.")
            if not any(char.isalpha() for char in password):
                raise forms.ValidationError("La nueva contraseña debe contener al menos una letra.")
            if password == password_actual:
                raise forms.ValidationError("La nueva contraseña no puede ser igual a la contraseña actual.")
            if password == username:
                raise forms.ValidationError("La nueva contraseña no puede ser igual al nombre de usuario.")
        return cleaned_data

    def save(self):
        empleado = super().save(commit=False)
        empleado.set_password(self.cleaned_data['password'])
        empleado.save()
        return empleado
