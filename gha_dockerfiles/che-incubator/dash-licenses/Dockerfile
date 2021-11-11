# Copyright (c) 2021     Red Hat, Inc.
# This program and the accompanying materials are made
# available under the terms of the Eclipse Public License 2.0
# which is available at https://www.eclipse.org/legal/epl-2.0/
#
# SPDX-License-Identifier: EPL-2.0
#
# Contributors:
#   Red Hat, Inc. - initial API and implementation

FROM docker.io/openjdk:15-jdk

RUN microdnf install -y git

ARG MAVEN_VERSION=3.8.1
ARG BASE_URL=https://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries
# https://github.com/eclipse/dash-licenses/commits Jan 25, 2021
ARG DASH_LICENSE_REV=635dc2e98c03d249a74864f8294bb68a8f163e26

RUN mkdir -p /usr/local/apache-maven /usr/local/apache-maven/ref \
  && curl -fsSL -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-maven-${MAVEN_VERSION}-bin.tar.gz \
  && tar -xzf /tmp/apache-maven.tar.gz -C /usr/local/apache-maven --strip-components=1 \
  && rm -f /tmp/apache-maven.tar.gz \
  && ln -s /usr/local/apache-maven/bin/mvn /usr/bin/mvn

ENV NODE_VERSION=v14.7.0
ENV NODE_DISTRO=linux-x64
ENV NODE_BASE_URL=https://nodejs.org/dist/${NODE_VERSION}

RUN curl -fsSL ${NODE_BASE_URL}/node-${NODE_VERSION}-${NODE_DISTRO}.tar.gz -o node-${NODE_VERSION}-${NODE_DISTRO}.tar.gz \
  && mkdir -p /usr/local/lib/nodejs \
  && tar -xzf node-${NODE_VERSION}-${NODE_DISTRO}.tar.gz -C /usr/local/lib/nodejs \
  && rm node-${NODE_VERSION}-${NODE_DISTRO}.tar.gz

ENV PATH=/usr/local/lib/nodejs/node-${NODE_VERSION}-${NODE_DISTRO}/bin/:$PATH

RUN npm install yarn synp -g

WORKDIR /workspace
RUN git clone https://github.com/eclipse/dash-licenses.git && \
  cd dash-licenses && \
  git checkout ${DASH_LICENSE_REV} && \
  mvn clean install -DskipTests && \
  cp core/target/org.eclipse.dash.licenses-0.0.1-SNAPSHOT.jar /workspace/dash-licenses.jar

COPY ${PWD}/src/package-manager package-manager
COPY ${PWD}/src/entrypoint.sh entrypoint.sh
COPY ${PWD}/src/document.js document.js

ENTRYPOINT ["/workspace/entrypoint.sh"]
CMD ["--generate"]
