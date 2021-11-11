FROM ubuntu:14.04

MAINTAINER Evan Heidtmann

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential \
    wget \
    libdbix-safe-perl \
    libdbd-pg-perl \
    libpq-dev \
    postgresql-plperl-9.3 \
    libboolean-perl \
    postgresql \
    postgresql-contrib \
    expect

RUN mkdir /srv/bucardo
RUN mkdir /var/run/bucardo
RUN mkdir /var/log/bucardo

WORKDIR /srv/bucardo

RUN wget http://bucardo.org/downloads/Bucardo-5.3.1.tar.gz \
  && tar xf Bucardo-5.3.1.tar.gz \
  && cd Bucardo-5.3.1 \
  && perl Makefile.PL \
  && make \
  && make install \
  && cd .. \
  && rm -rf Bucardo*

# Credentials for main bucardo database
ENV BUCARDO_POSTGRES_PASSWORD=bucardo
ENV BUCARDO_POSTGRES_DATABASE=bucardo
ENV BUCARDO_POSTGRES_HOST=bucardo-postgres
ENV BUCARDO_POSTGRES_USERNAME=bucardo

CMD /bin/bash
#CMD bucardo install --batch --db-user "$BUCARDO_POSTGRES_USERNAME" --db-host "$BUCARDO_POSTGRES_HOST" --db-name "$BUCARDO_POSTGRES_DATABASE" --db-pass "$BUCARDO_POSTGRES_PASSWORD" && bucardo start
