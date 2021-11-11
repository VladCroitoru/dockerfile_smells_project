FROM sequenceiq/hadoop-docker:2.6.0
MAINTAINER Qiao, Nan

# install dependencies
RUN yum update; \
yum install -y ant asciidoc cyrus-sasl-devel cyrus-sasl-gssapi gcc gcc-c++ krb5-devel libtidy  libxml2-devel libxslt-devel make mysql mysql-devel openldap-devel python-devel sqlite-devel openssl-devel gmp-devel \
java-1.8.0-openjdk java-1.8.0-openjdk-devel wget; 
ENV JAVA_HOME /etc/alternatives/java_sdk_1.8.0
ENV PATH $JAVA_HOME/bin:$PATH
RUN wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo; \
yum install apache-maven; \
yum clean all 

# install spark
RUN wget http://d3kbcqa49mib13.cloudfront.net/spark-1.5.1-bin-hadoop2.6.tgz /usr/local/
RUN cd /usr/local && ln -s spark-1.5.1-bin-hadoop2.6 spark
ENV SPARK_HOME /usr/local/spark
RUN mkdir $SPARK_HOME/yarn-remote-client
ADD docker_files/yarn-remote-client $SPARK_HOME/yarn-remote-client
ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop
ENV PATH $PATH:$SPARK_HOME/bin:$HADOOP_PREFIX/bin
COPY docker_files/bootstrap.sh /etc/bootstrap.sh
RUN chown root.root /etc/bootstrap.sh
RUN chmod 700 /etc/bootstrap.sh

# install hue
RUN wget https://dl.dropboxusercontent.com/u/730827/hue/releases/3.9.0/hue-3.9.0.tgz /usr/local/
RUN cd /usr/local/hue-3.9.0 && PREFIX=/usr/local make install
ENV HUE_HOME /usr/local/hue
ENV PATH $PATH:HUE_HOME/build/env/bin

WORKDIR /home/bigdata
# Expose HDFS/Hadoop ports
EXPOSE 50020 50090 50070 50010 8020
# Expose Apache Spark ports
EXPOSE 18080 18081 7077
# Expose Hue
EXPOSE 8088 8042 8888
RUN $BOOTSTRAP && $HADOOP_PREFIX/bin/hadoop dfsadmin -safemode leave && $HADOOP_PREFIX/bin/hdfs dfs -put $SPARK_HOME-1.5.1-bin-hadoop2.6/lib /spark
RUN ["hue", "livy_server"]
RUN ["hue", "runserver", "0.0.0.0:8888"]
ENTRYPOINT ["/etc/bootstrap.sh"]
