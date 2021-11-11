FROM alpine:3.7

RUN apk add --update --no-cache quagga supervisor logrotate tcpdump iputils nmap-ncat net-tools && \
	mkdir -p /var/log/quagga && chown quagga -R /var/log/quagga

ADD supervisor/supervisord.conf /etc/supervisord.conf
ADD quagga /etc/quagga/
ADD supervisor/conf.d /usr/share/supervisor/conf.d/
ADD logrotate/logrotate.conf /etc/logrotate.conf
ADD logrotate/quagga /etc/logrotate.d/quagga

ENTRYPOINT ["/usr/bin/supervisord"]

CMD ["-c", "/etc/supervisord.conf", "-n"]
