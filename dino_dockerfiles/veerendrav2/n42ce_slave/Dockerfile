FROM ubuntu:latest
MAINTAINER Networks42
RUN apt-get update && apt-get install -y supervisor python2.7 python-pip curl vim python-dev
RUN pip install potsdb redis docker-py pyyaml ipy netifaces pynetfilter_conntrack pybrctl
#packetbeat
RUN apt-get install -y libpcap0.8
RUN curl -L -O https://download.elastic.co/beats/packetbeat/packetbeat_1.1.2_amd64.deb
RUN dpkg -i packetbeat_1.1.2_amd64.deb
ADD packetbeat.yml /etc/packetbeat/packetbeat.yml
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD stats /opt/n42Agents/stats
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY docker_app_dep.py /opt/n42Agents/docker_app_dep.py
COPY port_dictionary.py /opt/n42Agents/port_dictionary.py
COPY docker_app_dep_perodic.py /opt/n42Agents/docker_app_dep_perodic.py
CMD ["/usr/bin/supervisord"]
