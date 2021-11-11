FROM phusion/baseimage

RUN apt-get update
RUN locale-gen en_US.UTF-8
ENV LANG       en_US.UTF-8
ENV LC_ALL     en_US.UTF-8
ENV FIRST_RUN_LOCK /etc/postgresql/9.3/main/firstrun.lock

RUN echo '#!/bin/sh' "\nexit 0" >  /usr/sbin/policy-rc.d

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Install the latest postgresql
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
    apt-get -y update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3 && \
    /etc/init.d/postgresql stop

# Allow connections from anywhere.
RUN sed -i -e"s/^#listen_addresses =.*$/listen_addresses = '*'/" /etc/postgresql/9.3/main/postgresql.conf
RUN echo "host    all    all    0.0.0.0/0    md5" >> /etc/postgresql/9.3/main/pg_hba.conf

#create a file
RUN touch $FIRST_RUN_LOCK

RUN mkdir /etc/service/postgresql
ADD run.sh /etc/service/postgresql/run
RUN chmod 755 /etc/service/postgresql/run


VOLUME ["/var/lib/postgresql"]
EXPOSE 5432

CMD ["/sbin/my_init"]