FROM ubuntu:bionic
RUN echo deb http://archive.ubuntu.com/ubuntu/ precise main universe > /etc/apt/sources.list.d/precise.list
#RUN apt-get update -q
RUN apt-get install -qy openvpn iptables socat curl
ADD ./bin /usr/local/sbin
ADD server.conf /etc/openvpn/server.conf
VOLUME /etc/openvpn
EXPOSE 443/tcp 1194/udp 8080/tcp
CMD run
