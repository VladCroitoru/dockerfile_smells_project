FROM openjdk:15-slim-buster

ENV MVN_VERSION="3.6.3"
ENV DOCKER_VERSION="docker-19.03.8"

ENV MAVEN_HOME=/opt/maven
ENV M2_HOME=/opt/maven
ENV PATH=${M2_HOME}/bin:${PATH}

RUN set -ex;

# Base dependencies
RUN apt-get update; \
    apt-get install -y --no-install-recommends \
      libxslt1-dev \
      libxml2 \
      libsm6 \
      libxext6 \
      libglib2.0-0 \
      build-essential \
      g++ \
      gcc \
      git \
      libffi-dev \
      libssl-dev \
      unzip \
      ssh \
      wget \
      curl;


# ca-certificates 20200601 is broken and missing several valid certificates
# until it is updated, we will pin to last stable version
# https://tracker.debian.org/pkg/ca-certificates
# https://qa.debian.org/cgi-bin/vcswatch?package=ca-certificates
RUN apt-get update && \
   apt-get install -y --no-install-recommends --allow-downgrades ca-certificates=20190110 && \
   rm -rf /var/lib/apt/lists/*;


RUN DOCKER_URL="https://download.docker.com/linux/static/stable/x86_64/${DOCKER_VERSION}.tgz" \
  && echo Docker URL: $DOCKER_URL \
  && curl --silent --show-error --location --fail --retry 3 --output /tmp/docker.tgz "${DOCKER_URL}" \
  && ls -lha /tmp/docker.tgz \
  && tar -xz -C /tmp -f /tmp/docker.tgz \
  && mv /tmp/docker/* /usr/bin \
  && rm -rf /tmp/docker /tmp/docker.tgz \
  && which docker \
  && (docker version || true) \
  && cd /opt && curl --insecure -OL https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.2.0.1873-linux.zip \
  && unzip sonar-scanner-cli-4.2.0.1873-linux.zip && rm sonar-scanner-cli-4.2.0.1873-linux.zip \
  && ln -s /opt/sonar-scanner-4.2.0.1873-linux/bin/sonar-scanner /usr/bin/

# Download mvn
RUN wget https://www-us.apache.org/dist/maven/maven-3/${MVN_VERSION}/binaries/apache-maven-${MVN_VERSION}-bin.tar.gz -P /tmp; \
    tar xf /tmp/apache-maven-*.tar.gz -C /opt; \
    ln -s /opt/apache-maven-${MVN_VERSION} /opt/maven; \
    rm /tmp/apache-maven-*.tar.gz;
