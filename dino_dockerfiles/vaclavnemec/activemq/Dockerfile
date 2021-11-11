FROM vtajzich/java:oracle-java8

WORKDIR /home/activemq/

ADD http://apache.miloslavbrada.cz/activemq/5.13.0/apache-activemq-5.13.0-bin.tar.gz /home/activemq/

RUN tar -zxvf apache-activemq-5.13.0-bin.tar.gz && rm apache-activemq-5.13.0-bin.tar.gz

EXPOSE 8161 61616

CMD /home/activemq/apache-activemq-5.13.0/bin/activemq console
