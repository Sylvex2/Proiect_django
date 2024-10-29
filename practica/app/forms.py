from django import forms
from .models import Bypass, Statie, Depozit, Particular, Client, Test

class BypassForm(forms.ModelForm):
    class Meta:
        model = Bypass
        fields = [
            'motiv', 'sofer', 'transportator', 'cisterna', 
            'tip', 'tip_statie', 'cod_statie', 'info_statie', 
            'utilizator', 'observatii'
        ]
        widgets = {
            'cod_statie': forms.TextInput(attrs={'readonly': 'readonly'}),
            'info_statie': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    observatii = forms.CharField(
        widget=forms.Textarea(attrs={
            'id': 'id_observatii',
            'maxlength': 300,
            'required': 'required',
            'placeholder': 'Introduceți observațiile...',
            'rows': 6,
            'cols': 40,
        }),
        label='Observații'
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(BypassForm, self).__init__(*args, **kwargs)

        if user is not None:
            self.fields['utilizator'].initial = user
            self.fields['utilizator'].disabled = True

        # Adăugare câmp pentru numele stațiilor, inițial ascuns
        self.fields['nume_statie'] = forms.ChoiceField(
            choices=[('', 'Selectați un tip de stație mai întâi')],
            required=False
        )
        self.fields['nume_statie'].widget.attrs.update({
            'id': 'id_nume_statie',
            'style': 'display: none;',  # Ascuns implicit
            'onchange': 'populateStationInfo(this);'
        })
        
        # Actualizare câmp pentru tipul de stație pentru a afișa câmpul cu nume stație
        self.fields['tip_statie'].widget.attrs.update({
            'onchange': 'updateStationList(this);'
        })

        # Adăugare validare pentru câmpuri neobligatorii
        self.fields['motiv'].required = False
        self.fields['sofer'].required = False
        self.fields['transportator'].required = False
