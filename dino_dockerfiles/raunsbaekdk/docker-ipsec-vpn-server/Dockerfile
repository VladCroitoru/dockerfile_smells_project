# From alpine:latest image
FROM alpine:latest

# Set the maintainer
MAINTAINER Mike

# Set work dir
WORKDIR /opt/src

# Install dep packge , Configure,make and install strongSwan
RUN apk --no-cache --update add wget bash iproute2 iptables openssl kmod libreswan xl2tpd ipsec-tools ca-certificates curl \
  && rm -f /etc/ppp/chap-secrets /etc/ipsec.d/passwd /etc/ipsec.secrets

# Download and install grimd
RUN curl -o /usr/local/bin/grimd -L https://github.com/raunsbaekdk/grimd/releases/download/1.0.8/grimd-linux-amd64
RUN chmod 755 /usr/local/bin/grimd
RUN mkdir -p /etc/grimd
COPY ./conf/grimd.toml /etc/grimd/grimd.toml

# Copy start file
COPY ./run.sh /opt/src/run.sh
RUN chmod 755 /opt/src/run.sh

# Open ports
EXPOSE 500:500/udp 4500:4500/udp

# Mount volumnes
VOLUME ["/lib/modules"]

# Start
CMD ["/opt/src/run.sh"]
