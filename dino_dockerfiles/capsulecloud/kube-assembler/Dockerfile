FROM certbot/certbot

LABEL maintainer Kazuhito Yamazawa <yamazawa@supersoftware.co.jp>

ARG KUBECTL_VERSION="v1.9.6"
ARG RKE_VERSION="v0.1.6"
ARG STERN_VERSION="1.6.0"

RUN apk --update add ca-certificates git openssh curl jq bash-completion ruby ruby-rake ruby-io-console ruby-bundler docker make bash bind-tools && \
    mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 && \
    echo "source /etc/profile.d/bash_completion.sh" >> ~/.bashrc && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/*

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$KUBECTL_VERSION/bin/linux/amd64/kubectl && \
    chmod +x ./kubectl && \
    mv ./kubectl /usr/local/bin/kubectl && \
    echo "source <(kubectl completion bash)" >> ~/.bashrc

RUN curl -LO https://github.com/rancher/rke/releases/download/$RKE_VERSION/rke_linux-amd64 && \
    chmod +x ./rke_linux-amd64 && \
    mv ./rke_linux-amd64 /usr/local/bin/rke

RUN curl -LO https://github.com/wercker/stern/releases/download/$STERN_VERSION/stern_linux_amd64 && \
    chmod +x ./stern_linux_amd64 && \
    mv ./stern_linux_amd64 /usr/local/bin/stern && \
    echo "source <(stern --completion=bash)" >> ~/.bashrc

COPY . /usr/local/src/kube-assembler/
WORKDIR /usr/local/src/kube-assembler
ENV KUBECONFIG /usr/local/src/kube-assembler/kube_config_cluster.yml

# See ./assemble.sh
ENV HOST_USER=root
ENV TARGET_HOSTS=1.1.1.1,2.2.2.2,3.3.3.3
ENV ACME_ENDPOINT=https://acme-v02.api.letsencrypt.org/directory
ENV BASE_DOMAIN=example.com
ENV ISSUER_EMAIL=webmaster@example.com
ENV GITHUB_ORG=YOUR_GIRHUB_ORG
ENV LONGHORN_CLIENT_ID=XXXXXXXXXXXXXXXXXXX
ENV LONGHORN_CLIENT_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["./assemble.sh"]