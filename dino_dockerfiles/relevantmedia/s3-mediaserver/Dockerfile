FROM oraclelinux:latest
# LABEL NAME=mysql

ENV PACKAGE_URL https://repo.mysql.com/yum/mysql-5.6-community/docker/x86_64/mysql-community-server-minimal-5.6.28-2.el7.x86_64.rpm

RUN mkdir /docker-entrypoint-initdb.d
COPY clouse-1.0.2.1-linux-x64/* /tmp/clouse-1.0.2.1-linux-x64/
COPY /docker-entrypoint/* /docker-entrypoint-initdb.d/
# COPY /aws/* /root/.aws/

# Install server
RUN rpmkeys --import http://repo.mysql.com/RPM-GPG-KEY-mysql \
  && yum install -y $PACKAGE_URL \
  && yum install -y libpwquality \
  # && python /docker-entrypoint-initdb.d/get-pip.py \
  # && pip install awscli \
  && rm -rf /var/cache/yum/*
VOLUME /var/lib/mysql

COPY docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 3306
CMD ["mysqld"]
