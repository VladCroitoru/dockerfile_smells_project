FROM debian:stretch
LABEL maintainer "Kyle Lucy <kmlucy@gmail.com>"

COPY start.sh /start.sh

RUN apt-get update && \
	apt-get install cups foomatic-db whois -y && \
	apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
	chmod +x /start.sh && \
	# Remove backends that don't make sense for container
	rm /usr/lib/cups/backend/parallel && \
	rm /usr/lib/cups/backend/serial && \
	rm /usr/lib/cups/backend/usb

VOLUME /etc/cups/ /var/log/cups /var/spool/cups /var/cache/cups

ENV CUPS_USER=admin CUPS_PASS=password

EXPOSE 631

CMD ["/start.sh"]
