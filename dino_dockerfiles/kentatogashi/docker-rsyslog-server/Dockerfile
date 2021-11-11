FROM ubuntu:latest
MAINTAINER togashik@togashi.k

RUN sed -e 's/^#\(.*\)imudp/\1imudp/' -e 's/^#\(\$UDPServerRun.*\)/\1/' -e 's/^#\(.*\)imtcp/\1imtcp/' -e 's/^#\(\$InputTCPServerRun.*\)/\1/' /etc/rsyslog.conf
ADD entrypoint.sh /entrypoint.sh
EXPOSE 514:514
ENTRYPOINT ["sh", "/entrypoint.sh"]
