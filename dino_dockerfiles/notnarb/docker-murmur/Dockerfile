FROM alpine:3.5
RUN apk add --update murmur && rm /var/cache/apk/*
COPY murmur.ini /etc/murmur.ini
RUN chmod 666 /etc/murmur.ini
# No password (-D), force uid
RUN adduser murmuruser -D -u 1000
# Set permissions to 777 so that this folder is accessible by any user the container may be run as
RUN chmod 777 /var/lib/murmur
VOLUME /var/lib/murmur
# specifiy uid by number so it works with current versions of rkt
USER 1000
EXPOSE 64738 64738/udp
CMD murmurd -fg -ini `if [ -e /var/lib/murmur/murmur.ini ];then echo "/var/lib/murmur/murmur.ini"; else echo "/etc/murmur.ini"; fi`
