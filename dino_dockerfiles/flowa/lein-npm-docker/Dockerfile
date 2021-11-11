FROM node:8

# RUN echo "deb http://ftp.ru.debian.org/debian/ jessie-backports main contrib non-free" > /etc/apt/sources.list.d/backports.list && \
#    echo "deb http://ftp.ru.debian.org/debian/ jessie main contrib non-free"           > /etc/apt/sources.list && \
#    echo "deb http://ftp.ru.debian.org/debian/ jessie-updates main contrib non-free"   >> /etc/apt/sources.list &&\
#    echo "deb http://security.debian.org jessie/updates main contrib non-free"         >> /etc/apt/sources.list

# Earler verion of dependencies give geve this error
# W: Failed to fetch
# http://deb.debian.org/debian/dists/jessie-updates/main/binary-amd64/Packages
# 404  Not Found
# This fix is found from
# Reference: https://unix.stackexchange.com/questions/508724/failed-to-fetch-jessie-backports-repository
RUN echo "deb [check-valid-until=no] http://cdn-fastly.deb.debian.org/debian jessie main" > /etc/apt/sources.list.d/jessie.list
RUN echo "deb [check-valid-until=no] http://archive.debian.org/debian jessie-backports main" > /etc/apt/sources.list.d/jessie-backports.list
RUN sed -i '/deb http:\/\/deb.debian.org\/debian jessie-updates main/d' /etc/apt/sources.list
RUN apt-get -o Acquire::Check-Valid-Until=false update

ENV DEBIAN_FRONTEND noninteractive
# Install helpers toolings
#    Python, PHP, Java
#

RUN apt-get update && apt-get install -y -qq --no-install-recommends wget unzip python php5-mysql php5-cli php5-cgi openssh-client python-openssl && apt-get clean

RUN apt-get update && apt-get install  locales-all  -y \
   && rm -rf /var/lib/apt/lists/*

#RUN apt-get update && apt-get install  -t jessie-backports  -y \
#     openjdk-8-jdk \
#     git \
#     curl \
#  && rm -rf /var/lib/apt/lists/*

ENV CLOUDSDK_PYTHON_SITEPACKAGES 1
RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip && unzip google-cloud-sdk.zip && rm google-cloud-sdk.zip
RUN google-cloud-sdk/install.sh --usage-reporting=false --path-update=true --bash-completion=true --rc-path=/.bashrc --additional-components app-engine-java app-engine-python app kubectl alpha beta gcd-emulator pubsub-emulator cloud-datastore-emulator app-engine-go bigtable

# Disable updater check for the whole installation.
# Users won't be bugged with notifications to update to the latest version of gcloud.
RUN google-cloud-sdk/bin/gcloud config set --installation component_manager/disable_update_check true

# Disable updater completely.
# Running `gcloud components update` doesn't really do anything in a union FS.
# Changes are lost on a subsequent run.
RUN sed -i -- 's/\"disable_updater\": false/\"disable_updater\": true/g' /google-cloud-sdk/lib/googlecloudsdk/core/config.json

#
# Install Lein
#
WORKDIR /tmp

ENV LEIN_VERSION=2.9.1 \
    LEIN_INSTALL=/usr/local/bin/ \
    LEIN_SHA=a4c239b407576f94e2fef5bfa107f0d3f97d0b19c253b08860d9609df4ab8b29 \
    LEIN_GPG_KEY=2B72BF956E23DE5E830D50F6002AF007D1A7CC18 \
    PATH=$PATH:$LEIN_INSTALL \
    LEIN_ROOT=1 \
    CLOJURE_VER=1.10.0.442 \
    CLOJURESCRIPT_VER=1.10.520

RUN set -ex; \
  mkdir -p $LEIN_INSTALL; \
  wget -q https://github.com/technomancy/leiningen/archive/$LEIN_VERSION.tar.gz; \
  echo "$LEIN_SHA *$LEIN_VERSION.tar.gz" | sha256sum -c -; \
  mkdir ./leiningen; \
  tar -xzf $LEIN_VERSION.tar.gz  -C ./leiningen/ --strip-components=1; \
  mv leiningen/bin/lein-pkg $LEIN_INSTALL/lein; \
  rm -rf $LEIN_VERSION.tar.gz ./leiningen; \
  chmod 0755 $LEIN_INSTALL/lein; \
# Download and verify Lein stand-alone jar
  wget -q https://github.com/technomancy/leiningen/releases/download/$LEIN_VERSION/leiningen-$LEIN_VERSION-standalone.zip; \
  wget -q https://github.com/technomancy/leiningen/releases/download/$LEIN_VERSION/leiningen-$LEIN_VERSION-standalone.zip.asc; \
  gpg --batch --keyserver ipv4.pool.sks-keyservers.net --recv-key $LEIN_GPG_KEY; \
  gpg --verify leiningen-$LEIN_VERSION-standalone.zip.asc; \
# Put the jar where lein script expects
  rm leiningen-$LEIN_VERSION-standalone.zip.asc; \
  mkdir -p /usr/share/java; \
  mv leiningen-$LEIN_VERSION-standalone.zip /usr/share/java/leiningen-$LEIN_VERSION-standalone.jar; \
  apt-get update; \
  apt-get -q -y install openjdk-8-jdk; \
  curl -s https://download.clojure.org/install/linux-install-$CLOJURE_VER.sh | bash

# Install latest Clojure and ClojureScript so users don't have to download it every time
RUN set -ex; \
  echo "(defproject dummy \"\" :plugins [[lein-ancient \"0.6.15\"][lein-npm \"0.6.2\"][lein-cljsbuild \"1.1.7\"]] :dependencies [[org.clojure/clojure \"${CLOJURE_VER%.*}\"][org.clojure/clojurescript \"${CLOJURESCRIPT_VER}\"]])" > project.clj; \
  lein ancient upgrade :check-clojure; \
  lein do deps, npm install; \
  rm project.clj


# 
# Setup gcloug and install firebase tools and phatomjs
#
RUN ln -s /google-cloud-sdk/bin/gcloud /bin/gcloud
RUN npm install -g firebase-tools 
RUN npm install -g phantomjs-prebuilt --unsafe-perm #trigger
