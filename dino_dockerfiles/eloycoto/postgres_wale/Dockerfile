FROM postgres:9.6

MAINTAINER Eloy Coto <eloy.coto@gmail.com>
ENV LANG en_GB.UTF-8

RUN apt-get update && \
    apt-get install -y python3-pip python3.4 lzop pv daemontools sudo locales&& \
    pip3 install wal-e[aws] && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    echo 'en_GB.UTF-8 UTF-8' >> /etc/locale.gen && \
    locale-gen en_GB.UTF-8 && \
    /usr/sbin/update-locale LANG=en_GB.UTF-8

COPY entrypoint.sh postgresql.conf pg_hba.conf /
ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 5432
