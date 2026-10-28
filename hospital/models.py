from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دپارتمان")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دپارتمان"
        verbose_name_plural = "دپارتمان‌ها"


class Doctor(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True, blank=True, verbose_name="کاربر")
    first_name = models.CharField(max_length=50, verbose_name="نام")
    last_name = models.CharField(max_length=50, verbose_name="نام خانوادگی")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="دپارتمان")
    specialty = models.CharField(max_length=100, verbose_name="تخصص")

    def __str__(self):
        return f"دکتر {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "پزشک"
        verbose_name_plural = "پزشکان"


class Patient(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True, blank=True, verbose_name="کاربر")
    first_name = models.CharField(max_length=50, verbose_name="نام")
    last_name = models.CharField(max_length=50, verbose_name="نام خانوادگی")
    phone = models.CharField(max_length=15, verbose_name="شماره تماس")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "بیمار"
        verbose_name_plural = "بیماران"


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="پزشک")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="بیمار")
    date = models.DateField(verbose_name="تاریخ")
    time = models.TimeField(verbose_name="ساعت")
    is_active = models.BooleanField(default=True, verbose_name="فعال")

    def __str__(self):
        return f"نوبت {self.patient} با {self.doctor}"

    class Meta:
        verbose_name = "نوبت"
        verbose_name_plural = "نوبت‌ها"