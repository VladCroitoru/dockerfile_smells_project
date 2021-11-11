FROM docker.io/1and1internet/ubuntu-16-apache-php-7.1:latest
ARG DEBIAN_FRONTEND=noninteractive
COPY files /
RUN \
  groupadd cbpolicyd && \
  useradd -g cbpolicyd cbpolicyd && \
  apt-get update && \
  apt-get -o Dpkg::Options::=--force-confdef -y install gettext-base postfix-cluebringer postfix-cluebringer-mysql postfix-cluebringer-webui -y && \
  apt-get -y clean && \
  rm -rf /var/lib/apt/lists/* /etc/cluebringer && \
  mkdir --mode=0775 /etc/cluebringer && \
  cp /usr/share/doc/postfix-cluebringer/database/policyd-db.mysql.gz /tmp/ && \
  cp -r /usr/share/postfix-cluebringer-webui/webui/* /var/www/html/ && \
  gunzip /tmp/policyd-db.mysql.gz && \
  sed -i -e 's/TYPE=InnoDB/ENGINE=InnoDB/g' /tmp/policyd-db.mysql && \
  chmod -R 0755 /hooks && \
  chmod -R 0777 /var/www/html && \
  chmod 0666 /var/log/cbpolicyd.log
ENV MYSQL_ROOT_PASSWORD=ReplaceWithENVFromBuild \
    MYSQL_DATABASE=cluebringer \
    MYSQL_USER=cluebringer \
    MYSQL_PASSWORD=ReplaceWithENVFromBuild \
    CLUEBRINGER_DB_BACKEND=mysql \
    CLUEBRINGER_DB_PORT=3306 \
    CLUEBRINGER_DB_HOST=policyd_mysql \
    WEBUI_PASSWORD=ReplaceWithENVFromBuild
EXPOSE 10031 8080 8443
