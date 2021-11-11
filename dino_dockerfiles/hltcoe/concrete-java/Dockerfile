FROM centos:7

RUN yum update -y && yum clean all

RUN yum install -y \
        java-1.8.0-openjdk-devel \
        maven

RUN useradd -m -U -s /bin/bash concrete && \
    passwd -l concrete
ADD . /home/concrete/concrete-java
RUN cd /home/concrete/concrete-java && \
    mvn clean install \
        -Dskiptests=true \
        -Dmaven.test.skip=true && \
    chown -R concrete:concrete /home/concrete

USER concrete
WORKDIR /home/concrete
