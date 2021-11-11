# This Dockerfile sets up the Buddycloud stack from the database layer
# all the way up to the webserver, API and user-facing webclient

FROM ubuntu:14.04
RUN apt-get update

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y -q install --no-install-recommends postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3

USER postgres

RUN /etc/init.d/postgresql start && psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" &&\
    createdb -O docker docker

RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf
RUN echo "listen_addresses='0.0.0.0'" >> /etc/postgresql/9.3/main/postgresql.conf

USER root

# Setup XMPP-layer
RUN apt-get install -y --no-install-recommends prosody lua-zlib lua-cyrussasl lua-sec
ADD resources/prosody.cfg.lua /etc/prosody/prosody.cfg.lua
RUN mkdir -p /var/run/prosody
RUN chown prosody /var/run/prosody

EXPOSE 5222 5432 5347

ENTRYPOINT prosodyctl start && service postgresql start && tailf /var/log/prosody/prosody.log