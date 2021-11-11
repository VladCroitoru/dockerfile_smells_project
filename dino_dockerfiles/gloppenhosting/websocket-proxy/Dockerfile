FROM debian:jessie
MAINTAINER Andreas Krüger
ENV RUNDIR /run/haproxy

# Install haproxy and curl
RUN apt-get update -yqq && apt-get install --no-install-recommends --no-install-suggests -yqq haproxy curl ssl-cert && rm -rf /var/lib/apt/lists/*

# Install confd
RUN curl -skL https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-amd64 -o /usr/local/bin/confd
RUN chmod +x /usr/local/bin/confd

# Add startup script
COPY start.sh /start.sh

# Add confd configs
COPY haproxy.cfg.tmpl /etc/confd/templates/haproxy.cfg.tmpl
COPY haproxy.toml /etc/confd/conf.d/haproxy.toml

# Certs
WORKDIR /etc/ssl
RUN cat private/ssl-cert-snakeoil.key certs/ssl-cert-snakeoil.pem > snakeoil.pem

# Set volume for confd
# VOLUME /etc/confd

# Lets go
CMD ["/start.sh"]
