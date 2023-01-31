from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView

from funny.forms import StudentForm
from funny.models import Student
from funny.services import handle_some_data


def hello(request):
    handle_some_data()
    context = {
        'object_list': Student.objects.all()
    }

    return render(request, 'funny/index.html', context)


def contacts(request):
    if request.method == 'POST':
        print(request.POST.get('name'))
        print(request.POST.get('email'))
        print(request.POST.get('message'))

    return render(request, 'funny/contacts.html')


class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status=Student.STATUS_INACTIVE)
        return queryset


class SomeView(TemplateView):
    template_name = 'funny/contacts.html'

    def get(self, *args, **kwargs):
        context = {

        }
        return render(self.request, self.template_name, context)


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('funny:list')
    extra_context = {
        'title': 'Создание студента'
    }


class StudentUpdateView(UpdateView):
    model = Student
    # fields = '__all__'
    # fields = ('first_name', 'last_name')
    form_class = StudentForm
    success_url = reverse_lazy('funny:list')


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('funny:list')


class StudentDetailView(DetailView):
    model = Student


def change_status(request, pk):
    # student_item = Student.objects.get(pk=pk)
    # student_item = Student.objects.filter(pk=pk).first()
    # if student_item:
    #     ...
    student_item = get_object_or_404(Student, pk=pk)
    if student_item.status == Student.STATUS_ACTIVE:
        student_item.status = Student.STATUS_INACTIVE
    else:
        student_item.status = Student.STATUS_ACTIVE
    student_item.save()

    res = send_mail(
        subject='Смена статуса',
        message=f'Для студента {student_item.first_name} {student_item.last_name} был изменен статус',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['info@oscar-studio.com'],
        fail_silently=False
    )

    # Attemp.objects.create(
    #     status=res,
    #     response=''
    # )

    return redirect(reverse('funny:list'))
