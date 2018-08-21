FROM python:2.7-slim

RUN adduser magalu

WORKDIR /home/magalu/app

COPY . .
RUN pip install -r requirements.txt

EXPOSE 8000
ENTRYPOINT gunicorn --bind 0.0.0.0:8000 wsgi
