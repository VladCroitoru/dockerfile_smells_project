FROM python:2.7

MAINTAINER Hans Kristian Flaatten <hans.kristian.flaatten@turistforeningen.no>

RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive \
    apt-get install -y libxslt1-dev libxml2-dev
#                      libpq-dev expect libldap2-dev libsasl2-dev libssl-dev

RUN pip install -U sentry[postgres]==7.7.0

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /wheels/*

RUN useradd -ms /bin/bash sentry
USER sentry
WORKDIR /home/sentry

EXPOSE 3333

ADD sentry.conf.py /home/sentry/.sentry/sentry.conf.py


