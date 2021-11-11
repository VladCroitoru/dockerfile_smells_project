# This is a copy of jenkins/jnlp-slave with Maven

# The MIT License
#
#  Copyright (c) 2015-2017, CloudBees, Inc. and other Jenkins contributors
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

FROM openjdk:8-jdk

MAINTAINER Martin Goldhahn <mgoldhahn@gmail.com>

ARG MAVEN_VERSION=3.5.2
ARG MAVEN_SHA1=190dcebb8a080f983af4420cac4f3ece7a47dd64
ARG SLAVE_VERSION=3.16
ARG SLAVE_SHA1=98133ca4027b00ed1a1d87241708ac05acc20e8b
ARG JNLP_TAG=3.16-1
ARG JNLP_SHA1=d537b4885845524b98be001a2845362f396d58aa
ARG AGENT_WORKDIR=/home/jenkins/agent


ARG HOME=/home/jenkins
RUN groupadd -g 10000 jenkins
RUN useradd -c "Jenkins user" -d $HOME -u 10000 -g 10000 -m jenkins
LABEL Description="This is a jenkins slave including maven"

# download jenkins agent
RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/${SLAVE_VERSION}/remoting-${SLAVE_VERSION}.jar \
    && sha1sum /usr/share/jenkins/slave.jar | grep ${SLAVE_SHA1} \
    && chmod 755 /usr/share/jenkins \
    && chmod 644 /usr/share/jenkins/slave.jar

# download jenkins-jnlp-agent
RUN cd /tmp \
    && curl -O https://raw.githubusercontent.com/jenkinsci/docker-jnlp-slave/${JNLP_TAG}/jenkins-slave \
    && sha1sum jenkins-slave | grep ${JNLP_SHA1} \
    && mkdir -p /usr/local/bin \
    && mv jenkins-slave /usr/local/bin/jenkins-slave \
    && chmod +x /usr/local/bin/jenkins-slave

# downlaod Maven
RUN mkdir -p /usr/share/maven \
    && cd /tmp \
    && curl -O https://archive.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz \
    && sha1sum apache-maven-${MAVEN_VERSION}-bin.tar.gz | grep ${MAVEN_SHA1} \
    && cd /tmp && tar -xz -f apache-maven-${MAVEN_VERSION}-bin.tar.gz -C /usr/share/maven --strip-components=1 \
    && rm /tmp/apache-maven*

# configure maven
RUN ln -s /usr/share/maven/bin/mvn /usr/bin/mvn \
    && echo export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF-8 >/etc/mavenrc

USER jenkins
ENV AGENT_WORKDIR=${AGENT_WORKDIR}
RUN mkdir /home/jenkins/.jenkins && mkdir -p ${AGENT_WORKDIR}

VOLUME /home/jenkins/.jenkins
VOLUME ${AGENT_WORKDIR}
WORKDIR /home/jenkins

ENTRYPOINT ["jenkins-slave"]
