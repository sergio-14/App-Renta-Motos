# forms.py
from django import forms
from .models import Alquiler

class AlquilerForm(forms.ModelForm):
    tarifa_moto = forms.DecimalField(widget=forms.HiddenInput())

    class Meta:
        model = Alquiler
        fields = ['hora_inicio', 'hora_fin', 'cantidad_horas', 'estado', 'monto', 'cliente', 'moto', 'tarifa_moto']

    def __init__(self, *args, **kwargs):
        super(AlquilerForm, self).__init__(*args, **kwargs)
        self.fields['hora_inicio'].widget = forms.TimeInput(format='%H:%M', attrs={'type': 'time'})
        self.fields['hora_fin'].widget = forms.TimeInput(format='%H:%M', attrs={'type': 'time', 'onchange': 'calcularMonto()'})
        self.fields['monto'].widget = forms.NumberInput(attrs={'readonly': True})  # Mostrar el monto como solo lectura

        if 'instance' in kwargs and kwargs['instance'] and kwargs['instance'].moto:
            self.initial['tarifa_moto'] = kwargs['instance'].moto.tarifa
        else:
            self.fields['tarifa_moto'].widget.attrs['readonly'] = True

    class Media:
        js = ('js/calculo_monto.js',)  # Archivo JavaScript para el cálculo dinámico de monto
