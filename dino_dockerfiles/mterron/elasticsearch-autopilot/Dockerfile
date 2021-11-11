FROM elasticsearch:alpine

# Alpine packages
RUN	apk -f -q --progress --no-cache upgrade &&\
	apk -f -q --progress --no-cache add \
		bash \
		curl \
		dnsmasq \
		jq \
		tzdata 

ENV CONTAINERPILOT_VERSION=2.6.0 \
	CONTAINERPILOT=file:///etc/containerpilot/containerpilot.json \
	CONSUL_VERSION=0.7.2 \
	S6_VERSION=1.19.1.1

# Copy internal CA certificate bundle.
COPY ca.pem /etc/ssl/private/
# Client certificate to talk to Consul 
# From man curl 
# -E, --cert # <certificate[:password]> (SSL) Tells curl to use the specified
# client certificate file when getting a file with HTTPS, FTPS or another SSL-
# based protocol. The certificate must be in PKCS#12 format if using Secure 
# Transport, or PEM format if using any other engine. If the optional 
# password isn't specified, it will be queried for on the terminal. 
# Note that this option assumes a "certificate" file that is the private key 
# and the private certificate concatenated! See --cert and --key to specify 
# them independently.
COPY client_certificate.* /etc/tls/
# Add our configuration files and scripts
COPY bin/* /usr/local/bin/
COPY containerpilot.json /etc/containerpilot/containerpilot.json
COPY etc/ /etc
COPY consul.json /etc/consul/
COPY elasticsearch.yml /usr/share/elasticsearch/config/

# If you build on top of this image, please provide this files
# If you are using an internal CA
ONBUILD COPY ca.pem /etc/ssl/private/
ONBUILD COPY containerpilot.json /etc/containerpilot/containerpilot.json
ONBUILD COPY consul.json /etc/consul/
ONBUILD COPY elasticsearch.yml /usr/share/elasticsearch/config/

WORKDIR /tmp
RUN echo "Downloading S6 Overlay" &&\
	curl -LO# https://github.com/just-containers/s6-overlay/releases/download/v${S6_VERSION}/s6-overlay-amd64.tar.gz &&\
	gunzip -c /tmp/s6-overlay-amd64.tar.gz | tar -xf - -C / &&\
	rm -f s6-overlay-amd64.tar.gz &&\
	echo "Downloading Containerpilot" &&\
	curl -LO# https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VERSION}/containerpilot-${CONTAINERPILOT_VERSION}.tar.gz &&\
	echo "Downloading Containerpilot checksums" &&\
	curl -LO# https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VERSION}/containerpilot-${CONTAINERPILOT_VERSION}.sha1.txt &&\
	sha1sum -sc containerpilot-${CONTAINERPILOT_VERSION}.sha1.txt &&\
	mkdir -p /opt/containerpilot &&\
	tar xzf containerpilot-${CONTAINERPILOT_VERSION}.tar.gz -C /opt/containerpilot/ &&\
	rm -f containerpilot-${CONTAINERPILOT_VERSION}.* &&\
# Download Consul binary
	echo "Downloading Consul" &&\
	curl -LO# https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip &&\
# Download Consul integrity file
	echo "Downloading Consul checksums" &&\
	curl -LO# https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_SHA256SUMS &&\
# Check integrity and installs Consul
	grep "linux_amd64.zip" consul_${CONSUL_VERSION}_SHA256SUMS | sha256sum -sc &&\
	unzip -q -o consul_${CONSUL_VERSION}_linux_amd64.zip -d /bin &&\
	rm -f consul_${CONSUL_VERSION}_* &&\
# Consul user
	adduser -D -H -g consul consul &&\
	adduser consul consul &&\
# Create Consul data directory
	mkdir /data &&\
	mkdir -p /etc/consul &&\
	chmod 770 /data &&\
	chown -R consul: /data &&\
	chown -R consul: /etc/consul/ &&\
	chmod +x /bin/* &&\
# Create and take ownership over required directories
	mkdir -p /etc/containerpilot &&\
	chmod -R g+w /etc/containerpilot &&\
	chown -R elasticsearch:elasticsearch /etc/containerpilot &&\
	cat /etc/ssl/private/ca.pem >> /etc/ssl/certs/ca-certificates.crt

EXPOSE 9200 9300 8301

# Put Consul data on a separate volume to avoid filesystem performance issues with Docker image layers
VOLUME ["/data"]

ENTRYPOINT ["/init"]
