FROM ubuntu:15.04
MAINTAINER funarg

RUN apt-get update && apt-get install -y net-tools iodine iptables
RUN mkdir -p /opt/iodine
ADD start.sh /opt/iodine/start.sh

WORKDIR /opt/iodine

EXPOSE 53/udp
EXPOSE 5053/udp

CMD ["./start.sh"]
