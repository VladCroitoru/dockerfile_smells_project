# Forked from: https://github.com/apache/hadoop/blob/123b3db743a86aa18e46ec44a08f7b2e7c7f6350/dev-support/docker/Dockerfile
# 
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM ubuntu:trusty
MAINTAINER Akihiro Suda

ENV MAVEN_OPTS -Xms256m -Xmx512m
ENV JAVA_HOME /usr/lib/jvm/default-java

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
      openjdk-7-jdk \
      openssh-server openssh-client \
      git curl ant make maven \
      cmake gcc g++ protobuf-compiler \
      build-essential libtool \
      zlib1g-dev pkg-config libssl-dev \
      snappy libsnappy-dev \
      bzip2 libbz2-dev \
      libjansson-dev \
      fuse libfuse-dev \
      libcurl4-openssl-dev \
      python python2.7

# Fixing the Apache commons / Maven dependency problem under Ubuntu:
# See http://wiki.apache.org/commons/VfsProblems
RUN cd /usr/share/maven/lib && ln -s ../../java/commons-lang.jar .

RUN ssh-keygen -b 2048 -t rsa -f /root/.ssh/id_rsa -q -N "" && \
    cp -f /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys

RUN mkdir /src
# how can we keep the maven cache?
ADD hadoop /src/hadoop
WORKDIR /src/hadoop
RUN mvn package -Pdist,native -DskipTests

RUN cp -R /src/hadoop/hadoop-dist/target/hadoop-3.0.0-SNAPSHOT /hadoop
ADD etc-customized/hadoop /hadoop/etc/hadoop
ENV PATH /hadoop/bin:/hadoop/sbin:$PATH

RUN hadoop version
