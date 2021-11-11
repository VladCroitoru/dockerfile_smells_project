################################################################################
# mesos-master: 1.3.0
# Date: 02/20/2017
# Mesos Version: 1.1.0-2.0.107.ubuntu1404
#
# Description:
# Mesos Master container. Mesos Version is tied to mesos-base container.
# Former MAINTAINER Bob Killen / killen.bob@gmail.com / @mrbobbytables
################################################################################

FROM pixelfederation/mesos-base:1.3.0

MAINTAINER Milan Baran / mbaran@pixelfederation.com / @mbaran

COPY ./skel /

RUN chmod +x init.sh  \
 && chown -R logstash-forwarder:logstash-forwarder /opt/logstash-forwarder

EXPOSE 5050

CMD ["./init.sh"]
