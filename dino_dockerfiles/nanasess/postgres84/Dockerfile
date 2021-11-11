# vim:set ft=dockerfile:
FROM centos:6

MAINTAINER "Kentaro Ohkouchi" <nanasess@fsm.ne.jp>

### see also https://github.com/docker-library/postgres/blob/2df7c179897a4a0c5dbb5a68543e46fb77215067/9.1/Dockerfile

# explicitly set user/group IDs
RUN groupadd -r postgres --gid=999 && useradd -r -g postgres --uid=999 postgres

ENV GOSU_VERSION 1.7
RUN gpg --keyserver pgp.mit.edu --recv-keys \
	B42F6819007F00F88E364FD4036A9C25BF357DD4 \
	&& curl -sSL https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-amd64 -o /bin/gosu \
	&& chmod +x /bin/gosu \
	&& curl -sSL https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-amd64.asc -o /tmp/gosu.asc \
	&& gpg --verify /tmp/gosu.asc /bin/gosu \
	&& rm /tmp/gosu.asc

RUN yum -y install postgresql-server; yum clean all; chkconfig postgresql on

RUN localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8
ENV LANG ja_JP.UTF-8

RUN mkdir /docker-entrypoint-initdb.d

ENV PG_MAJOR 8.4
ENV PG_VERSION 8.4.13

RUN sed -ri "s!^#?(listen_addresses)\s*=\s*\S+.*!\1 = '*'!" /usr/share/pgsql/postgresql.conf.sample

ENV PGDATA /var/lib/pgsql/data
VOLUME /var/lib/pgsql/data

COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 5432
CMD ["postgres"]
