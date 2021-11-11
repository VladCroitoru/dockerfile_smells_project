FROM openjdk:8

EXPOSE 8080

RUN apt-get install wget \
  && wget http://mirror.olnevhost.net/pub/apache/zeppelin/zeppelin-0.6.1/zeppelin-0.6.1-bin-netinst.tgz \
  && tar xzvf zeppelin-0.6.1-bin-netinst.tgz \
  && rm zeppelin-0.6.1-bin-netinst.tgz \
  && /zeppelin-0.6.1-bin-netinst/bin/install-interpreter.sh --all

COPY spark-defaults.conf /opt/zeppelin-0.6.1-bin-netinst/conf/spark-defaults.conf

CMD ["/zeppelin-0.6.1-bin-netinst/bin/zeppelin.sh"]
