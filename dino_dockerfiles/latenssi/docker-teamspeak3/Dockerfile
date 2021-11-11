FROM ubuntu:16.04

ENV TS3_UID 1000
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y curl bzip2 locales && \
    apt-get clean && rm -rf /var/lib/apt/lists

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8

ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

ENV TEAMSPEAK_VERSION 3.2.0
ENV TEAMSPEAK_URL http://dl.4players.de/ts/releases/${TEAMSPEAK_VERSION}/teamspeak3-server_linux_amd64-${TEAMSPEAK_VERSION}.tar.bz2

RUN cd /opt/ \
    && curl ${TEAMSPEAK_URL} | tar -xj \
    && mkdir -p /data/logs \
    && ln -s /data/ts3server.sqlitedb /opt/teamspeak3-server_linux_amd64/ts3server.sqlitedb

RUN useradd -u ${TS3_UID} ts3 \
    && chown -R ts3 /opt/teamspeak3-server_linux_amd64 \
    && chown -R ts3 /data

VOLUME ["/data"]

EXPOSE 9987/udp 30033 10011

USER ts3

ENTRYPOINT ["/opt/teamspeak3-server_linux_amd64/ts3server_minimal_runscript.sh"]
CMD ["inifile=/data/ts3server.ini", "logpath=/data/logs","licensepath=/data/","query_ip_whitelist=/data/query_ip_whitelist.txt","query_ip_backlist=/data/query_ip_blacklist.txt"]
