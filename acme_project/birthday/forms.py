from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from .models import Birthday, Congratulation


BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


YES_OR_NO = ((True, 'Yes'), (False, 'No'))


class BirthdayForm(forms.ModelForm):

    class Meta:
        model = Birthday
        exclude = ('author', 'diner',)
        widgets = {
            "birthday": forms.DateInput(attrs={"type": "date"}),
            "diner": forms.RadioSelect(choices=YES_OR_NO),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.split()[0]

    def clean(self):
        super().clean()
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        if f'{first_name} {last_name}' in BEATLES:
            send_mail(
                subject='Another Beatles member',
                message=f'{first_name} {last_name} пытался опубликовать запись!',
                from_email='birthday_form@acme.not',
                recipient_list=['admin@acme.not'],
                fail_silently=True,
            )
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
            )


class CongratulationForm(forms.ModelForm):

    class Meta:
        model = Congratulation
        fields = ('text',)



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
