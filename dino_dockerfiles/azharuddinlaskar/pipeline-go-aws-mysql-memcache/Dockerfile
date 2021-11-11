FROM golang:latest
MAINTAINER Azhar Uddin Laskar

ENV MYSQL_MAJOR 5.7
ENV MYSQL_ROOT_PASSWORD root
ENV GOOSE_DIR /db
ENV TZ Asia/Singapore
ENV APP_PORT 443
ENV APP_REF_DOCS http://0.0.0.0:8081
ENV APP_ACCESS_LOG /log/access.log
ENV APP_ENV TESTING
ENV APP_NAME myapp
ENV REPO_OWNER github.com/someone

# Update and Fix Language
RUN \
 apt-get update && apt-get -y upgrade &&\
 apt-get -y --no-install-recommends install locales &&\
 echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen &&\
 locale-gen en_US.UTF-8 &&\
 /usr/sbin/update-locale LANG=en_US.UTF-8

# Add MySQL repository
RUN \
 apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys A4A9406876FCBD3C456770C88C718D3B5072E1F5 &&\
 echo "deb http://repo.mysql.com/apt/debian/ jessie mysql-$MYSQL_MAJOR" > /etc/apt/sources.list.d/mysql.list &&\
 apt-get update &&\
 { \
       echo mysql-community-server mysql-community-server/data-dir select ''; \
       echo mysql-community-server mysql-community-server/root-pass password $MYSQL_ROOT_PASSWORD; \
       echo mysql-community-server mysql-community-server/re-root-pass password $MYSQL_ROOT_PASSWORD; \
       echo mysql-community-server mysql-community-server/remove-test-db select false; \
   } | debconf-set-selections &&\
 apt-get -y --no-install-recommends install mysql-server

# Install built in's
RUN \
 apt-get -y --no-install-recommends install mysql-client redis-server &&\
 apt-get autoclean && apt-get clean && apt-get autoremove &&\
 apt-get -y install unzip groff

# Install Goose
RUN go get bitbucket.org/liamstask/goose/cmd/goose

RUN \
 curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" &&\
 unzip awscli-bundle.zip &&\
 ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws &&\
 rm -rfv awscli-bundle awscli-bundle.zip

RUN \
 curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest &&\
 chmod 755 /usr/local/bin/ecs-cli

ADD scripts /scripts
RUN chmod -R 755 /scripts
ENV PATH $PATH:/scripts

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends apt-utils &&\
 DEBIAN_FRONTEND=noninteractive apt-get -y install memcached
