FROM debian:jessie

RUN \
  export DEBIAN_FRONTEND=noninteractive \
  && apt-get update \
  && apt-get install --no-install-recommends -y gnupg dirmngr \
  && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 8507EFA5 \
  && echo "deb http://repo.percona.com/apt jessie main" > /etc/apt/sources.list.d/percona.list \
  && apt-get update \
  && apt-get -y dist-upgrade \
  && apt-get install --no-install-recommends --auto-remove -y percona-xtrabackup s3cmd rsync percona-server-client \
  && rm -rf /var/lib/apt/lists/* \
  && sed -i 's/^\(bind-address\s.*\) /# \1/' /etc/mysql/my.cnf \
  && sed -i 's/^\(log_error\s.*\)/# \1/' /etc/mysql/my.cnf

ENV AWS_ACCESS_KEY= \
  AWS_SECRET_KEY= \
  S3_BUCKET= \
  S3_PATH=/ \
  MYSQL_PORT=3306 \
  MYSQL_HOST=mysql \
  MYSQL_USER=root \
  MYSQL_PASS= \
  CREATE_ONE_FILE_PER_DB=false
ADD run.sh /run.sh
ADD dump.sh /dump.sh
ADD restore.sh /restore.sh
CMD ["/run.sh"]
