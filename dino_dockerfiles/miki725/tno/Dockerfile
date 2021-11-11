FROM python:3.5
MAINTAINER "Miroslav Shubernetskiy"

WORKDIR /www

ENV DJANGO_SETTINGS_MODULE=tno.settings.prod
ENV DJANGO_CONFIGURATION=Prod

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    libpq-dev \
    nodejs-legacy \
    npm

RUN npm install -g \
    less \
    yuglify

# cleanup
RUN apt-get clean && \
    rm -rf /var/cache/apt

COPY requirements.txt /www/requirements.txt

RUN pip install -r /www/requirements.txt

COPY tno/ /www

EXPOSE 8888

CMD newrelic-admin run-python \
    /usr/local/bin/gunicorn --config gunicorn.py tno.wsgi:application
