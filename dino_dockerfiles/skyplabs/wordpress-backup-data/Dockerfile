FROM python:2-onbuild

LABEL net.skyplabs.maintainer-name="Paul-Emmanuel Raoul"
LABEL net.skyplabs.maintainer-email="skyper@skyplabs.net"

RUN mkdir /backups

WORKDIR /usr/src/app
ENTRYPOINT ["python", "wp-backup-data"]
CMD ["-d", "/backups"]
