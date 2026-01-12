FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install flask gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
