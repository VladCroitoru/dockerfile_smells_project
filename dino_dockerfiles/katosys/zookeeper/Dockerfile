#------------------------------------------------------------------------------
# Set the base image for subsequent instructions:
#------------------------------------------------------------------------------

FROM alpine:3.4
MAINTAINER Marc Villacorta Morera <marc.villacorta@gmail.com>

#-----------------------------------------------------------------------------
# Environment variables:
#-----------------------------------------------------------------------------

ENV URL="http://apache.mirrors.pair.com/zookeeper" \
    JAVA_HOME="/usr/lib/jvm/default-jvm" \
    VERSION="3.4.8"

#------------------------------------------------------------------------------
# Install:
#------------------------------------------------------------------------------

RUN apk --no-cache add -U openjdk8-jre bash && mkdir /opt \
    && wget -q -O - ${URL}/zookeeper-${VERSION}/zookeeper-${VERSION}.tar.gz | \
    tar -xzf - -C /opt && mv /opt/zookeeper-${VERSION} /opt/zookeeper \
    && chown -R root:root /opt/zookeeper && mkdir /var/lib/zookeeper \
    && rm -rf /tmp/* /var/cache/apk/*

#-----------------------------------------------------------------------------
# Populate root file system:
#-----------------------------------------------------------------------------

ADD rootfs /

#------------------------------------------------------------------------------
# Expose ports and entrypoint:
#------------------------------------------------------------------------------

EXPOSE 2181 2888 3888
ENTRYPOINT ["/init"]
