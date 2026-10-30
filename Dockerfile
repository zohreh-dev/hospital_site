# استفاده از نسخه رسمی پایتون (سبک‌شده)
FROM python:3.12-slim

# تنظیم متغیرهای محیطی
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# تعیین پوشه کاری
WORKDIR /app

# نصب پیش‌نیازهای سیستم‌عامل لینوکس
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# کپی کردن فایل نیازمندی‌ها و نصب آن‌ها
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن کل کدهای پروژه
COPY . /app/

# 👇 این خط مهم‌ترین بخشه: ساخت ادمین + اجرای سرور
CMD python manage.py collectstatic --no-input && python manage.py migrate && python create_admin.py && gunicorn config.wsgi:application --bind 0.0.0.0:8000