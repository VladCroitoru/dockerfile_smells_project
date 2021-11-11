FROM alpine:3.6
LABEL maintainer="Tomas Kislan - https://kislan.sk"

EXPOSE 22

COPY entrypoint.sh /

RUN apk add --no-cache openssh && \
  mkdir -p /root/.ssh && \
  echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config && \
  echo "PasswordAuthentication no" >> /etc/ssh/ssh_config

VOLUME ["/root/.ssh"]

ENTRYPOINT ["/entrypoint.sh"]
