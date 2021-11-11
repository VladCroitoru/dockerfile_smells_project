# Use zeroae/ap-light
# https://github.com/zeroae/ap-light
FROM zeroae/ap-light:0.6.0
MAINTAINER Patrick Sodré <sodre@zeroae.co>

ENV CONSUL_BOOTSTRAP_EXPECT=3

ADD service ${AP_SERVICE_DIR}
RUN ap-service-install

# Set /var/www/ in a data volume
VOLUME /var/lib/run

# Expose default http and https ports
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 53 53/udp
