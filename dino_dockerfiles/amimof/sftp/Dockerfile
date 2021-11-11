FROM alpine:3.7

LABEL maintainer="Amir Mofasser (@amimof)"

COPY sshd_config /etc/ssh/sshd_config
COPY server /

RUN set -x \
&&  apk add --no-cache --update openssh bash \
&&  mkdir -p /var/run/sshd \
&&  chmod +x /server

CMD ["/server"]
