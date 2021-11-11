FROM        ubuntu:14.04
MAINTAINER Grischa Meyer <grischa.meyer@monash.edu>
#Inspired by Carlo Hamalainen <c.hamalainen@uq.edu.au>

# Update and install packages.
# ADD sources.list /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y dist-upgrade
RUN apt-get -y install \
  build-essential \
  git \
  libevent-dev \
  libgraphviz-dev \
  libmagickwand5 \
  libsasl2-dev \
  libxml2-dev \
  libxslt1-dev \
  libyaml-dev \
  make \
  pkg-config \
  postgresql-server-dev-all \
  pwgen \
  python-dev \
  screen \
  supervisor

RUN adduser --home /opt/mytardis --disabled-password --gecos '' mytardis
USER mytardis
# Install MyTARDIS:
RUN mkdir -p /opt/mytardis/webapp
WORKDIR     /opt/mytardis/webapp
RUN git clone -b develop https://github.com/mytardis/mytardis.git .
# ADD         mytardis /opt/mytardis
USER root
ADD buildout-docker.cfg /opt/mytardis/webapp/
RUN chown mytardis /opt/mytardis/webapp/buildout-docker.cfg
ADD wsgi.py /opt/mytardis/webapp/
RUN chown mytardis /opt/mytardis/webapp/wsgi.py
ADD settings.py /opt/mytardis/webapp/tardis/
RUN chown mytardis /opt/mytardis/webapp/tardis/settings.py
USER mytardis
RUN python bootstrap.py -v 1.7.1
RUN ./bin/buildout -c buildout-docker.cfg

# # Add our config to MyTARDIS:
# WORKDIR     /opt
# ADD         settings.py             /opt/mytardis/tardis/
# ADD         run_mytardis.sh         /opt/mytardis/
# ADD         run_celery.sh           /opt/mytardis/
# ADD         create_admin.py         /opt/mytardis/
# ADD         create_location.py      /opt/mytardis/
# ADD         wipe_db.py              /opt/mytardis/
# ADD         append_django_paths.py  /opt/mytardis/
# ADD         create_role.sh          /opt/mytardis/

# WORKDIR     /opt/mytardis
# RUN         ln -s bin/django djangosettings.py

# RUN         rmdir /opt/mytardis/var/store
# RUN         ln -s /mytardis_store/ /opt/mytardis/var/store

# RUN         rmdir /opt/mytardis/var/staging
# RUN         ln -s /mytardis_staging/ /opt/mytardis/var/staging

# RUN mkdir /mytardis_store /mytardis_staging
USER root
RUN mkdir /mytardis_settings
VOLUME ["/mytardis_settings", "/data", "/var/log", "/mytardis_store"]

EXPOSE 22
EXPOSE 8000

RUN mkdir /scratch
VOLUME "/scratch"

# Supervisord
ADD gunicorn-supervisor.conf /etc/supervisor/conf.d/


CMD /usr/bin/supervisord -n
