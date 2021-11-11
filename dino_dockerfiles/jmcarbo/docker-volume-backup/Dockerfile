FROM ubuntu
MAINTAINER Joan Marc Carbo Arnau <jmcarbo@gmail.com>

RUN apt-get update && \
    apt-get install -y mysql-client curl cron && \
    curl https://dl.minio.io/client/mc/release/linux-amd64/mc > /usr/local/bin/mc && \
    chmod +x /usr/local/bin/mc && \ 
    mkdir /backup

ENV CRON_TIME="0 0 * * *" 

ADD restic_app /usr/local/bin/restic
RUN chmod +x /usr/local/bin/restic
ADD run.sh /run.sh
RUN chmod +x /run.sh
VOLUME ["/backup"]

CMD ["/run.sh"]
