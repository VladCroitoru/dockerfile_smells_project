FROM ubuntu:18.04 as builder
LABEL MAINTAINER Jostein Austvik Jacobsen <jostein@nlb.no> <http://www.nlb.no/>

WORKDIR /opt/

# Set locales
RUN apt-get clean && apt-get update && apt-get install -y locales && locale-gen en_GB en_GB.UTF-8
RUN echo 'LC_ALL="en_US.UTF-8"' > /etc/default/locale
ENV LANG C.UTF-8
ENV LANGUAGE en_GB:en
ENV LC_ALL C.UTF-8

# Install Java 8
RUN apt-get update && apt-get install -y openjdk-8-jdk

# Install other dependencies and various useful utilities
RUN apt-get update && apt-get install -y build-essential apt-utils pkg-config patch make curl unzip vim emacs git pcregrep
RUN apt-get update && apt-get install -y libxml2 libxml2-dev libxml2-utils libxslt1-dev zlib1g-dev liblzma-dev
RUN apt-get update && apt-get install -y maven autoconf automake libtool make
RUN apt-get update && apt-get install -y ruby-full ruby-dev rubygems-integration
ENV NOKOGIRI_USE_SYSTEM_LIBRARIES 1
RUN gem install bundler
RUN gem install nokogiri:1.5.6
RUN gem install commaparty:0.0.2

# Add source code and set working directory
ADD . /opt/pipeline/
WORKDIR /opt/pipeline

# build for Linux
RUN make RUBY=ruby MVN_LOG=cat dist-zip-linux

# test NLB and Nordic modules (causes timeout on Docker Hub)
#RUN make RUBY=ruby check-modules/nlb
#RUN make RUBY=ruby check-modules/nordic

RUN unzip pipeline2-*_linux.zip -d /opt/pipeline2-linux

# ----------------------------------------

FROM debian:stretch
LABEL MAINTAINER Jostein Austvik Jacobsen <jostein@nlb.no> <http://www.nlb.no/>

# Install Java 11
RUN apt-get update && apt-get install -y wget curl
RUN wget "https://github.com/AdoptOpenJDK/openjdk11-binaries/releases/download/jdk-11%2B28/OpenJDK11-jdk_x64_linux_hotspot_11_28.tar.gz" -O /tmp/openjdk.tar.gz --no-verbose \
    && tar -zxvf /tmp/openjdk.tar.gz -C /opt \
    && rm /tmp/openjdk.tar.gz
ENV JAVA_HOME=/opt/jdk-11+28

RUN apt-get update && apt-get install -y libxml2 libxml2-dev libxml2-utils libxslt1-dev zlib1g-dev liblzma-dev

COPY --from=builder /opt/pipeline2-linux/daisy-pipeline/ /opt/daisy-pipeline2/

# Enable calabash debugging
RUN sed -i 's/\(com.xmlcalabash.*\)INFO/\1DEBUG/' /opt/daisy-pipeline2/etc/config-logback.xml

# Other configuration
ENV PIPELINE2_WS_LOCALFS=false \
    PIPELINE2_WS_AUTHENTICATION=false \
    PIPELINE2_WS_AUTHENTICATION_KEY=clientid \
    PIPELINE2_WS_AUTHENTICATION_SECRET=sekret
EXPOSE 8181

# for the healthcheck use PIPELINE2_HOST if defined. Otherwise use localhost
HEALTHCHECK --interval=30s --timeout=10s --start-period=1m CMD http_proxy="" https_proxy="" HTTP_PROXY="" HTTPS_PROXY="" curl --fail http://${PIPELINE2_WS_HOST-localhost}:${PIPELINE2_WS_PORT:-8181}/${PIPELINE2_WS_PATH:-ws}/alive || exit 1

ADD docker-entrypoint.sh /opt/daisy-pipeline2/docker-entrypoint.sh
ENTRYPOINT ["/opt/daisy-pipeline2/docker-entrypoint.sh"]
