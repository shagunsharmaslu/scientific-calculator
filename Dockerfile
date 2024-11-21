FROM python:3.8-slim-buster

WORKDIR /app

COPY app.py .

CMD ["python3", "app.py"]