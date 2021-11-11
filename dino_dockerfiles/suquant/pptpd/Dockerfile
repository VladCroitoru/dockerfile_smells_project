FROM alpine:edge
MAINTAINER George Kutsurua <g.kutsurua@gmail.com>

RUN apk update && apk upgrade && \
	apk add iptables pptpd ppp ppp-radius

COPY entrypoint.sh /usr/bin/entrypoint.sh
COPY pptpd.conf /etc/pptpd.conf

VOLUME ["/var/lib/pptpd"]

ENTRYPOINT ["/usr/bin/entrypoint.sh"]
CMD [""]

EXPOSE 1723
