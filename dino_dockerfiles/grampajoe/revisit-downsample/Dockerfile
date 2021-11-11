FROM python:2.7

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ENV PORT=5000
ENV WORKERS=2
ENV WORKER_CLASS=eventlet

COPY . /app

WORKDIR /app

CMD gunicorn downsample:app -k $WORKER_CLASS -w $WORKERS --access-logfile=- --error-logfile=- --log-file=- -b 0.0.0.0:$PORT
