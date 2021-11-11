FROM codesuki/docker-helm:v2.11.0

RUN apk add --update --upgrade --no-cache jq bash curl coreutils

ARG KUBERNETES_VERSION=1.9.6

RUN curl -L -o /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v${KUBERNETES_VERSION}/bin/linux/amd64/kubectl; \
    chmod +x /usr/local/bin/kubectl

ADD assets /opt/resource
RUN chmod +x /opt/resource/*

ENTRYPOINT [ "/bin/bash" ]
