# استفاده از نسخه رسمی پایتون (سبک‌شده)
FROM python:3.12-slim

# تنظیم متغیرهای محیطی برای جلوگیری از ساخت فایل‌های اضافی
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# تعیین پوشه کاری داخل داکر
WORKDIR /app

# نصب پیش‌نیازهای سیستم‌عامل لینوکس
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# کپی کردن فایل نیازمندی‌ها و نصب آن‌ها
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن کل کدهای پروژه به داخل داکر
COPY . /app/

# دستور اجرای سایت
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]