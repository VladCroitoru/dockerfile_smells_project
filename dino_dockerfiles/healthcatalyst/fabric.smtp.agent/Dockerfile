FROM centos:centos7

LABEL maintainer="Health Catalyst"
LABEL version="1.0"

# https://tecadmin.net/install-and-configure-postfix-on-centos-redhat/#
RUN yum -y install postfix dos2unix rsyslog cyrus-sasl-plain

# RUN alternatives --set mta /usr/sbin/postfix

# COPY main.cnf /etc/postfix/main.cf

# RUN postfix reload

ADD docker-entrypoint.sh ./docker-entrypoint.sh

RUN dos2unix ./docker-entrypoint.sh &>/dev/null \
	&& chmod a+x ./docker-entrypoint.sh

EXPOSE 25

ENTRYPOINT ["./docker-entrypoint.sh"]

# CMD ["postfix", "start"]


