FROM python:2.7-slim

RUN adduser magalu

WORKDIR /home/magalu/app

COPY . .
RUN pip install -r requirements.txt

ENV FLASK_APP run.py

EXPOSE 5000
ENTRYPOINT flask run
