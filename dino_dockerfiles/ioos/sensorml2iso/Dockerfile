FROM python:3.5

MAINTAINER Luke Campbell <luke.campbell@rpsgroup.com>

# General dependencies:
RUN apt-get update && \
    apt-get install -y --no-install-recommends libgeos-dev && \
    apt-get install -y cron rsyslog && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /srv/app /srv/iso

WORKDIR /srv/app

COPY setup.py requirements.txt ./

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY setup.py contrib/docker-entrypoint.sh ./
COPY sensorml2iso ./sensorml2iso
COPY contrib/init /etc/my_init.d
COPY contrib/bin/setuser /sbin/setuser
COPY contrib/config/config.json /etc/sensorml2iso/config.json

RUN touch /var/log/cron.log && \
    pip install -e . && \
    useradd --system --home-dir=/srv/app app && \
    chown -R app:app /srv/app /srv/iso

VOLUME /srv/iso

ENTRYPOINT ["./docker-entrypoint.sh"]
