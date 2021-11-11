#
# Reverse proxy for kubernetes
#
FROM nginx:1.10.1-alpine

RUN apk add --no-cache openssl

# setup confd
ADD https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-amd64 /usr/local/bin/confd
RUN chmod u+x /usr/local/bin/confd && \
	mkdir -p /etc/confd/conf.d && \
	mkdir -p /etc/confd/templates

ADD ./src/confd/conf.d/myconfig.toml /etc/confd/conf.d/myconfig.toml
ADD ./src/confd/templates/nginx.tmpl /etc/confd/templates/nginx.tmpl
ADD ./src/confd/confd.toml /etc/confd/confd.toml

ADD ./src/boot.sh /opt/boot.sh
RUN chmod +x /opt/boot.sh

# Run the boot script
CMD /opt/boot.sh
