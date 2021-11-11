FROM ubuntu:trusty
MAINTAINER Stephen Pope <spope@projectricochet.com>

RUN sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6 && \
    echo "deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list && \
    sudo apt-get update && \
    sudo apt-get install -y mongodb-org && \
    apt-get install -y python-pip && pip install awscli && \
    mkdir /backup

ENV RESTORE=false

ADD run.sh /run.sh
ADD backup.sh /backup.sh
ADD restore.sh /restore.sh
ADD restore_latest.sh /restore_latest.sh

RUN chmod +x *.sh

HEALTHCHECK --interval=5s --timeout=3s CMD pgrep cron || exit 1

CMD ["/run.sh"]
