FROM nimmis/ubuntu:14.04

MAINTAINER wendal "wendal1985@gmail.com"

ENV DEBIAN_FRONTEND noninteractive
ENV JAVA_HOME /opt/jdk

RUN cd /opt/   \
    && wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u102-b14/jdk-8u102-linux-x64.tar.gz" \
    && tar xzf jdk-8u102-linux-x64.tar.gz \
    && ln -s /opt/jdk1.8.0_102 /opt/jdk \
    && rm jdk-8u102-linux-x64.tar.gz \
	&& cd jdk && rm -rf src.zip javafx-src.zip db man ./jre/lib/amd64/libjfxwebkit.so

COPY local_policy.jar /opt/jdk/jre/lib/security/
COPY US_export_policy.jar /opt/jdk/jre/lib/security/
