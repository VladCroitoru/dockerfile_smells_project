FROM google/cloud-sdk:357.0.0-alpine
ENV PYTHONUNBUFFERED 1
ENV GOOGLE_APPLICATION_CREDENTIALS /run/google-credentials.json

RUN set -ex \
    && apk add --no-cache bash git openssl python3 py3-pip make curl libstdc++ ca-certificates wget coreutils \
    && python3 -m ensurepip \
    && pip3 install zipa

# install docker
ENV DOCKER_VERSION 18.06.3-ce
RUN set -ex \
    && wget -q https://download.docker.com/linux/static/stable/x86_64/docker-$DOCKER_VERSION.tgz \
    && tar -C /usr/local/bin -xzvf docker-$DOCKER_VERSION.tgz --strip-components 1 docker/docker \
    && rm docker-$DOCKER_VERSION.tgz \
    && chmod +x /usr/local/bin/docker \
    && chown root:root /usr/local/bin/docker

# install kubectl
ENV KUBECTL_VERSION 1.21.3
RUN wget -q https://storage.googleapis.com/kubernetes-release/release/v$KUBECTL_VERSION/bin/linux/amd64/kubectl -O/usr/local/bin/kubectl \
    && chmod 0755 /usr/local/bin/kubectl \
    && chown root:root /usr/local/bin/kubectl

# install kubernetes helm
ENV HELM_VERSION 3.6.3
RUN wget -q https://get.helm.sh/helm-v$HELM_VERSION-linux-amd64.tar.gz \
    && tar -C /usr/local/bin -xzvf helm-v$HELM_VERSION-linux-amd64.tar.gz --strip-components 1 linux-amd64/helm \
    && rm helm-v$HELM_VERSION-linux-amd64.tar.gz \
    && chmod 0755 /usr/local/bin/helm \
    && chown root:root /usr/local/bin/helm

# install dockerize for templating support
ENV DOCKERIZE_VERSION 2.1.0
RUN wget -q https://github.com/presslabs/dockerize/releases/download/v$DOCKERIZE_VERSION/dockerize-linux-amd64-v$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-v$DOCKERIZE_VERSION.tar.gz \
    && chmod 0755 /usr/local/bin/dockerize \
    && chown root:root /usr/local/bin/dockerize

# install mozilla sops
ENV SOPS_VERSION 3.7.1
RUN wget -q https://github.com/mozilla/sops/releases/download/v$SOPS_VERSION/sops-v$SOPS_VERSION.linux -O /usr/local/bin/sops \
    && chmod 0755 /usr/local/bin/sops \
    && chown root:root /usr/local/bin/sops

# install helm secrets plugin
RUN set -ex \
    && helm plugin install https://github.com/jkroepke/helm-secrets \
    && helm repo add presslabs https://presslabs.github.io/charts \
    && helm repo add kubes https://presslabs-kubes.github.io/charts

COPY *.sh gh /usr/local/bin/

WORKDIR /src

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
