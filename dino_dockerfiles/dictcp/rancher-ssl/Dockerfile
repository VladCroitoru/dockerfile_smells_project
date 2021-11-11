FROM nginx

RUN echo "deb http://ftp.debian.org/debian jessie-backports main" | tee -a /etc/apt/sources.list

RUN apt-get update \
    && apt-get install -y bc cron \
    && apt-get install -y letsencrypt -t jessie-backports \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src
WORKDIR /usr/src
COPY . /usr/src

RUN echo "0 12,6 * * * /usr/src/renew.sh" | tee -a /var/spool/cron/root \
    && chmod +x /usr/src/renew.sh \
    && chmod +x /usr/src/start.sh

RUN /etc/init.d/cron start \
    && update-rc.d cron defaults

CMD ["/bin/sh", "-c", "./start.sh"]
