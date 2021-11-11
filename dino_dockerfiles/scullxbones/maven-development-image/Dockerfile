FROM openjdk:7-jdk

ENV MAVEN_VERSION 3.3.9

RUN mkdir -p /opt/maven/$MAVEN_VERSION

RUN apt-get update && \
    apt-get upgrade --no-install-recommends -y && \
    apt-get install --no-install-recommends -y git-all vim wget && \
    wget http://mirrors.ibiblio.org/apache/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz \
         -O /opt/maven/apache-maven-bin.tar.gz && \
    tar xf /opt/maven/apache-maven-bin.tar.gz -C /opt/maven/$MAVEN_VERSION --strip-components=1 && \
    rm /opt/maven/apache-maven-bin.tar.gz && \
    apt-get remove -y wget && \
    apt-get clean autoclean -y && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt /var/lib/dpkg /var/lib/cache /var/lib/log

CMD ["java","-version"]
