FROM sentry:8.22.0

MAINTAINER Simone Esposito "simone@kiwi.com"

ENV SENTRY_VERSION=8.22

RUN apt-get update && apt-get -y install python-dev libldap2-dev libsasl2-dev libssl-dev && \
    pip install sentry-auth-gitlab==0.1.0 datadog==0.17.0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY sentry.conf.py /etc/sentry/sentry.conf.py

LABEL name=sentry version=$SENTRY_VERSION
