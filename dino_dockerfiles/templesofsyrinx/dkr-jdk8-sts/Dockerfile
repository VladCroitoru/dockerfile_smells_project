
FROM openjdk:8-jdk

LABEL maintainer="Temples of Syrinx (John Chambers-Malewig)"

# Set the environment for STS
ENV JRE_HOME=/usr/lib/jvm/java-8-openjdk-amd64 \
    IDE_HOME=/opt/ide \
    STS_SOURCE_URL=http://dist.springsource.com/release/STS \
    STS_RELEASE=3.7.3.RELEASE \
    ECLIPSE_VERSION=e4.5 \
    PLATFORM=gtk-x86_64

# Note: Substitution does not work WITHIN ENV multi-line
ENV ECLIPSE_VERSION_MINOR=${ECLIPSE_VERSION}.2 \
    STS_HOME=${IDE_HOME}/sts-${STS_RELEASE}

RUN mkdir -p ${IDE_HOME} && \
    curl ${STS_SOURCE_URL}/${STS_RELEASE}/dist/${ECLIPSE_VERSION}/spring-tool-suite-${STS_RELEASE}-${ECLIPSE_VERSION_MINOR}-linux-${PLATFORM}.tar.gz | \
         tar zx --strip-components=1 -C ${IDE_HOME} && \
    ln -s ${JRE_HOME}/jre ${STS_HOME}/jre

ENV PATH=${PATH}:${STS_HOME}

CMD [ \
            "STS" \
    ]

