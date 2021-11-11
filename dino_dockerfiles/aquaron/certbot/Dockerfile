FROM debian:buster-slim

ARG BUILD_DATE

LABEL maintainer="docker@aquaron.com" \
 org.label-schema.build-date=$BUILD_DATE \
 org.label-schema.docker.cmd="docker run --rm -t -v $PWD:/data aquaron/certbot" \
 org.label-schema.description="Get/renew Let's Encrypt Wildcard Certs with Certbot" \
 org.label-schema.name="certbot" \
 org.label-schema.url="https://certbot.eff.org" \
 org.label-schema.vcs-url="https://github.com/aquaron/certbot" \
 org.label-schema.vendor="aquaron" \
 org.label-schema.version="1.2"

COPY data/runme.sh /usr/bin/runme.sh
COPY data/cli.ini /etc/cli.ini


RUN apt update -q \
 && apt install -yq certbot \
    python3-certbot-dns-digitalocean \
    python3-certbot-dns-linode \
    python3-certbot-dns-google \
    python3-certbot-dns-route53 \
 && apt autoremove -qy \
 && rm -rf /var/lib/apt/lists/*

ENTRYPOINT [ "runme.sh" ]
CMD [ "help" ]
