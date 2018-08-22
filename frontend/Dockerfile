FROM python:2.7-slim

RUN adduser magalu

WORKDIR /home/magalu/app

COPY . .
RUN pip install -r requirements.txt

EXPOSE 8001
ENTRYPOINT ./start.sh
