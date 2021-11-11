FROM alpine
LABEL Author="Sven Weintuch"
LABEL Description="SSH-client image, based on alpine, prepared for a reverse-tunnel-setup"

RUN apk add --no-cache openssh-client && mkdir ~/.ssh
COPY ssh_config /etc/ssh/ssh_config

COPY run.sh /
RUN chmod +x /run.sh

ENTRYPOINT ["/run.sh"]
