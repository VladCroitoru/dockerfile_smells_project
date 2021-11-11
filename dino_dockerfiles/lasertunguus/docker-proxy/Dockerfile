FROM ubuntu:16.04

EXPOSE 8888 8888

RUN apt-get -y update && apt-get install -y openvpn curl wget net-tools vim less default-jre iptables && \
  mkdir /vpn

# working dir
WORKDIR /vpn

CMD ["/bin/bash"]
