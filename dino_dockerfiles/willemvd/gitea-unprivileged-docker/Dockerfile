FROM gitea/gitea:1.1.0
MAINTAINER willemvd <willemvd@github>

ENV HOME /data/git

COPY docker /

RUN rm -rf /etc/s6/syslogd && \
  chmod g+w /etc/passwd /var/run && \
  chmod -R g+w /etc/s6 && \
  chown -R git:root /app

USER git

EXPOSE 2222 3000
