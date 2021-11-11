FROM timmyraynor/spark:latest
MAINTAINER Tim.Qin<qinyujue@gmail.com>

# add python into for pyspark
RUN apt-get install -y python

RUN wget -q -O /tmp/zeppelin-0.7.0-bin-all.tgz http://apache.uberglobalmirror.com/zeppelin/zeppelin-0.7.0/zeppelin-0.7.0-bin-all.tgz
# install zeppelin
RUN tar -xzf /tmp/zeppelin-0.7.0-bin-all.tgz -C /usr/local
RUN cd /usr/local && ln -s ./zeppelin-0.7.0-bin-all zeppelin

ENV ZEPPELIN_HOME /usr/local/zeppelin
ADD zeppelin-env.sh $ZEPPELIN_HOME/conf/
ADD bootstrap-zeppelin.sh /etc/
RUN chown root.root /etc/bootstrap-zeppelin.sh
RUN chmod 777 /etc/bootstrap-zeppelin.sh

ENTRYPOINT ["/etc/bootstrap-zeppelin.sh"]

