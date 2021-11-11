FROM alpine:3.6

LABEL maintainer="rimelek@it-sziget.hu"

RUN apk update && apk add openssh-client \
 && echo -e 'Host *\nUseRoaming no' >> /etc/ssh/ssh_config

ENV TUNNEL_HOST="" \
    TUNNEL_REMOTES=""

COPY start.sh /start.sh

RUN chmod +x /start.sh

ENTRYPOINT []

CMD ["/bin/sh", "-c", "/start.sh"]