from django import forms
from ofertas.models import DescripcionCargo, Empresa


class OfertaForm(forms.ModelForm):

    class Meta:
        model = DescripcionCargo
        exclude = []
