FROM centos:7
MAINTAINER Daniel Tschan <tschan@puzzle.ch>

RUN env

RUN cat /etc/resolv.conf

# RUN curl http://59.60.0.19/

RUN curl http://mirror.switch.ch/

RUN yum -y install openssh-server passwd dnsutil curl nmap lsof jq links bind-utils net-tools telnet iputils shellinabox initscripts; yum clean all
RUN /usr/sbin/sshd-keygen
RUN echo shellinabox | passwd --stdin root

ADD run.sh /tmp/run.sh
ADD libmapuid.so /usr/local/lib/libmapuid.so

USER 1001

EXPOSE 4200

CMD ["/usr/bin/env", "LD_PRELOAD=/usr/local/lib/libmapuid.so", "/tmp/run.sh"]
