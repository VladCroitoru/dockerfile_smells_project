FROM frolvlad/alpine-glibc:latest

MAINTAINER Patrick Eichmann <phreakazoid@phreakazoid.com>

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.docker.dockerfile="/Dockerfile" \
      org.label-schema.name="docker-teamspeak" \
      org.label-schema.description="Teamspeak Server on Alpine Linux" \
      org.label-schema.url="https://github.com/phreakazoid/docker-teamspeak" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/phreakazoid/docker-teamspeak.git" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

ENV TEAMSPEAK_VERSION 3.8.0
ENV TEAMSPEAK_URL http://dl.4players.de/ts/releases/${TEAMSPEAK_VERSION}/teamspeak3-server_linux_amd64-${TEAMSPEAK_VERSION}.tar.bz2
ENV TS3_UID 1000

RUN apk update && apk add ca-certificates && rm -rf /var/cache/apk/*

RUN adduser -S -D -u ${TS3_UID} ts3 \
  && mkdir -p /home/ts3 \
  && wget -q -O /home/ts3/teamspeak3-server_linux_amd64.tar.bz2 ${TEAMSPEAK_URL} \
  && tar --directory /home/ts3 -xjf /home/ts3/teamspeak3-server_linux_amd64.tar.bz2 \
  && rm /home/ts3/teamspeak3-server_linux_amd64.tar.bz2 \
  && mkdir -p /home/ts3/data/logs \
  && mkdir -p /home/ts3/data/files \
  && ln -s /home/ts3/data/files /home/ts3/teamspeak3-server_linux_amd64/files \
  && ln -s /home/ts3/data/ts3server.sqlitedb /home/ts3/teamspeak3-server_linux_amd64/ts3server.sqlitedb \
  && chown -R ts3 /home/ts3 
# Symlink because i dont know how to move sqlite-db (like dbpath=/data/ts/mysqlite.db)

USER ts3
ENTRYPOINT ["/home/ts3/teamspeak3-server_linux_amd64/ts3server_minimal_runscript.sh"]
CMD ["inifile=/home/ts3/data/ts3server.ini", "logpath=/home/ts3/data/logs","licensepath=/home/ts3/data/","query_ip_whitelist=/home/ts3/data/query_ip_whitelist.txt","query_ip_backlist=/home/ts3/data/query_ip_blacklist.txt","license_accepted=1"]

VOLUME ["/home/ts3/data"]

# Expose the Standard TS3 port, for files, for serverquery
EXPOSE 9987/udp 30033 10011
