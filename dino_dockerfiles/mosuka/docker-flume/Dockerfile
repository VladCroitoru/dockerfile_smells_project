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

ENV FLUME_GROUP flume
ENV FLUME_USER flume
ENV FLUME_UID 41414
ENV HOME=/home/${FLUME_USER}

RUN apt-get update && \
    apt-get install -y jq tar && \
    apt-get clean && \
    mkdir ${HOME} && \
    groupadd -r ${FLUME_GROUP} && \
    useradd -u ${FLUME_UID} -g ${FLUME_GROUP} -d ${HOME} ${FLUME_USER} && \
    chown -R ${FLUME_USER}:${FLUME_GROUP} ${HOME}

USER ${FLUME_USER}
WORKDIR ${HOME}

ENV FLUME_VERSION 1.6.0
ENV ZOOKEEPER_CLI_VERSION 0.1.3
RUN curl -L -o ${HOME}/apache-flume-${FLUME_VERSION}-bin.tar.gz http://archive.apache.org/dist/flume/${FLUME_VERSION}/apache-flume-${FLUME_VERSION}-bin.tar.gz && \
    tar -C ${HOME} -xf ${HOME}/apache-flume-${FLUME_VERSION}-bin.tar.gz && \
    rm ${HOME}/apache-flume-${FLUME_VERSION}-bin.tar.gz && \
    cp ${HOME}/apache-flume-${FLUME_VERSION}-bin/conf/flume-conf.properties.template ${HOME}/apache-flume-${FLUME_VERSION}-bin/conf/flume-conf.properties && \
    cp ${HOME}/apache-flume-${FLUME_VERSION}-bin/conf/flume-env.sh.template ${HOME}/apache-flume-${FLUME_VERSION}-bin/conf/flume-env.sh && \
    curl -L -o ${HOME}/apache-flume-${FLUME_VERSION}-bin/lib/zookeeper-3.4.6.jar http://central.maven.org/maven2/org/apache/zookeeper/zookeeper/3.4.6/zookeeper-3.4.6.jar && \
    curl -L -o ${HOME}/zookeeper-cli-${ZOOKEEPER_CLI_VERSION}.tgz https://github.com/mosuka/zookeeper-cli/releases/download/${ZOOKEEPER_CLI_VERSION}/zookeeper-cli-${ZOOKEEPER_CLI_VERSION}.tgz && \
    tar -C ${HOME} -xf ${HOME}/zookeeper-cli-${ZOOKEEPER_CLI_VERSION}.tgz && \
    rm ${HOME}/zookeeper-cli-${ZOOKEEPER_CLI_VERSION}.tgz

ENV FLUME_HOME ${HOME}/apache-flume-${FLUME_VERSION}-bin
ENV ZOOKEEPER_CLI_PREFIX ${HOME}/zookeeper-cli-${ZOOKEEPER_CLI_VERSION}

ADD docker-run.sh /usr/local/bin/
ADD docker-stop.sh /usr/local/bin/

EXPOSE 41414

CMD ["/usr/local/bin/docker-run.sh"]
