FROM cloudera/quickstart
MAINTAINER Vpon Data Team

ENV KYLIN_HOME=/usr/lib/kylin

WORKDIR /tmp
RUN curl -O http://apache.stu.edu.tw/kylin/apache-kylin-2.1.0/apache-kylin-2.1.0-bin-cdh57.tar.gz && \
    tar xvf apache-kylin-2.1.0-bin-cdh57.tar.gz && \
    mv apache-kylin-2.1.0-bin-cdh57 /usr/lib/kylin && \
    ln -s /etc/hive/conf/hive-site.xml /etc/hadoop/conf.pseudo

ADD kylin /etc/init.d
ADD docker-quickstart-kylin /usr/bin

RUN chmod 755 /etc/init.d/kylin && \
    chmod 755 /usr/bin/docker-quickstart-kylin

EXPOSE 80 7070 8888 18080 50070
VOLUME ["/var/lib/hadoop-hdfs", "/var/lib/mysql"]
ENTRYPOINT ["/usr/bin/docker-quickstart-kylin"]
