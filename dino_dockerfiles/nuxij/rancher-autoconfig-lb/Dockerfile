FROM alpine

MAINTAINER Joe Eaves <joe.eaves@shadowacre.ltd>

RUN apk update && apk add gcc musl-dev python python-dev py2-pip vim

WORKDIR /var/lib/rancher-autoconfig-lb/
ADD src/requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt && python -c "import requests, urllib3"

COPY src/ /var/lib/rancher-autoconfig-lb/

ENV CA https://acme-v01.api.letsencrypt.org/directory
ENV LEE_SEED_JSON "{}"
ENV LE_WORK_DIR "/var/lib/rancher-autoconfig-lb/.le"

CMD cd /var/lib/rancher-autoconfig-lb && python -u run.py
