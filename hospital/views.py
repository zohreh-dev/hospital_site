from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Doctor, Appointment
from .forms import AppointmentForm

def home(request):
    doctors = Doctor.objects.all()
    return render(request, 'home.html', {'doctors': doctors})

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AppointmentForm()
    
    return render(request, 'appointment.html', {'form': form})

@login_required
def patient_dashboard(request):
    appointments = Appointment.objects.filter(patient__user=request.user).order_by('-date')
    return render(request, 'dashboard.html', {'appointments': appointments})

# 👇 این تابع جدید برای پنل پزشک است 👇
@login_required
def doctor_dashboard(request):
    # فقط نوبت‌هایی که پزشکشان همان کاربر لاگین‌کرده است را نشان بده
    appointments = Appointment.objects.filter(doctor__user=request.user).order_by('-date')
    return render(request, 'doctor_dashboard.html', {'appointments': appointments})