FROM ubuntu:14.04

RUN apt-get update && apt-get -y install wget
RUN wget --quiet --no-check-certificate -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install pgbouncer stunnel supervisor

ADD ./serverconf/etc/supervisor/supervisor.conf /etc/supervisor/conf.d/
ADD ./serverconf/etc/stunnel/ /etc/stunnel/

ADD ./serverconf/scripts/      /build/scripts/

CMD ["/build/scripts/init.sh"]

EXPOSE 5432
