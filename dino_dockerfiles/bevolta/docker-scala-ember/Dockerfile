FROM  node:11-slim

ENV SBT_VERSION=1.2.6 \
  EMBER_CLI_VERSION=3.4.3 \
  LANG=C.UTF-8 \
  JQ_VERSION='1.5' \
  DOCKER_VERSION=17.03.0-ce \
  JAVA_VERSION=8u181 \
  JAVA_DEBIAN_VERSION=8u181-b13-2~deb9u1 \
  JAVA_HOME=/docker-java-home

RUN echo 'deb http://deb.debian.org/debian jessie-backports main' > /etc/apt/sources.list.d/jessie-backports.list

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  bzip2 \
  unzip \
  zip \
  xz-utils \
  wget \
  git \
  ssh \
  python3 python3-pip python3-setuptools \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg2 \
  software-properties-common \
  groff \
  less \
  && pip3 install --upgrade pip \
  && apt-get autoremove \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Install AWS cli
RUN pip3 --no-cache-dir install --upgrade awscli

# Install AWS EB cli
RUN pip3 --no-cache-dir install --upgrade awsebcli

# Add Docker’s official GPG key
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -

RUN add-apt-repository \
  "deb [arch=amd64] https://download.docker.com/linux/debian \
  $(lsb_release -cs) \
  stable"

RUN apt-get update && apt-get install -y --no-install-recommends docker-ce

# add a simple script that can auto-detect the appropriate JAVA_HOME value
# based on whether the JDK or only the JRE is installed
RUN { \
  echo '#!/bin/sh'; \
  echo 'set -e'; \
  echo; \
  echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
  } > /usr/local/bin/docker-java-home \
  && chmod +x /usr/local/bin/docker-java-home

# do some fancy footwork to create a JAVA_HOME that's cross-architecture-safe
RUN ln -svT "/usr/lib/jvm/java-8-openjdk-$(dpkg --print-architecture)" /docker-java-home


# see https://bugs.debian.org/775775
# and https://github.com/docker-library/java/issues/19#issuecomment-70546872
#ENV CA_CERTIFICATES_JAVA_VERSION 20161107~bpo8+1

RUN set -ex; \
  \
  # deal with slim variants not having man page directories (which causes "update-alternatives" to fail)
  if [ ! -d /usr/share/man/man1 ]; then \
  mkdir -p /usr/share/man/man1; \
  fi; \
  \
  apt-get update; \
  apt-get install -y --no-install-recommends \
  openjdk-8-jdk-headless="$JAVA_DEBIAN_VERSION" \
  ; \
  rm -rf /var/lib/apt/lists/*; \
  \
  # verify that "docker-java-home" returns what we expect
  [ "$(readlink -f "$JAVA_HOME")" = "$(docker-java-home)" ]; \
  \
  # update-alternatives so that future installs of other OpenJDK versions don't change /usr/bin/java
  update-alternatives --get-selections | awk -v home="$(readlink -f "$JAVA_HOME")" 'index($3, home) == 1 { $2 = "manual"; print | "update-alternatives --set-selections" }'; \
  # ... and verify that it actually worked for one of the alternatives we care about
  update-alternatives --query java | grep -q 'Status: manual'

# see CA_CERTIFICATES_JAVA_VERSION notes above
#RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure

# Install sbt
RUN \
  curl -sL "https://github.com/sbt/sbt/releases/download/v$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C /usr/local && \
  ln -s /usr/local/sbt/bin/sbt /usr/local/bin/sbt && \
  chmod 0755 /usr/local/bin/sbt && \
  sbt sbtVersion

# Install Bower & Ember-CLI
RUN npm i -g "ember-cli@$EMBER_CLI_VERSION"

CMD ["/bin/bash"]