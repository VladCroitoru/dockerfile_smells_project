FROM logstash:2.3

RUN mkdir /config

RUN wget -O /tmp/mysql-connector-java-5.1.38.tar.gz "http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.38.tar.gz"

RUN tar xzf /tmp/mysql-connector-java-5.1.38.tar.gz -C /config

WORKDIR /config

COPY docker-entrypoint.sh /

COPY logstash.conf.template /config/

CMD ["logstash", "-f", "/config/logstash.conf"]
