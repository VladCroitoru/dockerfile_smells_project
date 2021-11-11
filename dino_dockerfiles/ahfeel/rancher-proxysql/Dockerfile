FROM debian:jessie

MAINTAINER Jérémie BORDIER <jeremie.bordier@gmail.com>

ARG PROXYSQL_VERSION=1.4.6

RUN apt-get update && \
	apt-get install -y mysql-client curl netcat && \
	apt-get -y clean

RUN curl -L -o /tmp/proxysql.deb https://github.com/sysown/proxysql/releases/download/v${PROXYSQL_VERSION}/proxysql_${PROXYSQL_VERSION}-debian8_amd64.deb && \
	dpkg -i /tmp/proxysql.deb && \
	rm /tmp/proxysql.deb

VOLUME /var/lib/proxysql

ADD docker-entrypoint.sh /
ADD proxysql.cnf.tpl /etc/proxysql.cnf.tpl

EXPOSE 3306 6032 6080

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["/usr/bin/proxysql", "--initial", "-f"]
