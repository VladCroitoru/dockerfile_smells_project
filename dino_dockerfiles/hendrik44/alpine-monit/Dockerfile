FROM alpine:3.12
MAINTAINER Hendrik Juerst <Hendrik44@users.noreply.github.com>

# Compile and install monit and confd
ENV MONIT_VERSION=5.27.1     MONIT_HOME=/opt/monit     MONIT_URL=https://mmonit.com/monit/dist     SERVICE_VOLUME=/opt/tools     PATH=$PATH:/opt/monit/bin

# Compile and install monit
RUN apk upgrade --update \
	&& apk add --no-cache bash libressl curl fping libcap gcc musl-dev make libressl-dev file zlib-dev \
	&& rm -rf /var/cache/apk/* \
	&& mkdir -p /opt/src; cd /opt/src \
	&& curl -sS ${MONIT_URL}/monit-${MONIT_VERSION}.tar.gz | gunzip -c - | tar -xf - \
	&& cd /opt/src/monit-${MONIT_VERSION} \
	&& ./configure  --prefix=${MONIT_HOME} --without-pam \
	&& make && make install \
	&& mkdir -p ${MONIT_HOME}/etc/conf.d ${MONIT_HOME}/log \
	&& apk del gcc musl-dev make libressl-dev file zlib-dev \
	&& rm -rf /var/cache/apk/* /opt/src 
ADD root /
RUN chmod +x ${MONIT_HOME}/bin/monit-start.sh

ENTRYPOINT ["/bin/bash","-c","${MONIT_HOME}/bin/monit-start.sh"]
