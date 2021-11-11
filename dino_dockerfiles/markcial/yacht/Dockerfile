FROM docker:1.9

MAINTAINER marc garcia <marc.garcia@ulabox.com>

RUN apk add --update \
    python \
    python-dev \
    py-pip \
  && pip install --upgrade pip \
  && pip install docker-py \
  && pip install nose \
  && pip install mock \
  && rm -rf /var/cache/apk/*

RUN mkdir /hosts.d
RUN touch /hosts.d/base
WORKDIR /app
COPY application /app

CMD ["/usr/bin/python", "main.py"]
