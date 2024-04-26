from django import forms


class GameForm(forms.Form):
    game = forms.ChoiceField(label='Game', choices=[('coin', 'монета'), ('cube', 'кости'), ('number', 'числа')],
                             widget=forms.RadioSelect(attrs={
                                 'class': 'from-control',
                             }))
    count_game = forms.IntegerField(label='count_game', min_value=1, max_value=64,
                                    widget=forms.NumberInput(attrs={
                                        'class': 'from-control',
                                    }))
