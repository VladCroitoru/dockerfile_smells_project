FROM python:3.5.2

MAINTAINER tecnologia@scielo.org

RUN apt-get update && apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor

COPY requirements.txt /app/requirements.txt
COPY production.ini-TEMPLATE /app/production.ini-TEMPLATE
COPY docker/generate_production_ini.py /app/docker/generate_production_ini.py
COPY docker/entrypoint.sh /app/docker/entrypoint.sh
COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install gunicorn

ENV ACCESSSTATS_SETTINGS_FILE=/app/production.ini

EXPOSE 11620
EXPOSE 8000

ADD docker/entrypoint.sh /app/docker/entrypoint.sh
RUN chmod +x /app/docker/entrypoint.sh

ENTRYPOINT [ "/app/docker/entrypoint.sh" ]
