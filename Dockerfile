# استفاده از نسخه رسمی پایتون (سبک‌شده)
FROM python:3.12-slim

# تنظیم متغیرهای محیطی
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# تعیین پوشه کاری
WORKDIR /app

# نصب پیش‌نیازهای سیستم‌عامل لینوکس (برای دیتابیس PostgreSQL)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# کپی کردن و نصب پکیج‌های پایتون
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن کل کدها
COPY . /app/

# 👇 این خط مهم‌ترین تغییره: 
# ۱. فایل‌های استاتیک رو جمع می‌کنه
# ۲. جدول‌های دیتابیس رو می‌سازه (migrate)
# ۳. سرور رو با گانیکورن روی پورت ۸۰۰۰ بالا میاره
CMD python manage.py collectstatic --no-input && python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:8000