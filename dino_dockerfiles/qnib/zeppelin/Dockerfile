FROM qnib/d-java7

ENV ZEPPELIN_VER=0.6.0

RUN wget -qO - http://supergsego.com/apache/zeppelin/zeppelin-${ZEPPELIN_VER}/zeppelin-${ZEPPELIN_VER}-bin-all.tgz |tar xfz - -C /opt/ \
 && mv /opt/zeppelin-${ZEPPELIN_VER}-bin-all /opt/zeppelin
ADD etc/supervisord.d/zeppelin.ini /etc/supervisord.d/
