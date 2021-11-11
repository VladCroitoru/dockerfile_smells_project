FROM ubuntu:14.04

MAINTAINER "Giovanni Colapinto" alfheim@syshell.net

RUN rm -rf /var/lib/apt/lists/ \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
    supervisor \
    sudo \
	python3-pip \
	python3-dev \
    build-essential \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/

RUN pip3 install Celery

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN mkdir -p /var/log/supervisor \
  && chgrp staff /var/log/supervisor \
  && chmod g+w /var/log/supervisor \
  && chgrp staff /etc/supervisor/conf.d/supervisord.conf \
  && groupadd -r celery \
  && useradd -g celery -r celery \
  && mkdir -p /etc/celery /var/celery/db /var/celery/apps\
  && chown -R celery.celery /var/celery/db /var/celery/apps

COPY celeryconfig.py /etc/celery/celeryconfig.py

COPY app_celery /var/celery/apps/app_celery

RUN export PYTHONPATH=/etc/celery:$PYTHONPATH

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
