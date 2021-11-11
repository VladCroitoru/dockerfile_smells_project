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

FROM java:openjdk-8-jre
MAINTAINER Minoru Osuka "minoru.osuka@gmail.com"

ENV SOLR_GROUP solr
ENV SOLR_USER solr
ENV SOLE_UID 8983
ENV HOME /home/${SOLR_USER}

RUN apt-get update && \
    apt-get install -y iproute netcat lsof jq libxml2-utils xmlstarlet tar && \
    apt-get clean && \
    mkdir ${HOME} && \
    groupadd -r ${SOLR_GROUP} && \
    useradd -u ${SOLE_UID} -g ${SOLR_GROUP} -d ${HOME} ${SOLR_USER} && \
    chown -R ${SOLR_USER}:${SOLR_GROUP} ${HOME}

USER ${SOLR_USER}
WORKDIR ${HOME}

ENV SOLR_VERSION 6.1.0
RUN curl -L -o ${HOME}/solr-${SOLR_VERSION}.tgz http://archive.apache.org/dist/lucene/solr/${SOLR_VERSION}/solr-${SOLR_VERSION}.tgz && \
    tar -C ${HOME} -xf ${HOME}/solr-${SOLR_VERSION}.tgz && \
    rm ${HOME}/solr-${SOLR_VERSION}.tgz

ENV SOLR_PREFIX ${HOME}/solr-${SOLR_VERSION}

ADD docker-run.sh /usr/local/bin/
ADD docker-stop.sh /usr/local/bin/

EXPOSE 8983 7983 18983

CMD ["/usr/local/bin/docker-run.sh"]
