# Restrict to alpine:3.8 to be sure we get the gpsd 3.17 version which is compatible with client tools
FROM alpine:3.8

RUN apk add --no-cache \
    'gpsd=3.17-r2' \
    'gpsd-clients=3.17-r2'

# capture output of gpsd to logging via syslogd
ARG GPS_DEVICE
ENTRYPOINT ["/bin/sh", "-c", "/sbin/syslogd -S -O - -n & exec /usr/sbin/gpsd -N -n -G -D 5 $GPS_DEVICE","--"]
