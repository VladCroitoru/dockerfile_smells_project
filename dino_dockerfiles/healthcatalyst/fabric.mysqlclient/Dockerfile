FROM healthcatalyst/fabric.baseos:latest

LABEL maintainer="imran.qureshi@healthcatalyst.com"


# install mariadb-client (i.e., mysql client) so we can wait for our tables to become ready
ADD mariadb.repo /etc/yum.repos.d/

RUN yum -y install MariaDB-client bind-utils; yum clean all

ADD docker-entrypoint.sh ./docker-entrypoint.sh

RUN dos2unix ./docker-entrypoint.sh &>/dev/null \
	&& chmod a+x ./docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh"]
# CMD ["shell"]
