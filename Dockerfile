# انتخاب تصویر پایه (Python 3.12.10)
FROM python:3.12.10

# تعیین دایرکتوری کاری داخل کانتینر
WORKDIR /app

# کپی کردن فایل‌های سورس از دایرکتوری فعلی به کانتینر
COPY . /app

# نصب کتاب‌خانه‌های مورد نیاز از فایل requirements.txt
RUN pip install --no-cache-dir -r req.txt

# اجرای فایل اصلی پایتون
CMD ["python", "main.py"]