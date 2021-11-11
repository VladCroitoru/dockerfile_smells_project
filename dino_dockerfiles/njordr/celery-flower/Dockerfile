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

RUN pip3 install flower

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN mkdir -p /var/log/supervisor \
  && chgrp staff /var/log/supervisor \
  && chmod g+w /var/log/supervisor \
  && chgrp staff /etc/supervisor/conf.d/supervisord.conf

RUN mkdir -p /etc/flower /var/flower/db 

COPY flowerconfig.py /etc/flower/flowerconfig.py

EXPOSE 5555

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
