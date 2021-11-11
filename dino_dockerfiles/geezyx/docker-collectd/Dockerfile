FROM geezyx/ruby-nodejs

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update
RUN apt-get -y install collectd snmp

ADD mibs.tar.gz /usr/share/snmp/

ADD start_container /usr/bin/start_container
RUN chmod +x /usr/bin/start_container
CMD start_container
