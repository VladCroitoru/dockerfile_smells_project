FROM debian:buster-slim

RUN apt-get update && apt-get install -y openconnect ocproxy curl lsof procps && \
    apt-get clean && \
    rm -rf /var/cache/apt/* && \
    rm -rf /var/lib/apt/lists/*

COPY vpn-open vpn-close /usr/bin/
RUN chmod +x /usr/bin/vpn-open & chmod +x /usr/bin/vpn-close

LABEL org.label-schema.schema-version="1.0" \
    org.label-schema.name="sk8darr/openconnect" \
    org.label-schema.description="Create a VPN tunnel to your on premise services" \
    org.label-schema.vcs-url="https://github.com/sk8darr/docker-openconnect"
