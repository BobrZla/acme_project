from django import forms


class BirthdayForm(forms.Form):
    first_name = forms.CharField(max_length=20, label="Имя")
    last_name = forms.CharField(
        required=False, label="Фамилия", help_text="Необязательное поле"
    )
    birthday = forms.DateField(
        label="Дата рождения", widget=forms.DateInput(attrs={"type": "date"})
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
