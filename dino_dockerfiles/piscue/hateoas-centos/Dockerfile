FROM centos:7
MAINTAINER Victor Sanahuja piscue@gmail.com
RUN yum -y update >/dev/null 2>&1 \
    && yum -y install git java-1.8.0-openjdk java-1.8.0-openjdk-devel wget >/dev/null 2>&1
RUN wget -nv \
    http://mirror.olnevhost.net/pub/apache/maven/maven-3/3.5.3/binaries/apache-maven-3.5.3-bin.tar.gz \
    && tar xf apache-maven-3.5.3-bin.tar.gz \
    && mv apache-maven-3.5.3 /usr/local/apache-maven \
    && echo 'export M2_HOME=/usr/local/apache-maven' >> ~/.bashrc \
    && echo 'export M2=$M2_HOME/bin' >> ~/.bashrc \
    && echo 'export PATH=$M2:$PATH' >> ~/.bashrc \
    && source ~/.bashrc
RUN git clone https://github.com/spring-projects/spring-boot
RUN yum -y install which
RUN cd spring-boot/spring-boot-samples/spring-boot-sample-hateoas && \
    /usr/local/apache-maven/bin/mvn package
WORKDIR /spring-boot/spring-boot-samples/spring-boot-sample-hateoas
EXPOSE 8080
CMD ["java", "-jar", "target/spring-boot-sample-hateoas-2.0.1.BUILD-SNAPSHOT.jar"]
