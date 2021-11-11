FROM strider/strider-docker-slave
MAINTAINER Fernando Neto <fernando.neto27051987@gmail.com>

USER root 

ENV DEBIAN_FRONTEND noninteractive
ENV MYSQL_DATABASE aas_test
ENV MYSQL_USER aas_test
ENV MYSQL_PASSWORD aas_test
ENV MYSQL_MAJOR 5.6
ENV MYSQL_VERSION 5.6.24
WORKDIR /home/strider/worksapce
ENV HOME /home
ENV STRIDER_CLONE_DEST=/tmp

RUN apt-get update
RUN groupadd -r mysql && useradd -r -g mysql mysql
RUN apt-get update && apt-get install -y ca-certificates git nodejs-legacy npm procps nano perl --no-install-recommends && rm -rf /var/lib/apt/lists/*
RUN apt-key adv --keyserver pool.sks-keyservers.net --recv-keys A4A9406876FCBD3C456770C88C718D3B5072E1F5
RUN npm install -g strider-docker-slave@latest
RUN locale-gen en_US.UTF-8
RUN echo "deb http://repo.mysql.com/apt/debian/ wheezy mysql-${MYSQL_MAJOR}" > /etc/apt/sources.list.d/mysql.list
RUN { \
                echo mysql-community-server mysql-community-server/data-dir select ''; \
                echo mysql-community-server mysql-community-server/root-pass password ''; \
                echo mysql-community-server mysql-community-server/re-root-pass password ''; \
                echo mysql-community-server mysql-community-server/remove-test-db select false; \
        } | debconf-set-selections \
        && apt-get update && apt-get install -y mysql-server="${MYSQL_VERSION}"* && rm -rf /var/lib/apt/lists/* \
        && rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql

VOLUME /var/lib/mysql
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD strider-docker-slave
