FROM ubuntu
MAINTAINER Michael Johnson <michael@johnson.computer>

RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -qq -y opendkim opendkim-tools psmisc

COPY confd/confd /opt/confd
RUN chmod a+x /opt/confd

COPY confd/dkim.key.toml /opt/confd-dkim/conf.d/
COPY confd/dkim.key.tmpl /opt/confd-dkim/templates/

COPY start.sh /opt/start.sh
RUN chmod a+x /opt/start.sh

EXPOSE 12301
CMD ["/opt/start.sh"]
