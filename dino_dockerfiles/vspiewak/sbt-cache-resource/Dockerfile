FROM anapsix/alpine-java:8
MAINTAINER Vincent Spiewak <vspiewak@googlemailadress>

RUN apk update && apk add --no-cache \
    openssl \
    openssh-client \
    jq \
    curl \
    git \
    rsync

# Install git lfs
ENV GIT_LFS_VERSION=2.0.1

RUN mkdir -p /tmp/gitlfs && \
    cd /tmp/gitlfs && \
    curl -sLO https://github.com/github/git-lfs/releases/download/v${GIT_LFS_VERSION}/git-lfs-linux-amd64-${GIT_LFS_VERSION}.tar.gz && \
    tar xf git-lfs-linux-amd64-${GIT_LFS_VERSION}.tar.gz && \
    mv git-lfs-${GIT_LFS_VERSION}/git-lfs /usr/bin/ && \
    cd /tmp && \
    rm -Rf /tmp/gitlfs


# Pull down git resource into our dockerfile
RUN mkdir -p /opt/resource/git && mkdir -p /var/cache/git && \
    wget https://github.com/concourse/git-resource/archive/master.zip -O /opt/resource/git/git-resource.zip && \
    unzip /opt/resource/git/git-resource.zip -d /opt/resource/git && \
    mv /opt/resource/git/git-resource-master/assets/* /opt/resource/git && \
    rm -r /opt/resource/git/git-resource.zip /opt/resource/git/git-resource-master

# Install SBT
ENV SBT_VERSION 0.13.13
ADD sbt.sh /usr/local/bin/sbt
RUN curl -sL "https://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/sbt-launch/${SBT_VERSION}/sbt-launch.jar" \
        > /usr/local/bin/sbt-launch.jar \
    && chmod +x /usr/local/bin/sbt \
    && sbt update

# Install sbt cache resource
ADD assets/ /opt/resource/
RUN chmod +x /opt/resource/*
