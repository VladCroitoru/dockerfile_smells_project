FROM alpine:3.6
MAINTAINER Frederic Leger <frederic@webofmars.com>

ENV SSHBASTION_USERS="jump"                 \
    SSHBASTION_DEFAULTPASSWD="Jump4rrounD!" \
    SSHBASTION_MODE="with-logins"

RUN mkdir -p /opt /ssh
COPY dist/* /tmp/

# add s6
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && rm /tmp/s6-overlay-amd64.tar.gz

# install need packages
RUN apk upgrade --no-cache && \
    apk add --no-cache openssh-server openssh-client

# create the sshusers group
RUN addgroup sshusers

# configuration
COPY etc/ /etc/
COPY ssh.template /ssh

# add confd
RUN mv /tmp/confd-0.12.0-linux-amd64 /opt/confd && chmod a+x /opt/confd

# config
HEALTHCHECK --interval=2m --timeout=3s \
  CMD nc -z localhost 22 || exit 1
ENTRYPOINT ["/init"]
VOLUME /etc/ssh
EXPOSE 22