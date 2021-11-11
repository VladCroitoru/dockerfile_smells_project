FROM navicore/spark:1.6.2a

ENV ZEPPELIN_VER  0.6.2

RUN mkdir -p /opt && cd /opt && curl http://www.us.apache.org/dist/zeppelin/zeppelin-${ZEPPELIN_VER}/zeppelin-${ZEPPELIN_VER}-bin-all.tgz | tar -zx && ln -s zeppelin-${ZEPPELIN_VER}-bin-all zeppelin && echo Zeppelin ${ZEPPELIN_VER} installed in /opt

ADD files/zeppelin-log4j.properties /opt/zeppelin/conf/log4j.properties
ADD files/zeppelin-env.sh /opt/zeppelin/conf/zeppelin-env.sh
ADD files/docker-zeppelin.sh /opt/zeppelin/bin/docker-zeppelin.sh

EXPOSE 8080
ENTRYPOINT ["/opt/zeppelin/bin/docker-zeppelin.sh"]

