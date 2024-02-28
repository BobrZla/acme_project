from typing import Any
from django import forms
from django.core.exceptions import ValidationError

from .models import Birthday


BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


class BirthdayForm(forms.ModelForm):

    class Meta:
        model = Birthday
        fields = "__all__"
        widgets = {"birthday": forms.DateInput(attrs={"type": "date"})}

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.split()[0]

    def clean(self):
        super().clean()
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        if f'{first_name} {last_name}' in BEATLES:
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
            )


# class ContestForm(forms.Form):
#     title = forms.CharField(max_length=20, label="Название")
#     description = forms.CharField(
#         widget=forms.Textarea(attrs={"cols": 70, "rows": 5}), label="Описание"
#     )
#     price = forms.IntegerField(
#         max_value=100,
#         min_value=10,
#         label="Цена",
#         help_text="Рекомендованная розничная цена"
#     )
#     comment = forms.CharField(
#         widget=forms.Textarea(),
#         label="Комментарий",
#         required=False
#     )
        

# # birthday/forms.py
# from django import forms

# # Импортируем функцию-валидатор.
# from .validators import real_age


# class BirthdayForm(forms.Form):
#     first_name = forms.CharField(label='Имя', max_length=20)
#     last_name = forms.CharField(
#         label='Фамилия', required=False, help_text='Необязательное поле'
#     )
#     birthday = forms.DateField(
#         label='Дата рождения',
#         widget=forms.DateInput(attrs={'type': 'date'}),
#         # В аргументе validators указываем список или кортеж 
#         # валидаторов этого поля (валидаторов может быть несколько).
#         validators=(real_age,), ВАЛИДАТОР
#     )         
