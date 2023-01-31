from django.contrib import admin

from funny.models import Student, Subject

# admin.site.register(Student)

admin.site.register(Subject)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',)
    search_fields = ('first_name', 'last_name',)
    list_filter = ('last_name',)
