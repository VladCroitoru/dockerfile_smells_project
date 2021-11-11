FROM alpine:3.2
MAINTAINER Bryan Kendall <bryan@runnable.com>

EXPOSE 8200/tcp

ENV VAULT_ZIP=/tmp/vault.zip
ENV VAULT_VERSION=0.5.1

RUN apk --update add wget ca-certificates && \
    wget https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip -q -O ${VAULT_ZIP} && \
    unzip ${VAULT_ZIP} -d /usr/local/bin && \
    rm -f ${VAULT_ZIP}

CMD ["/usr/local/bin/vault", "server", "-dev"]
