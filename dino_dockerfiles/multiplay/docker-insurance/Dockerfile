FROM alpine
MAINTAINER Jan Garaj <info@monitoringartist.com>

ADD run /docker-backup/
ADD docker_backup.py /docker-backup/
ADD s3cfg /.s3cfg

RUN \
  apk update && \
  apk upgrade && \
  apk add git py-pip python py-setuptools py-dateutil ssmtp bash && \
  git clone https://github.com/s3tools/s3cmd.git /s3cmd && \
  pip install docker-py && \
  cd /s3cmd && \
  python setup.py install && \
  chmod +x /docker-backup/run

ENTRYPOINT [ "/docker-backup/run" ]
