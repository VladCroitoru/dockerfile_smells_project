FROM alpine:edge
MAINTAINER Joseph Lutz <Joseph.Lutz@novatechweb.com>

# Install the packages
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
 && apk add --update \
      bitlbee \
      bitlbee-facebook@testing \
      su-exec \
 && rm -rf /var/cache/apk/*

# Store default config and
# Setup the bitlbee user for the service to run as
RUN adduser -h /var/lib/bitlbee -H -s /sbin/nologin -D bitlbee \
 && mkdir /var/run/bitlbee \
 && chown -R bitlbee:bitlbee /var/run/bitlbee \
 && cd /etc/bitlbee \
 && tar -cf /etc/bitlbee.default.config.tgz ./*

# copy over files
COPY ./docker-entrypoint.sh \
    /

# specify the volumes directly related to this image
VOLUME [ "/etc/bitlbee", "/var/lib/bitlbee" ]

# specify which network ports will be used
EXPOSE 6667

# start the entrypoint script
WORKDIR /var/lib/bitlbee
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["bitlbee"]
