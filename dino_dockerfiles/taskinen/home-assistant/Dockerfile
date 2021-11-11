FROM homeassistant/home-assistant:stable
LABEL maintainer="Timo Taskinen <timo.taskinen@iki.fi>"

# Install some dependencies and utils
RUN apk add --update \
  bash \
  curl \
  supervisor

# telldusd is already included in the official base image

# Install and configure Supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ENTRYPOINT ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]

# Specify health check for Docker
HEALTHCHECK CMD curl --fail http://localhost:8123 || exit 1
