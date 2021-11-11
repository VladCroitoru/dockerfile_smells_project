FROM heyman/postgresql
MAINTAINER Jonatan Heyman <http://heyman.info>

RUN apt-get update && apt-get install -y \
    python \
    python2.7 \
    python-dev \
    python-setuptools \
    unzip

RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
RUN unzip awscli-bundle.zip
RUN ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws
RUN aws configure set default.s3.signature_version s3v4
RUN rm -rf awscli-bundle.zip awscli-bundle

VOLUME ["/data/backups"]

ENV BACKUP_DIR /data/backups

ADD . /backup
RUN touch /backup.log

ENTRYPOINT ["/backup/entrypoint.sh"]
CMD cron && tail -f /backup.log
