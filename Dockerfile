# Dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app
Expose 8080

CMD ["python", "app.py"]

