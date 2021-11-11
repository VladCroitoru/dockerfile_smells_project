FROM fedora:24
MAINTAINER Juan Manuel Parrilla Madrid <jparrill@redhat.com>

ADD requirements.txt /opt/requirements.txt

RUN dnf clean all && \
    dnf -y install ImageMagick python-pip && \
    dnf clean all
RUN pip install -r /opt/requirements.txt

WORKDIR '/opt'
