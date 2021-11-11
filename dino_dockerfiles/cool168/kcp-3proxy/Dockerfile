FROM ubuntu:16.04

RUN apt-get update && \
	apt-get install -y  libappindicator3-1 wget openssh-server supervisor

RUN mkdir -p /var/run/sshd
RUN mkdir -p /var/log/supervisor

ADD zzsupervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN apt-get clean
ADD . /usr/bin
RUN chmod +x /usr/bin/3proxy
RUN chmod +x /usr/bin/dighosts
RUN chmod +x /usr/bin/ftppr
RUN chmod +x /usr/bin/icqpr
RUN chmod +x /usr/bin/mycrypt
RUN chmod +x /usr/bin/PCREPlugin.ld.so
RUN chmod +x /usr/bin/pop3p
RUN chmod +x /usr/bin/proxy
RUN chmod +x /usr/bin/smtpp
RUN chmod +x /usr/bin/socks
RUN chmod +x /usr/bin/StringsPlugin.ld.so
RUN chmod +x /usr/bin/tcppm
RUN chmod +x /usr/bin/TrafficPlugin.ld.so
RUN chmod +x /usr/bin/TransparentPlugin.ld.so
RUN chmod +x /usr/bin/udppm
RUN chmod +x /usr/bin/3proxy.cfg
RUN chmod +x /usr/bin/server_linux_amd64
COPY k3p-server.sh /k3p-server.sh
RUN chmod +x /k3p-server.sh

EXPOSE 39900/udp

# CMD ["/usr/bin/supervisord"]
ENTRYPOINT ["/k3p-server.sh", "/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

