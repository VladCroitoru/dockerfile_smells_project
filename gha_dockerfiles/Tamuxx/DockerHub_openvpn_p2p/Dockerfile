# v2.0
# Build with:
# docker build -t ovpn:2.0 .
FROM alpine:3.14.0
RUN apk --no-cache add openvpn
RUN mkdir -p /var/empty/tmp
COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
RUN mkdir /data
ENTRYPOINT ["/usr/bin/entrypoint.sh"]

