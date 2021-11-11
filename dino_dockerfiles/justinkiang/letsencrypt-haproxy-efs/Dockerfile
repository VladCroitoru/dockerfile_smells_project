FROM dockercloud/haproxy:1.6.2

RUN apk add --update \
		bash \
		openssl \
		wget \
		nfs-utils \
	&& rm -rf /var/cache/apk/*

ENV LIVE_CERT_FOLDER="/etc/letsencrypt/live"
ENV PATH="/opt/haproxy/bin:$PATH"

COPY . /opt/haproxy

CMD ["entrypoint.sh", "dockercloud-haproxy"]