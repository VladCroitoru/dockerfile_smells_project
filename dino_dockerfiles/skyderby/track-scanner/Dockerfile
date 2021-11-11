FROM python:3.6
MAINTAINER Aleksandr Kunin <skyksandr@gmail.com>

RUN mkdir -p /opt/app
WORKDIR /opt/app

COPY requirements.txt /opt/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /opt/app

RUN python build_models.py

EXPOSE 80

ENV WORKERS 1
ENV WORKER_THREADS 5

CMD gunicorn --workers $WORKERS --threads $WORKER_THREADS -b 0.0.0.0:80 tracksegmenter:app
