from django.contrib import admin
from django.urls import path, include
from hospital import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', views.patient_dashboard, name='patient_dashboard'),
    
    # 👇 این خط جدید برای پنل پزشک است 👇
    path('doctor-dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
]