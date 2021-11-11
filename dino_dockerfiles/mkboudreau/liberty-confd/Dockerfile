############################################################
# Dockerfile to add in confd capability into wasdev liberty
# Based on wasdev/websphere-liberty & ubuntu
############################################################

FROM websphere-liberty:8.5.5
MAINTAINER Michael Boudreau <mkboudreau@yahoo.com>

### INSTALL CONFD
RUN wget https://github.com/kelseyhightower/confd/releases/download/v0.7.1/confd-0.7.1-linux-amd64
RUN mv confd-0.7.1-linux-amd64 /usr/local/bin/confd
RUN chmod +x /usr/local/bin/confd
RUN mkdir -p /etc/confd/conf.d /etc/confd/templates
