FROM alpine:3.3

MAINTAINER wuqq wqzhiep@gmail.com

# install dependencies
RUN apk update &&\
    apk add --no-cache mysql mysql-client &&\
    apk add --no-cache redis &&\
    apk add --no-cache openjdk7-jre &&\
    rm -f /var/cache/apk/* &&\
    mysql_install_db --user=root &> /dev/null &&\
    mkdir -p /run/mysqld

ENV TERM dumb

# install jboss
COPY jboss-eap-6.4.0.zip .
RUN  unzip jboss-eap-6.4.0 &&\
     rm -rf jboss-eap-6.4.0.zip
COPY standalone.xml jboss-eap-6.4/standalone/configuration/

# config mysql
COPY my.cnf /etc/mysql/my.cnf

ADD start.sh .
RUN chmod +x start.sh

CMD ["./start.sh"]
