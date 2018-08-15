# encoding:utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _
from Universidad.Apps.ventas.models import Cliente


class NewClienteForm(forms.ModelForm):

	cedula = forms.CharField(
		label="Cedula", max_length=20, required=False,
		widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Cedula', 'pattern': '^\d{9,10}$',
			'title': 'Ingrese el nit sin codigo de verificacion'}))

	nombres = forms.CharField(
	max_length=50, required=True, label='Nombres',
	widget=forms.TextInput(attrs={
		'class': 'form-control', 'placeholder': '',
		'required': 'required'}))

	apellidos = forms.CharField(
	max_length=50, required=True, label='Apellidos',
	widget=forms.TextInput(attrs={
		'class': 'form-control', 'placeholder': '',
		'required': 'required'}))

	fecha_nacimiento = forms.DateField(
        label=_(u"Fecha de nacimiento"), widget=forms.TextInput(attrs={
            'class': 'form-control datepicker-min', 'placeholder': 'Fecha de nacimiento'}))

	email = forms.EmailField(
		label='Correo electrónico', required=False	,
		widget=forms.TextInput(attrs={
			'class': 'form-control', 'placeholder': 'Correo electrónico',
			'required': 'required', 'type': 'email'}))

	direccion = forms.CharField(
	label=_(u'Dirección'), required=False,
	widget=forms.Textarea(attrs={
		'rows': 1, 'class': 'form-control',
		'placeholder': _(u'Dirección')}))	


	celular  = forms.CharField(
		label="Telefono", max_length=20, required=False,
		widget=forms.TextInput(attrs={
			'class': 'form-control', 'type': 'tel',
			'placeholder': 'Celular', 'pattern': '^[3]\d{9}$',
			'title': 'Ingrese número celular sin espacios ni otros caracteres'}))

	class Meta:
		model = Cliente
		fields = [
			'cedula',
			'nombres',
			'apellidos',
			'fecha_nacimiento',
			'email' ,
			'direccion',
			'celular',
		]

		labels = {
			
		}

	def __init__(self, user=None, *args, **kwargs):
		super(NewClenteForm, self).__init__(*args, **kwargs)
		print "cliente ", user
		#self.fields['owner_usuario'].queryset = Usuarios.objects.filter(clientes=user,activo = True	)