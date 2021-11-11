FROM instructure/java:8

ENV SPARK_HOME /usr/share/spark
ENV JAVA_OPTIONS "-Xmx1500m -XX:MaxPermSize=512m -Dakka.test.timefactor=3"

USER root
# install and cache sbt, python

RUN echo 'deb http://dl.bintray.com/sbt/debian /' > /etc/apt/sources.list.d/sbt.list && \
    apt-get -qq update && \
    apt-get install -y --force-yes python3 python3-pip python-pip sbt=0.13.12 unzip && \
    sbt
# running sbt downloads some of its internals, speed up sebsequent sbt runs

RUN pip install --upgrade pip && \
    pip install py4j pyhocon tox && \
    pip3 install --upgrade pip && \
    pip3 install py4j pyhocon tox

RUN mkdir ${SPARK_HOME} && \
    curl -L -o /tmp/spark.tgz http://apache.lauf-forum.at/spark/spark-2.3.2/spark-2.3.2-bin-hadoop2.7.tgz && \
    tar xzf /tmp/spark.tgz --strip-components=1 --directory ${SPARK_HOME} && \
    rm /tmp/spark.tgz

RUN curl http://www.h2database.com/h2-2014-04-05.zip -o h2.zip && \
    unzip h2.zip -d /opt/ && \
    rm h2.zip && \
    mkdir -p /opt/h2-data

COPY h2-server.sh /opt/h2/bin

EXPOSE 1521
