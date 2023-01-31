from django.urls import path

from funny.apps import FunnyConfig
from funny.formset_views import StudentUpdateWithSubjectsView
from funny.views import hello, contacts, StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView, \
    StudentDetailView, change_status

app_name = FunnyConfig.name

urlpatterns = [
    path('', hello, name='home'),
    path('contacts/', contacts, name='contacts'),

    path('list/', StudentListView.as_view(), name='list'),
    path('create/', StudentCreateView.as_view(), name='create'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='update'),
    path('update/<int:pk>/subjects/', StudentUpdateWithSubjectsView.as_view(), name='update_with_subjects'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', StudentDetailView.as_view(), name='detail'),

    path('status/<int:pk>/', change_status, name='status'),
]
