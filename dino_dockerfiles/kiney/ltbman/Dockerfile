FROM debian:jessie

MAINTAINER Jannik Winkel <jannik.winkel@kiney.de>

ENV VERSION "1"

ENV DEBIAN_FRONTEND noninteractive

# install basic and VNC stuff
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    locales \
    unzip \
    python3-pip \
    python3-jinja2 \
    python3-yaml

ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

# install gunicorn
RUN pip3 install gunicorn records bottle

RUN useradd -ms /bin/bash ltbman
RUN mkdir /var/lib/ltbman
RUN chown ltbman:ltbman /var/lib/ltbman


EXPOSE 8080
VOLUME ["/var/lib/ltbman"]

# Add Tini
ENV TINI_VERSION v0.14.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-amd64 /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

ADD . /opt/ltbman

ADD run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]
