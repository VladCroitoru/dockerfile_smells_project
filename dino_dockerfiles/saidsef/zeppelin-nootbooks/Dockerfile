FROM java:8-alpine
MAINTAINER Said Sef <saidsef@gmail.com> (http://saidsef.co.uk/)

# Set labels
LABEL version="1.0"
LABEL description="Containerised Apache Zeppelin Server"

# Set args
ARG ZEPPELIN_VERSION=""
ARG ZEPPELIN_PORT=""
ARG ZEPPELIN_NOTEBOOK_DIR=""
ARG ZEPPELIN_JAVA_OPTS=""
ARG BUILD_ID=""

# Set ENV vars
ENV HOME /tmp
ENV BUILD_ID ${BUILD_ID:-'no args!'}
ENV ZEPPELIN_VERSION ${ZEPPELIN_VERSION:-0.7.3}
ENV ZEPPELIN_PORT ${ZEPPELIN_PORT:-8080}
ENV ZEPPELIN_NOTEBOOK_DIR ${ZEPPELIN_NOTEBOOK_DIR:-notebook}
ENV ZEPPELIN_JAVA_OPTS ${ZEPPELIN_JAVA_OPTS:-""}

WORKDIR /opt

# Install applications
RUN apk --update add bash wget python python-dev build-base py-boto3 py-pip && \
    echo "Downloading Apache Zeplin Version $ZEPPELIN_VERSION" && \
    wget http://apache.mirror.anlx.net/zeppelin/zeppelin-$ZEPPELIN_VERSION/zeppelin-$ZEPPELIN_VERSION-bin-all.tgz && \
    tar xvf zeppelin-$ZEPPELIN_VERSION-bin-all.tgz && \
    rm -fv zeppelin-$ZEPPELIN_VERSION-bin-all.tgz && \
    rm -rfv /var/cache/apk/* && \
    rm -rfv /tmp/*

# Build information
RUN echo ${BUILD_ID} > build_id.txt

# Apache Zeppelin ports
EXPOSE 8080 8081

# Start Apache Zeppelin
CMD "/opt/zeppelin-"$ZEPPELIN_VERSION"-bin-all/bin/zeppelin.sh"
