FROM ubuntu
MAINTAINER Michael Johnson <michael@johnson.computer>

COPY debconf.txt /debconf.txt
RUN debconf-set-selections /debconf.txt && rm /debconf.txt

RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -qq -y postfix

COPY confd/confd /opt/confd
RUN chmod a+x /opt/confd

COPY confd/cert.pem.toml /opt/confd-ssl/conf.d/
COPY confd/cert.pem.tmpl /opt/confd-ssl/templates/

COPY confd/aliases.toml /etc/confd/conf.d/
COPY confd/aliases.tmpl /etc/confd/templates/

COPY confd/relay_clientcerts.toml /etc/confd/conf.d/
COPY confd/relay_clientcerts.tmpl /etc/confd/templates/

COPY confd/virtual_aliases.toml /etc/confd/conf.d/
COPY confd/virtual_aliases.tmpl /etc/confd/templates/

COPY confd/virtual_domains.toml /etc/confd/conf.d/
COPY confd/virtual_domains.tmpl /etc/confd/templates/

COPY dh2048.pem /etc/ssl/dh2048.pem

COPY master.cf /etc/postfix/master.cf
COPY main.cf /etc/postfix/main.cf

COPY start.sh /opt/start.sh
RUN chmod a+x /opt/start.sh

EXPOSE 25 587
CMD ["/opt/start.sh"]
