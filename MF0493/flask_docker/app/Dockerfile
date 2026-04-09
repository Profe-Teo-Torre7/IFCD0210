FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install flask gunicorn

CMD ["gunicorn","-b","0.0.0.0:8000","app:app"]