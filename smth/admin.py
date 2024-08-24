from django.contrib import admin
from .models import News, Teacher, Award, Contact, Application, Question, EducationalStandard, MaterialTechnicalSupport, Scholarship, PaidService, Controls
from django.http import HttpResponse
from io import BytesIO
from zipfile import ZipFile
import zipfile
from django.utils.translation import gettext_lazy as _
from django.db.models import QuerySet
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'text')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'created_at')
    search_fields = ('name', 'position', 'bio')

class AwardAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')

class EducationalStandardAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')

class MaterialTechnicalSupportAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')

class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')

class PaidServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')


class ControlsAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'position')
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'student_name', 'student_class', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'phone', 'student_name', 'student_class')
    list_per_page = 20
    actions = ['download_applications']
    @admin.action(description="Выгрузка заявок")
    def download_applications(self, request, qs:QuerySet):
        """
        Downloads all applications as a zip archive.
        """
        in_memory_zip = BytesIO()
        with ZipFile(in_memory_zip, 'w') as zf:
            for app in qs:
                zf.writestr(f'{app.pk}.txt', f'Name: {app.name}\nEmail: {app.email}\nPhone: {app.phone}\nStudent Name: {app.student_name}\nStudent Class: {app.student_class}\nPassport Data: {app.passport_data}\nParent Name: {app.parent_name}\nParent Passport Data: {app.parent_passport_data}\nFiles: {app.files.url}')

        response = HttpResponse(in_memory_zip.getvalue(), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename=applications.zip'
        return response

    download_applications.short_description = 'Download selected applications as a zip archive'

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('text', 'email')
    list_per_page = 20
    actions = ['download_questions']
    @admin.action(description="Выгрузка вопросов")
    def download_questions(self, request, qs:QuerySet):
        """
        Downloads all questions as a zip archive.
        """
        in_memory_zip = BytesIO()
        with ZipFile(in_memory_zip, 'w') as zf:
            for question in qs:
                zf.writestr(f'{question.pk}.txt', f'Text: {question.text}\nEmail: {question.email}')

        response = HttpResponse(in_memory_zip.getvalue(), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename=questions.zip'
        return response

    download_questions.short_description = 'Download selected questions as a zip archive'

admin.site.register(News, NewsAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(EducationalStandard, EducationalStandardAdmin)
admin.site.register(MaterialTechnicalSupport, MaterialTechnicalSupportAdmin)
admin.site.register(Scholarship, ScholarshipAdmin)
admin.site.register(PaidService, PaidServiceAdmin)
admin.site.register(Controls, ControlsAdmin)
