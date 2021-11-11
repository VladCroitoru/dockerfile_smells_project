FROM centos:centos7
MAINTAINER ome-devel@lists.openmicroscopy.org.uk

ENV MAVEN_VERSION=3.3.9

RUN yum install -y java-1.8.0-openjdk-devel tar

# Don't use maven from repos because it pulls in Java 7
RUN curl -L -o apache-maven-$MAVEN_VERSION-bin.tar.gz \
	http://mirror.olnevhost.net/pub/apache/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz && \
	tar -zxvf apache-maven-$MAVEN_VERSION-bin.tar.gz && \
	mv apache-maven-$MAVEN_VERSION /opt/maven && \
	rm apache-maven-$MAVEN_VERSION-bin.tar.gz

RUN useradd build
COPY . /home/build/src/
RUN chown -R build:build /home/build/src

USER build
WORKDIR /home/build/src

# mvn needs JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java
RUN /opt/maven/bin/mvn install

WORKDIR /mineotaur
ENTRYPOINT ["java", "-jar", "/home/build/src/target/Mineotaur-1.0.1.jar"]
CMD ["-help"]

