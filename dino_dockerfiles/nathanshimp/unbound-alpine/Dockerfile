FROM alpine:latest
RUN apk --no-cache add unbound
COPY unbound.conf /etc/unbound/unbound.conf
RUN unbound-checkconf
EXPOSE 53/udp
ENTRYPOINT ["unbound", "-d"]
