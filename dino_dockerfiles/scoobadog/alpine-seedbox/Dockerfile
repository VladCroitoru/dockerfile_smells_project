FROM scoobadog/s6-openvpn:1.1
MAINTAINER Janne K <0x022b@gmail.com>

RUN \
addgroup -S flexget && \
adduser -s /sbin/nologin -h /var/lib/flexget -SD -G flexget flexget && \
apk --no-cache add \
	py2-pip \
	transmission-daemon && \
pip install --no-cache-dir --upgrade pip flexget transmissionrpc && \
rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /root/.cache

COPY rootfs/ /
