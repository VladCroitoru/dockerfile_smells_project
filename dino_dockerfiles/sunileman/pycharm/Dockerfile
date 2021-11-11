FROM centos:latest
MAINTAINER sunile manjee sunilemanjee@gmail.com

#install yum repos
ENV PYCHARM_HOME=/etc/pycharm
RUN yum update -y &&\
    yum install -y which wget git java-1.8.0-openjdk python && yum clean all


#install pycharm
RUN wget -P /tmp/ http://download.jetbrains.com/python/pycharm-community-4.5.4.tar.gz &&\
    mkdir ${PYCHARM_HOME} && tar -xzvf /tmp/pycharm-community-4.5.4.tar.gz -C ${PYCHARM_HOME} --strip=1

#install pip and clean up
RUN wget -P /tmp/ https://bootstrap.pypa.io/get-pip.py && python /tmp/get-pip.py &&\
    rm -rf /var/lib/apt-lists; 

#install scala
ARG SCALA_VERSION=2.11.8
RUN rpm -ivh http://downloads.lightbend.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.rpm

#install spark
RUN curl -s http://www-us.apache.org/dist/spark/spark-1.6.1/spark-1.6.1-bin-hadoop2.6.tgz | tar -xz -C /usr/local/ && cd /usr/local && ln -s spark-1.6.1-bin-hadoop2.6 spark

#install pybuilder
RUN pip install pybuilder


ENTRYPOINT ["/etc/pycharm/bin/pycharm.sh"]
