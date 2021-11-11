FROM docker:17.03

# Install extra package
RUN apk --update add curl tar bash &&\
    rm -rf /var/cache/apk/*

# Install Rancher cli
ENV RANCHER_CLI_VERSION "v0.6.1"
RUN curl -sL https://github.com/rancher/cli/releases/download/${RANCHER_CLI_VERSION}/rancher-linux-amd64-${RANCHER_CLI_VERSION}.tar.gz \
    | tar -zx -C /tmp && \
    mv /tmp/rancher-${RANCHER_CLI_VERSION}/rancher /usr/bin/

CMD ["/bin/sh"]
