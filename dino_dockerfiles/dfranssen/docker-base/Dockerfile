FROM ubuntu:14.04
MAINTAINER Dirk Franssen "dirk.franssen@gmail.com"

# One could force a daily or weekly upgrade of all
# packages by changing the REFRESHED_AT date, from time to time.
# Otherwise the first lines would be cached by docker and
# one would always use non up-to-date versions of the OS

ENV REFRESHED_AT 2014-10-14

RUN sed 's/main$/main universe/' -i /etc/apt/sources.list && \
        apt-get update && \
        apt-get -y install man wget curl && \
        apt-get clean

ENV JVM_ROOT_PATH /usr/lib/jvm
RUN mkdir -p $JVM_ROOT_PATH

# I personally prefer not to depend on a ppa package to install 'a version' of jdk1.8
# This will install JDK1.8 (8u20-b26 to be exact :-))
RUN wget --header "Cookie: oraclelicense=accept-securebackup-cookie" \
    http://download.oracle.com/otn-pub/java/jdk/8u20-b26/jdk-8u20-linux-x64.tar.gz -O /tmp/jdk-8u20-linux-x64.tar.gz && \
    echo "ec7f89dc3697b402e2c851d0488f6299  /tmp/jdk-8u20-linux-x64.tar.gz" | md5sum -c && \
    tar -zxf /tmp/jdk-8u20-linux-x64.tar.gz -C $JVM_ROOT_PATH && \
    chown -R root:root $JVM_ROOT_PATH && \
    rm /tmp/jdk-8u20-linux-x64.tar.gz

ENV JAVA_HOME $JVM_ROOT_PATH/jdk1.8.0_20
ENV PATH $JAVA_HOME/bin:$PATH

#Note: Here it is just set in the PATH env, because this image is less big than the update-alternatives one.
#See https://github.com/dfranssen/docker-files/tree/master/docker-base-ubuntu/java8-update-alternatives
