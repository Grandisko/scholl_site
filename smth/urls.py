from django.urls import path
from . import views
from django.conf.urls.static import static
from qwe import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('news/<pk>/', views.news_detail, name='news_detail'),
    path('teachers/', views.teachers, name='teachers'),
    path('teachers/<pk>/', views.teacher_detail, name='teacher_detail'),
    path('contact/', views.contact, name='contact'),
    path('apply/', views.apply, name='apply'),
    path('ask/', views.ask, name='ask'),
    path('educational_standards/', views.educational_standards, name='educational_standards'),
    path('material_technical_support/', views.material_technical_support, name='material_technical_support'),
    path('scholarships/', views.scholarships, name='scholarships'),
    path('paid_services/', views.paid_services, name='paid_services'),
    path('awards/', views.award_list, name='award_list'),
    path('controls/', views.controls_list, name='controls_list'),
    path('controls/<pk>/', views.control_detail, name='control_detail'),
    path('export/documents/', views.export_documents, name='export_documents'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)