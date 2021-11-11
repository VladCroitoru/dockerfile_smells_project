FROM alpine:latest
LABEL maintainer="dante"

ENV TZ Asia/Shanghai

RUN apk --no-cache add tzdata dnsmasq-dnssec
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN cp /usr/share/zoneinfo/$TZ /etc/localtime
RUN echo $TZ > /etc/timezone

EXPOSE 53/udp

VOLUME "/config"

CMD ["dnsmasq", "-k", "-q", "-C", "/config/dnsmasq.conf", "--log-facility=-"]