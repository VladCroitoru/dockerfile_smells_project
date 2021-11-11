FROM debian:stretch

RUN apt-get update && apt-get install -y \
        ca-certificates \
        authbind \
        trafficserver \
	--no-install-recommends && rm -r /var/lib/apt/lists/*

RUN touch /etc/authbind/byport/80 \
  && chmod 777 /etc/authbind/byport/80

RUN mkdir -p /var/run/trafficserver \
  && chown trafficserver:trafficserver /var/run/trafficserver

COPY etc/plugin.config /etc/trafficserver/plugin.config
COPY etc/remap.config /etc/trafficserver/remap.config

ENV PROXY_CONFIG_ADMIN_USER_ID trafficserver
ENV PROXY_CONFIG_CACHE_RAM_CACHE_SIZE 0
ENV PROXY_CONFIG_SSL_CLIENT_CA_CERT_PATH="/etc/ssl/certs"
ENV PROXY_CONFIG_SSL_CLIENT_VERIFY_SERVER 1
ENV PROXY_CONFIG_URL_REMAP_REMAP_REQUIRED 0
ENV PROXY_CONFIG_REVERSE_PROXY_ENABLED 0
ENV PROXY_CONFIG_HTTP_SERVER_PORTS="80"

EXPOSE 80

CMD ["authbind", "--deep", "traffic_cop", "-o"]
