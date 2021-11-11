FROM bde2020/hadoop-base:1.0.0-hadoop2.7.1

MAINTAINER gnaga <giridhar.naga@gmail.com>

ENV HIVE_VERSION 2.1.1

ENV HIVE_HOME /opt/hive
ENV PATH $HIVE_HOME/bin:$PATH
ENV HADOOP_HOME /opt/hadoop-$HADOOP_VERSION

WORKDIR /opt

#Install Hive and PostgreSQL JDBC
RUN apt-get update && apt-get install -y vim python perl wget procps && \
	wget http://www-eu.apache.org/dist/hive/hive-$HIVE_VERSION/apache-hive-$HIVE_VERSION-bin.tar.gz && \
	tar -xzvf apache-hive-$HIVE_VERSION-bin.tar.gz && \
	mv apache-hive-$HIVE_VERSION-bin hive && \
	wget https://jdbc.postgresql.org/download/postgresql-9.4.1209.jre7.jar -O $HIVE_HOME/lib/postgresql-jdbc.jar && \
	rm apache-hive-$HIVE_VERSION-bin.tar.gz && \
	rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y python2.7-dev \
    make \
    libkrb5-dev \
    libxml2-dev \
    libffi-dev \
    libxslt-dev \
    libsqlite3-dev \
    libssl-dev \
    libldap2-dev \
    python-pip \
    ant git gcc g++ libkrb5-dev libffi-dev libmysqlclient-dev libssl-dev libsasl2-dev libsasl2-modules-gssapi-mit libsqlite3-dev libtidy-0.99-0 libxml2-dev libxslt-dev make libldap2-dev maven python-dev python-setuptools libgmp3-dev

RUN cd /root && git clone https://github.com/cloudera/hue.git && cd hue && make apps

#RUN python2.7 /root/hue/tools/virtual-bootstrap/virtual-bootstrap.py \
#        -qq --no-site-packages /root/hue/build/env && cd /root/hue/ && make apps

#CMD  ./build/env/bin/hue runserver &


#Spark should be compiled with Hive to be able to use it
#hive-site.xml should be copied to $SPARK_HOME/conf folder

#Custom configuration goes here
ADD conf/hive-site.xml $HIVE_HOME/conf
ADD conf/beeline-log4j2.properties $HIVE_HOME/conf
ADD conf/hive-env.sh $HIVE_HOME/conf
ADD conf/hive-exec-log4j2.properties $HIVE_HOME/conf
ADD conf/hive-log4j2.properties $HIVE_HOME/conf
ADD conf/ivysettings.xml $HIVE_HOME/conf
ADD conf/llap-daemon-log4j2.properties $HIVE_HOME/conf

COPY startup.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/startup.sh

COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 10000
EXPOSE 10002

ENTRYPOINT ["entrypoint.sh"]
CMD startup.sh
