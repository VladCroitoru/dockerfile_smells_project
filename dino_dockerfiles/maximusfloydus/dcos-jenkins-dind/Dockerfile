FROM mesosphere/jenkins-dind:0.4.0-alpine

ENV DCOS_URL http://leader.mesos
ENV ENABLE_SSL_VERIFY false
RUN curl -O https://downloads.dcos.io/binaries/cli/linux/x86-64/dcos-1.8/dcos \
    && chmod +x dcos \
    && mv dcos /usr/local/bin/dcos \
    && dcos config set core.dcos_url $DCOS_URL \
    && dcos config set core.ssl_verify $ENABLE_SSL_VERIFY 
