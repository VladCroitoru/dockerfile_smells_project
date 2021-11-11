# The MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

FROM ubuntu:16.04
MAINTAINER Elmar Weber <elmar(.)weber(@)cupenya(.)com>

ENV TERM linux

# Install Java.
RUN \
  apt-get update && \
  apt-get install -y openjdk-8-jdk


# Install packages that are too stupid to not have
RUN apt-get install -y unzip curl wget



USER root



## Base Setup

# install basic build tools
RUN apt-get update && \
    apt-get install -y git

# get supervisord up and running
RUN apt-get update && \
    apt-get install -y supervisor sudo

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY sudoers /etc/sudoers

ENV HOME /home/jenkins
RUN useradd -c "Jenkins user" -d $HOME -m -G sudo jenkins

ARG VERSION=4.3
RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/${VERSION}/remoting-${VERSION}.jar \
     && chmod 755 /usr/share/jenkins \
     && chmod 644 /usr/share/jenkins/slave.jar

COPY jenkins-slave /usr/local/bin/jenkins-slave


WORKDIR /home/jenkins
USER jenkins

ENTRYPOINT ["jenkins-slave"]

## End Base Setup

## Setup Mongo

USER root

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6

RUN echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.4.list
RUN apt-get update && apt-get install -y mongodb-org=3.4.7 mongodb-org-server=3.4.7 mongodb-org-shell=3.4.7 mongodb-org-mongos=3.4.7 mongodb-org-tools=3.4.7
RUN mkdir -p /data/db

COPY supervisord-mongod.conf /etc/supervisor/conf.d/mongod.conf

# restore user for jenkins slave
USER jenkins


## End Setup mongo

## Setup Elastic Search
USER root
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys 46095ACC8548582C1A2699A9D27D666CD88E42B4

ENV ELASTICSEARCH_VERSION 2.3.3
ENV ELASTICSEARCH_REPO_BASE http://packages.elasticsearch.org/elasticsearch/2.x/debian

RUN echo "deb $ELASTICSEARCH_REPO_BASE stable main" > /etc/apt/sources.list.d/elasticsearch.list && \
  apt-get update && \
  apt-get install -y elasticsearch=$ELASTICSEARCH_VERSION

WORKDIR /usr/share/elasticsearch
RUN for path in \
    ./data \
    ./logs \
    ./config \
    ./config/scripts \
    ; do \
    mkdir -p "$path"; \
    chown -R elasticsearch:elasticsearch "$path"; \
    done

COPY config ./config

COPY supervisord-elasticsearch.conf /etc/supervisor/conf.d/elasticsearch.conf

# Restore user for Jenkins slave
USER jenkins
WORKDIR /home/jenkins


## End Setup Elastic Search



## cpy-root setup
USER root
# add npm, gulp and bower
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
   apt-get update && \
   apt-get install -y nodejs && \
   npm --global install yarn && \
   npm --global install gulp && \
   npm --global install bower && \
   # fix permissions done during install
   chown jenkins:jenkins -R /home/jenkins/.npm

# add ES plugin
COPY elasticsearch-business-hours-2-3-3-SNAPSHOT.zip /tmp
RUN /usr/share/elasticsearch/bin/plugin install -t 30s file:///tmp/elasticsearch-business-hours-2-3-3-SNAPSHOT.zip && \
  rm /tmp/elasticsearch-business-hours-2-3-3-SNAPSHOT.zip

# add k8s

ENV K8S_VERSION 1.14.10

RUN set -x && \
    wget -O /bin/kubectl "https://storage.googleapis.com/kubernetes-release/release/v1.14.10/bin/linux/amd64/kubectl" && \
    chmod +x /bin/kubectl

# add other utils required for k8s pipelines
RUN apt-get install -y jq
RUN npm install -g mustache

# add gcloud
RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
    echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update && apt-get install -y google-cloud-sdk

# add docker


RUN wget https://download.docker.com/linux/static/stable/x86_64/docker-18.09.7.tgz && \
    tar xvfz docker-18.09.7.tgz && \
    mv docker/docker /usr/bin/docker && \
    rm docker-18.09.7.tgz && \
    rm -Rf docker

# add docker setup script, docker daemon is bound via host path
USER root

COPY setup-docker-and-start-jenkins.sh /setup-docker-and-start-jenkins.sh
RUN chmod 755 /setup-docker-and-start-jenkins.sh

# overwrite default entry point to wrap docker user and group creation
ENTRYPOINT ["/setup-docker-and-start-jenkins.sh"]
