FROM alpine:3.12

LABEL maintainer="therandomsecurityguy" \
      version="0.3"

# Optional Configuration Parameter
ARG SERVICE_USER
ARG SERVICE_HOME

# Default Settings
ENV SERVICE_USER ${SERVICE_USER:-app}
ENV SERVICE_HOME ${SERVICE_HOME:-/home/${SERVICE_USER}}

COPY ./lockdown.sh /root

RUN \
  mkdir -p ${SERVICE_HOME} && \
  adduser -h ${SERVICE_HOME} -s /sbin/nologin -u 1000 -D ${SERVICE_USER} && \
  chown -R ${SERVICE_USER}:${SERVICE_USER} ${SERVICE_HOME} && \
  apk add --no-cache \
    dumb-init && \
  chmod +x /root/lockdown.sh \
  /root/lockdown.sh

USER ${SERVICE_USER}
WORKDIR ${SERVICE_HOME}
VOLUME ${SERVICE_HOME}

ENTRYPOINT [ "/usr/bin/dumb-init", "--" ]
CMD [ "sh" ]
