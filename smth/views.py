from django.shortcuts import render, redirect
from .models import News, Teacher, Award, Contact, Application, Question, EducationalStandard, MaterialTechnicalSupport, Scholarship, PaidService, Controls
from .forms import ApplicationForm, QuestionForm
from django.db.models import Q
from django.shortcuts import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
import zipfile
from io import BytesIO

def index(request):
    return render(request, 'index.html', {'news': News.objects.all()})

def news_detail(request, pk):
    news = News.objects.get(pk=pk)
    return render(request, 'news_detail.html', {'news': news})
def teachers(request):
    return render(request, 'teachers.html', {'teachers': Teacher.objects.all()})

def teacher_detail(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    return render(request, 'teacher_detail.html', {'teacher': teacher})

def contact(request):
    return render(request, 'contact.html', {'contact': Contact.objects.all()})

def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ApplicationForm()
    return render(request, 'apply.html', {'form': form})

def ask(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = QuestionForm()
    return render(request, 'ask.html', {'form': form})

def educational_standards(request):
    return render(request, 'educational_standards.html',{'educational_standards': EducationalStandard.objects.all()})

def material_technical_support(request):
    return render(request, 'material_technical_support.html',{'material_technical_support':MaterialTechnicalSupport.objects.all()})

def scholarships(request):
    return render(request, 'scholarships.html',{'scholarships': Scholarship.objects.all()})

def paid_services(request):
    return render(request, 'paid_services.html',{'paid_services': PaidService.objects.all()})

def award_list(request):
    return render(request, 'award.html', {'awards': Award.objects.all()})

def controls_list(request):
    return render(request, 'controls_list.html', {'controls': Controls.objects.all()})

def control_detail(request, pk):
    control = Controls.objects.get(pk=pk)
    return render(request, 'control_detail.html', {'control': control})

@staff_member_required
def export_documents(request):
    documents = Document.objects.all()
    zip_file = BytesIO()
    with zipfile.ZipFile(zip_file, 'w') as zip:
        for document in documents:
            zip.write(document.file.path, document.file.name)

    response = HttpResponse(zip_file.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="documents.zip"'
    return response