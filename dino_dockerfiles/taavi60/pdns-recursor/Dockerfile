FROM alpine:3.7

# Add community repo and install packages
RUN echo "@community http://dl-cdn.alpinelinux.org/alpine/v3.7/community" >> /etc/apk/repositories && \
    echo "@main http://dl-cdn.alpinelinux.org/alpine/v3.7/main" >> /etc/apk/repositories && \
    apk add -U --no-cache \
    pdns-recursor@community \
    rm -rf /var/cache/apk/*

# Edit recursor.conf
RUN sed -i "s|daemon=yes|daemon=no|g" /etc/pdns/recursor.conf && \
    sed -i "s|local-port=5353|local-port=53|g" /etc/pdns/recursor.conf && \
    sed -i "s|# local-address=127.0.0.1|local-address=0.0.0.0|g" /etc/pdns/recursor.conf && \
    sed -i "s|# include-dir=|include-dir=/data/recursor-conf.d|g" /etc/pdns/recursor.conf

# Give ownership of default config file to recursor:recursor
# This enables runtime zone/script reloading with rec_control
RUN chown recursor: /etc/pdns/recursor.conf

# Make sure the include-dir always exists
RUN mkdir -p /data/recursor-conf.d

# Make /data a volume
VOLUME /data

# Run pdns_recursor
ENTRYPOINT ["/usr/sbin/pdns_recursor"]
