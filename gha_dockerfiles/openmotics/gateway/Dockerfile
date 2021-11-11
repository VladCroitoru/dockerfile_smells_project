FROM alpine
MAINTAINER Openmotics <engineering@openmotics.com>

ENV LISTEN_PORT 8443
EXPOSE 8443

RUN apk upgrade --no-cache && apk add --no-cache \
    linux-headers \
    build-base \
    python3 \
    python3-dev \
    py3-pip \
    bash \
    git \
  && pip3 install --no-cache-dir --upgrade pip \
  && rm -rf /var/cache/* \
  && rm -rf /root/.cache/*

RUN pip3 install --upgrade pip
COPY requirements-py3.txt /requirements-py3.txt
RUN pip3 install -r /requirements-py3.txt
ADD src /opt/openmotics/python
ADD etc /opt/openmotics/etc
ADD static /opt/openmotics/static

WORKDIR /opt/openmotics/python
CMD python3 openmotics_service.py
