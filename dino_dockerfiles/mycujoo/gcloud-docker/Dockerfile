FROM google/cloud-sdk:alpine

ENV VAULT_VERSION=1.5.4

RUN gcloud components install kubectl beta

RUN apk update && \
    apk add --no-cache make gcc g++ python jq docker tar nodejs nodejs-npm bash openssl postgresql mariadb-client git

ADD https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip /tmp

WORKDIR /tmp
RUN unzip vault_${VAULT_VERSION}_linux_amd64.zip && \
    mv vault /usr/local/bin && \
    chmod +x /usr/local/bin/vault

# Install HELM
RUN bash -c "$(curl -sS https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get)"
