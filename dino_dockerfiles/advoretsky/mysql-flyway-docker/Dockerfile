FROM java:8

ENV fwversion 4.0
ENV mysqlversion 5.6

RUN wget -O mysql-apt-config.deb https://dev.mysql.com/get/mysql-apt-config_0.3.7-1debian8_all.deb \
   && dpkg -i mysql-apt-config.deb \
   && apt-get update \
   && apt-get install mysql-client-5.6 -y \
   && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

ADD http://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/$fwversion/flyway-commandline-$fwversion.zip /tmp/flyway.zip
RUN cd /tmp && unzip /tmp/flyway.zip && rm /tmp/flyway.zip \
    && mv /tmp/flyway-$fwversion /usr/local/flyway-$fwversion \
    && ln -s /usr/local/flyway-$fwversion/flyway /usr/local/bin/flyway


