FROM oberthur/docker-ubuntu:14.04.4

ENV JAVA_HOME /usr/lib/jvm/java-7-oracle/
ENV MAVEN_HOME /usr/share/maven

ENV JAVA_6_HOME /usr/lib/jvm/java-6-oracle/
ENV JAVA_7_HOME /usr/lib/jvm/java-7-oracle/
ENV JAVA_8_HOME /usr/lib/jvm/java-8-oracle/

# get maven
RUN add-apt-repository -y ppa:webupd8team/java \
  && curl -fsSL http://archive.apache.org/dist/maven/maven-3/3.3.3/binaries/apache-maven-3.3.3-bin.tar.gz | tar xzf - -C /usr/share \
  && mv /usr/share/apache-maven-3.3.3 /usr/share/maven \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn \
  && apt-get update \
  && echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections \
  && apt-get install -y git net-tools oracle-java6-installer oracle-java7-installer oracle-java8-installer npm

RUN git clone https://github.com/naver/pinpoint.git /pinpoint

WORKDIR /pinpoint
VOLUME [/pinpoint]
