#
# VERSION               0.0.1
FROM centos:6
MAINTAINER Fanday Dai "fandaydai@live.cn"

ENV JAVA_VER 1.8.0_20
ENV JAVA_DWL_VER 8u20
ENV JAVA_DWL_BVER b26


ENV JAVA_HOME /opt/java
ENV JDK_HOME ${JAVA_HOME}
ENV PATH ${JAVA_HOME}/bin:${PATH}

RUN yum install -y wget tar
RUN wget --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/${JAVA_DWL_VER}-${JAVA_DWL_BVER}/jdk-${JAVA_DWL_VER}-linux-x64.tar.gz
RUN ls
RUN tar xzf jdk-${JAVA_DWL_VER}-linux-x64.tar.gz -C /opt

RUN mv /opt/jdk${JAVA_VER}/jre /opt/jre${JAVA_VER}
RUN mv /opt/jdk${JAVA_VER}/lib/tools.jar /opt/jre${JAVA_VER}/lib/ext
RUN rm -Rf /opt/jdk${JAVA_VER}
RUN ln -s /opt/jre${JAVA_VER} /opt/java

CMD /bin/bash
