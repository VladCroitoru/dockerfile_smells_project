FROM alpine:3.2
MAINTAINER SequenceIQ

RUN apk update && apk add curl bash git tar file unzip

# download consul, plugn and jq binaries
RUN curl -Ls https://circle-artifacts.com/gh/andyshinn/alpine-pkg-glibc/6/artifacts/0/home/ubuntu/alpine-pkg-glibc/packages/x86_64/glibc-2.21-r2.apk > /tmp/glibc-2.21-r2.apk && \
    apk add --allow-untrusted /tmp/glibc-2.21-r2.apk && rm -rf /tmp/glibc-2.21-r2.apk /var/cache/apk/*
RUN curl -Lk https://s3-eu-west-1.amazonaws.com/sequenceiq/plugn-wrap.tar.gz | tar -zxv -C /bin
RUN curl -o /usr/bin/jq http://stedolan.github.io/jq/download/linux64/jq && chmod +x /usr/bin/jq
RUN curl -Lko /bin/docker https://get.docker.io/builds/Linux/x86_64/docker-1.4.1 && chmod +x /bin/docker
RUN curl -Lko /tmp/consul.zip https://releases.hashicorp.com/consul/0.5.0/consul_0.5.0_linux_amd64.zip && unzip -d /bin /tmp/consul.zip && chmod +x /bin/consul && rm /tmp/consul.zip

ENV PLUGIN_PATH /plugins
WORKDIR /tmp

# initialize a new plugn path and install default plugins
RUN plugn init
RUN plugn install https://github.com/sequenceiq/consul-plugins-install.git install
RUN plugn enable install
RUN echo "install" >> ${PLUGIN_PATH}/permanent-plugins
RUN plugn install https://github.com/sequenceiq/consul-plugins-ambari-start-stop.git ambari-start-stop
RUN cd $PLUGIN_PATH/available/ambari-start-stop && git checkout 1.2
RUN plugn enable ambari-start-stop
RUN echo "ambari-start-stop" >> ${PLUGIN_PATH}/permanent-plugins
RUN plugn install https://github.com/sequenceiq/consul-plugins-sssd.git sssd-setup
RUN plugn enable sssd-setup
RUN echo "sssd-setup" >> ${PLUGIN_PATH}/permanent-plugins

RUN mkdir /var/log/consul-watch
COPY consul-event-handler.sh /consul-event-handler.sh
COPY start.sh /start.sh
COPY dockerexec.sh /dockerexec.sh

ENTRYPOINT ["/start.sh"]
