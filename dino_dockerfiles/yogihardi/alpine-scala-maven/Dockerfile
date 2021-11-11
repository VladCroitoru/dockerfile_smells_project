FROM frolvlad/alpine-oraclejdk8

ENV SCALA_VERSION=2.10.6 
ENV SCALA_HOME=/usr/share/scala

ENV MAVEN_VERSION 3.6.3
ENV MAVEN_HOME /usr/lib/mvn
ENV PATH $MAVEN_HOME/bin:$PATH

ENV SBT_VERSION 0.13.16

# add id_rsa
RUN mkdir -p /root/.ssh
ADD id_rsa /root/.ssh/id_rsa
RUN chmod 700 /root/.ssh/id_rsa
RUN echo -e "Host *\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config

# NOTE: bash is used by scala/scalac scripts, and it cannot be easily replaced with ash.

RUN apk update && \
    apk add --no-cache --virtual=.build-dependencies wget ca-certificates && \
    apk add --no-cache bash && \
    apk add openssh && \
    apk add sshpass && \
    cd "/tmp" && \
    wget "https://downloads.typesafe.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.tgz" && \
    tar xzf "scala-${SCALA_VERSION}.tgz" && \
    mkdir "${SCALA_HOME}" && \
    rm "/tmp/scala-${SCALA_VERSION}/bin/"*.bat && \
    mv "/tmp/scala-${SCALA_VERSION}/bin" "/tmp/scala-${SCALA_VERSION}/lib" "${SCALA_HOME}" && \
    ln -s "${SCALA_HOME}/bin/"* "/usr/bin/" && \
    apk del .build-dependencies && \
    rm -rf "/tmp/"*

RUN wget http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  tar -zxvf apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  rm apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  mv apache-maven-$MAVEN_VERSION /usr/lib/mvn
  
RUN apk add --no-cache --virtual=build-dependencies curl && \
    curl -sL "https://github.com/sbt/sbt/releases/download/v1.0.4/sbt-1.0.4.tgz" | gunzip | tar -x -C /usr/local && \
    ln -s /usr/local/sbt/bin/sbt /usr/local/bin/sbt && \
    chmod 0755 /usr/local/bin/sbt && \
    apk del build-dependencies

RUN apk add --update curl && \
    rm -rf /var/cache/apk/* 
    
