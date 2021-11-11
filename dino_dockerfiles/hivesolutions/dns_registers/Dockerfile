FROM hivesolutions/alpine:latest

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

EXPOSE 53/udp

ADD bind /etc/bind
ADD bemisc.com /etc/bind/dns_registers/bemisc.com
ADD configuration /etc/bind/dns_registers/configuration
ADD hive /etc/bind/dns_registers/hive

RUN apk update && apk add bind
RUN ln -s /etc/bind/dns_registers/configuration/named.conf /etc/bind/named.conf
RUN echo "include \"/etc/bind/dns_registers/configuration/bemisc.com.conf\";" >> /etc/bind/named.conf
RUN echo "include \"/etc/bind/dns_registers/configuration/hive.conf\";" >> /etc/bind/named.conf

CMD ["/usr/sbin/named", "-g"]
