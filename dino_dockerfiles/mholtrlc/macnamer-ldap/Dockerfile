# Macnamer Dockerfile
# Version 0.1
FROM phusion/passenger-customizable:0.9.11

MAINTAINER Graham Gilbert <graham@grahamgilbert.com>

ENV HOME /root
#ENV DEBIAN_FRONTEND noninteractive
ENV APP_DIR /home/app/macnamer
ENV TZ Europe/London
ENV DOCKER_MACNAMER_TZ Europe/London
ENV DOCKER_MACNAMER_ADMINS Docker User, docker@localhost
ENV DOCKER_MACNAMER_LANG en_US

# Use baseimage-docker's init process.
CMD ["/sbin/my_init"]
RUN apt-get -y update
RUN /build/utilities.sh
RUN /build/python.sh

RUN apt-get -y install \
    python-setuptools \
    libpq-dev \
    python-dev \
    && easy_install pip

RUN git clone https://github.com/grahamgilbert/macnamer.git $APP_DIR
RUN pip install -r $APP_DIR/setup/requirements.txt
# RUN pip install psycopg2==2.5.3
RUN mkdir -p /etc/my_init.d
ADD nginx/nginx-env.conf /etc/nginx/main.d/
ADD nginx/macnamer.conf /etc/nginx/sites-enabled/macnamer.conf
ADD settings.py $APP_DIR/macnamer/
RUN mkdir -p $APP_DIR/macnamer/db
ADD settings_import.py $APP_DIR/macnamer/
ADD passenger_wsgi.py $APP_DIR/
ADD django/management/ $APP_DIR/namer/management/
ADD run.sh /etc/my_init.d/run.sh
RUN rm -f /etc/service/nginx/down
RUN rm -f /etc/nginx/sites-enabled/default

RUN apt-get update && apt-get install -y python-setuptools python-dev  libffi-dev libssl-dev libldap2-dev libsasl2-dev \
&& easy_install pip && pip install requests pyOpenSSL ndg-httpsclient pyasn1 django-auth-ldap

EXPOSE 8000

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
