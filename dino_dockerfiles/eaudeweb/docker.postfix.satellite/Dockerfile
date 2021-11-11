FROM centos:7
MAINTAINER Cristian Romanescu <cristian@romanescu.ro>

EXPOSE 25

VOLUME ["/var/log", "/var/spool/postfix"]

RUN yum install -y epel-release && yum update -y \
	&& yum install -y \
		cyrus-sasl cyrus-sasl-plain cyrus-sasl-md5 mailx nail postfix \
    	supervisor rsyslog \
    && yum clean all

RUN sed -i -e "s/^nodaemon=false/nodaemon=true/" /etc/supervisord.conf
RUN sed -i -e 's/inet_interfaces = localhost/inet_interfaces = all/g' /etc/postfix/main.cf

COPY etc/*.conf /etc/
COPY etc/rsyslog.d/* /etc/rsyslog.d

COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
COPY etc/supervisord.d/*.ini /etc/supervisord.d/

RUN newaliases

CMD ["/docker-entrypoint.sh"]
