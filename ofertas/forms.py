from django import forms
from ofertas.models import DescripcionCargo, Empresa, Postular


class OfertaForm(forms.ModelForm):

    class Meta:
        model = DescripcionCargo
        exclude = []


class PostularForm(forms.ModelForm):

    class Meta:
        model = Postular
        fields = [
            'postulante_oferta',
            'nivel_educacional',
            'carrera',
            'experiencia',
            'descripcion_breve'
        ]

        labels = {
            'postulante_oferta': 'Postulante',
            'nivel_educacional': 'Nivel educacional',
            'carrera': 'Carrera',
            'experiencia': 'Experiencia',
            'descripcion_breve': 'Descripcion breve'
        }

        widgets = {
            'nivel_educacional':forms.TextInput(attrs={'class': 'form-control'}),
            'carrera':forms.TextInput(attrs={'class': 'form-control'}),
            'experiencia':forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion_breve':forms.TextInput(attrs={'class': 'form-control'}),
        }