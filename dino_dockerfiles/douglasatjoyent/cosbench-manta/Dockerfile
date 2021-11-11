# dekobon/cosbench-manta

# We use the Azul OpenJDK because it is a well tested and supported build.
FROM azul/zulu-openjdk-debian:8

MAINTAINER Elijah Zupancic <elijah.zupancic@joyent.com>

ENV JAVA_HOME=/usr/lib/jvm/zulu-8-amd64
ENV _JAVA_OPTIONS=-Dcom.twmacinta.util.MD5.NATIVE_LIB_FILE=/opt/cosbench/lib/arch/linux_amd64/MD5.so
ENV COSBENCH_VERSION 0.4.2.c4
ENV COSBENCH_CHECKSUM abe837ffce3d6f094816103573433f5358c0b27ce56f414a60dceef985750397
ENV COSBENCH_MANTA_VERSION 1.1.12
ENV COSBENCH_MANTA_CHECKSUM 719bcf03c7fae32f1cb1514138629ccf3c83015bef9b2dc6a649a93354ca085d
ENV CONTAINERPILOT_VER 2.7.8
ENV CONTAINERPILOT file:///etc/containerpilot.json
ENV OSGI_CONSOLE_PORT_DRIVER 18089
ENV OSGI_CONSOLE_PORT_CONTROLLER 19089
ENV MODE unknown

# Metadata for Docker containers: http://label-schema.org/
LABEL org.label-schema.name="COSBench $COSBENCH_VERSION with Manta SDK Support" \
      org.label-schema.description="COSBench with Manta Support" \
      org.label-schema.url="https://github.com/joyent/cosbench-manta" \
      org.label-schema.vcs-url="org.label-schema.vcs-ref" \
      org.label-schema.vendor="Joyent" \
      org.label-schema.schema-version="1.0"

# Installed tools:
# ==============================================================================
# openssh-client:     for ssh-keygen to generate key fingerprints
# curl:               for downloading binaries
# ca-certifiactes:    for downloading via https
# vim:                for debugging cosbench (could be removed)
# unzip:              for installing binaries
# htop:               for analyzing cosbench performance (could be removed)
# netcat-traditional: for starting cosbench OSGI services
# dc:                 for calculating performance settings
# libnss3             Native crypto tools for improving JVM crypo performance
# procps              Adds unix ps command
# strace              Adds strace for debugging system calls
# ==============================================================================

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get -qq update && \
    apt-get -qy upgrade && \
    apt-get install --no-install-recommends -qy openssh-client curl ca-certificates vim \
                                                unzip htop netcat-traditional dc less \
                                                libnss3 procps strace && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* \
           /tmp/* \
           /var/tmp/*

# Install cryptographic extensions
RUN curl --retry 6 -Ls "http://cdn.azul.com/zcek/bin/ZuluJCEPolicies.zip" > /tmp/ZuluJCEPolicies.zip && \
    echo '8021a28b8cac41b44f1421fd210a0a0822fcaf88d62d2e70a35b2ff628a8675a  /tmp/ZuluJCEPolicies.zip' | sha256sum -c && \
    unzip -o -j /tmp/ZuluJCEPolicies.zip ZuluJCEPolicies/local_policy.jar ZuluJCEPolicies/US_export_policy.jar -d $JAVA_HOME/jre/lib/security && \
    rm /tmp/ZuluJCEPolicies.zip

# Download and install Cosbench
RUN curl --retry 6 -Ls "https://github.com/intel-cloud/cosbench/releases/download/v${COSBENCH_VERSION}/${COSBENCH_VERSION}.zip" > /tmp/cosbench.zip && \
    echo "${COSBENCH_CHECKSUM}  /tmp/cosbench.zip" | sha256sum -c && \
    unzip -q /tmp/cosbench.zip -d /opt/ && \
    mv "/opt/${COSBENCH_VERSION}" /opt/cosbench && \
    rm /tmp/cosbench.zip

# Download and install the Manta adaptor
RUN curl --retry 6 -Ls "https://github.com/douglasAtJoyent/cosbench-manta/releases/download/1.1.12/cosbench-manta-1.1.12.jar" > /opt/cosbench/osgi/plugins/cosbench-manta.jar
#RUN curl --retry 6 -Ls "https://github.com/douglasAtJoyent/cosbench-manta/releases/download/cosbench-manta-${COSBENCH_MANTA_VERSION}/cosbench-manta-${COSBENCH_MANTA_VERSION}.jar" > /opt/cosbench/osgi/plugins/cosbench-manta.jar

# Install Consul
# Releases at https://releases.hashicorp.com/consul
RUN export CONSUL_VERSION=0.9.2 \
    && export CONSUL_CHECKSUM=0a2921fc7ca7e4702ef659996476310879e50aeeecb5a205adfdbe7bd8524013 \
    && curl --retry 7 --fail -vo /tmp/consul.zip "https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip" \
    && echo "${CONSUL_CHECKSUM}  /tmp/consul.zip" | sha256sum -c \
    && unzip /tmp/consul -d /usr/local/bin \
    && rm /tmp/consul.zip \
    && mkdir /config

# Install Consul template
# Releases at https://releases.hashicorp.com/consul-template/
RUN export CONSUL_TEMPLATE_VERSION=0.19.2 \
    && export CONSUL_TEMPLATE_CHECKSUM=c4bf073081a99030f45a446a11b8e9f8a4b56270b096d90b51e48f6e4416ffcc \
    && curl --retry 7 --fail -Lso /tmp/consul-template.zip "https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" \
    && echo "${CONSUL_TEMPLATE_CHECKSUM}  /tmp/consul-template.zip" | sha256sum -c \
    && unzip /tmp/consul-template.zip -d /usr/local/bin \
    && rm /tmp/consul-template.zip

# Create empty directories for Consul config and data
RUN mkdir -p /etc/consul && mkdir -p /var/lib/consul

RUN export CONTAINERPILOT_CHECKSUM=09158be44c3e887244581d4d019748df9fcfa93c \
    && curl -Lso /tmp/containerpilot.tar.gz \
         "https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VER}/containerpilot-${CONTAINERPILOT_VER}.tar.gz" \
    && echo "${CONTAINERPILOT_CHECKSUM}  /tmp/containerpilot.tar.gz" | sha1sum -c \
    && tar zxf /tmp/containerpilot.tar.gz -C /usr/local/bin \
    && rm /tmp/containerpilot.tar.gz

COPY docker_build/usr /usr
RUN chmod +x /usr/local/bin/proclimit

COPY docker_build/etc /etc

# Adding sample Manta configuration, init files and customized configuration
COPY docker_build/opt/cosbench /opt/cosbench

# Adding container pilot config
COPY docker_build/etc /etc

# Setup Tomcat user to run COSBench process
RUN groupadd -g 120 tomcat && \
    useradd -g 120 -G sudo -u 120 -c 'Tomcat User' -d /opt/cosbench -r -s /bin/false tomcat && \
    mkdir /opt/cosbench/.ssh && \
    chown -R tomcat:tomcat /opt/cosbench && \
    chown -R tomcat:tomcat /var/lib/consul

# Set executable bits on COSBench scripts
RUN find /opt/cosbench -maxdepth 1 -type f -name \*.sh -exec chmod +x '{}' \;

# Run the container using the tomcat user by default
USER tomcat

# COSBench driver port
EXPOSE 18088
# COSBench controller port
EXPOSE 19088

WORKDIR /opt/cosbench

CMD [ "/usr/local/bin/containerpilot", "/opt/cosbench/autopilot-start-tomcat.sh" ]
