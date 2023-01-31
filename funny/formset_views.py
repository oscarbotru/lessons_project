from django.db import transaction
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView

from funny.forms import SubjectForm, StudentForm
from funny.models import Student, Subject


class StudentUpdateWithSubjectsView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('myapp:list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        FormSet = inlineformset_factory(self.model, Subject, form=SubjectForm, extra=1)
        if self.request.method == 'POST':
            formset = FormSet(self.request.POST, instance=self.object)
        else:
            formset = FormSet(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        with transaction.atomic():
            if form.is_valid():
                self.object = form.save()  # Student
                if formset.is_valid():
                    formset.instance = self.object
                    formset.save()  # Subject

        return super().form_valid(form)
