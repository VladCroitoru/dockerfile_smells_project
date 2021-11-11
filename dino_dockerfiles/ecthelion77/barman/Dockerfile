FROM golang:1.8-jessie

# grab gosu for easy step-down from root
ARG GOSU_VERSION=1.7
RUN set -x \
	&& apt-get update && apt-get install -y --no-install-recommends ca-certificates wget && rm -rf /var/lib/apt/lists/* \
	&& wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)" \
	&& wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc" \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
	&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
	&& rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc \
	&& chmod +x /usr/local/bin/gosu \
	&& gosu nobody true 

RUN  wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | apt-key add - && \
     sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" >> /etc/apt/sources.list.d/pgdg.list' && \
     apt-get update && \
     apt-get install -y libffi-dev libssl-dev postgresql-client-10=10.2\* barman=2.3-2.pgdg80+1 openssh-server

RUN apt-get -y install cron
ADD ./crontab /etc/cron.d/barman
RUN rm -f /etc/cron.daily/*

RUN groupadd -r postgres --gid=999 \ 
  && useradd -r -g postgres -d /home/postgres --uid=999 postgres \
  && mkdir /home/postgres \
  && chown -R postgres:postgres /home/postgres \
  && mkdir /var/log/barman \
  && chown -R postgres:postgres /var/log/barman

COPY ./bin /usr/local/bin/barman_docker
RUN chmod +x /usr/local/bin/barman_docker/* \
  && ls /usr/local/bin/barman_docker

COPY ./metrics /go
RUN cd /go && go build /go/main.go

VOLUME /var/backups

ENTRYPOINT ["/usr/local/bin/barman_docker/entrypoint.sh"]
