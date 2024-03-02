# from django.shortcuts import render, get_object_or_404, redirect
# # from django.core.paginator import Paginator
# from django.views.generic import (
#     ListView, CreateView, UpdateView, DeleteView, DetailView
# )    
# from django.urls import reverse_lazy

# from .forms import BirthdayForm
# from .utils import calculate_birthday_countdown
# from .models import Birthday


# class BirthdayMixin:
#     model = Birthday
#     success_url = reverse_lazy('birthday:list')


# class BirthdayFormMixin:
#     form_class = BirthdayForm
#     template_name = 'birthday/birthday.html'


# class BirthdayDetailView(DetailView):
#     model = Birthday
#     # template_name_suffix = '_detail'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['birthday_countdown'] = calculate_birthday_countdown(
#             self.object.birthday
#         )
#         return context


# class BirthdayListView(ListView):
#     model = Birthday
#     ordering = 'id'
#     paginate_by = 10


# class BirthdayCreateViews(CreateView, BirthdayMixin, BirthdayFormMixin):
#     pass


# class BirthdayUpdateView(UpdateView, BirthdayMixin, BirthdayFormMixin):
#     pass


# class BirthdayDeleteViews(DeleteView, BirthdayMixin):
#     pass


# # def birthday(request, pk=None):
# #     if pk is not None:
# #         instance = get_object_or_404(Birthday, pk=pk)
# #     else:
# #         instance = None
# #     print(request.POST)
# #     form = BirthdayForm(
# #         request.POST or None, files=request.FILES or None, instance=instance
# #     )
# #     context = {"form": form}

# #     if form.is_valid():
# #         birthday_countdown = calculate_birthday_countdown(form.cleaned_data["birthday"])
# #         context.update({"birthday_countdown": birthday_countdown})
# #         form.save()
# #     return render(request, "birthday/birthday.html", context)


# # def birthday_list(request):
# #     birthdays = Birthday.objects.order_by('id')
# #     paginator = Paginator(birthdays, 2)
# #     page_number = request.GET.get('page')
# #     page_obj = paginator.get_page(page_number)
# #     context = {"page_obj": page_obj}
# #     return render(request, "birthday/birthday_list.html", context)


# # def delete_birthday(request, pk):
# #     instance = get_object_or_404(Birthday, pk=pk)
# #     form = BirthdayForm(instance=instance)
# #     context = {"form": form}
# #     if request.method == "POST":
# #         instance.delete()
# #         return redirect("birthday:list")
# #     return render(request, "birthday/birthday.html", context)

#     # if request.GET:
#     #     form = BirthdayForm(request.GET)
#     #     if form.is_valid():
#     #         pass
#     # else:
#     #     form = BirthdayForm()
