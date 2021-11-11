FROM python:3.4
MAINTAINER "Miroslav Shubernetskiy"

COPY formslayer/ /www
COPY requirements.txt /www/requirements.txt

WORKDIR /www

ENV DJANGO_SETTINGS_MODULE=formslayer.settings.prod

RUN apt-get update && \
    apt-get install pdftk -y && \
    apt-get upgrade -y

# cleanup
RUN apt-get clean && \
    rm -rf /var/cache/apt

RUN pip install -r /www/requirements.txt


EXPOSE 8888
CMD newrelic-admin run-python \
    /usr/local/bin/gunicorn --config gunicorn.py formslayer.wsgi:application
