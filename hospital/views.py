from django.shortcuts import render, redirect
from .models import Doctor
from .forms import AppointmentForm

def home(request):
    doctors = Doctor.objects.all()
    return render(request, 'home.html', {'doctors': doctors})

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # بعد از ثبت، برگرد به صفحه اصلی
    else:
        form = AppointmentForm()
    
    return render(request, 'appointment.html', {'form': form})