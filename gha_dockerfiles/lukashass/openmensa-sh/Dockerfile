FROM python:3.9.6-alpine3.14

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY cron.txt /
RUN cat /cron.txt >> /var/spool/cron/crontabs/root
