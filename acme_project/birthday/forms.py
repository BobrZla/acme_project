from django import forms


from .models import Birthday


class BirthdayForm(forms.ModelForm):

    class Meta:
        model = Birthday
        fields = "__all__"
        widgets = {"birthday": forms.DateInput(attrs={"type": "date"})}


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
