# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM java:openjdk-7-jre

MAINTAINER Minoru Osuka "minoru.osuka@gmail.com"

ENV ZOOKEEPER_GROUP zookeeper
ENV ZOOKEEPER_USER zookeeper
ENV ZOOKEEPER_UID 2181
ENV HOME /home/${ZOOKEEPER_USER}

RUN apt-get update && \
    apt-get install -y iproute netcat dnsutils curl tar && \
    apt-get clean && \
    mkdir -p ${HOME} && \
    groupadd -r ${ZOOKEEPER_GROUP} && \
    useradd -u ${ZOOKEEPER_UID} -g ${ZOOKEEPER_GROUP} -d ${HOME} ${ZOOKEEPER_USER} && \
    chown -R ${ZOOKEEPER_USER}:${ZOOKEEPER_GROUP} ${HOME}

USER ${ZOOKEEPER_USER}
WORKDIR ${HOME}

ENV ZOOKEEPER_VERSION 3.5.1-alpha
RUN curl -L -o ${HOME}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz http://archive.apache.org/dist/zookeeper/zookeeper-${ZOOKEEPER_VERSION}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz && \
    tar -C ${HOME} -xf ${HOME}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz && \
    mv ${HOME}/zookeeper-${ZOOKEEPER_VERSION} ${HOME}/zookeeper && \
    rm ${HOME}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz

ENV ZOOKEEPER_PREFIX ${HOME}/zookeeper

ADD docker-run.sh /usr/local/bin
ADD docker-stop.sh /usr/local/bin

EXPOSE 2181 2888 3888

CMD ["/usr/local/bin/docker-run.sh"]
