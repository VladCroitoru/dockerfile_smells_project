FROM ubuntu:18.10
MAINTAINER Piotr Krzemiński (pio.krzeminski@gmail.com)

RUN apt-get update && apt-get install -y dirmngr ca-certificates wget curl jq netcat

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" |  tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update && apt-get install -y nodejs yarn

RUN apt-get install -y openjdk-11-jdk-headless && update-java-alternatives -s java-1.11.0-openjdk-amd64 && update-ca-certificates -f

ENV MILL_VERSION 0.5.1

RUN \
  curl -L -o /usr/local/bin/mill https://github.com/lihaoyi/mill/releases/download/$MILL_VERSION/$MILL_VERSION && \
  chmod +x /usr/local/bin/mill  
#  touch build.sc && \
#  mill -i resolve _ && \
#  rm build.sc

RUN apt-get install -y postgresql-10 \
 && echo "local all postgres trust" > /etc/postgresql/10/main/pg_hba.conf \
 && echo "host all postgres 127.0.0.1/32 trust" >> /etc/postgresql/10/main/pg_hba.conf


RUN curl -L https://github.com/docker/compose/releases/download/1.24.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose \
 && chmod +x /usr/local/bin/docker-compose

RUN wget -qO- https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/5.2.4/flyway-commandline-5.2.4-linux-x64.tar.gz | tar xvz && ln -s `pwd`/flyway-5.2.4/flyway /usr/local/bin 

RUN apt-get clean && apt-get autoclean && rm -fr /tmp/* /usr/share/man* /usr/share/doc*

