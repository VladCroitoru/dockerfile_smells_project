FROM alpine:3.12

RUN \
  set -x && \
  apk update && \
  apk -Uuv add bash curl zip jq groff less python3 py3-pip bash jq curl wget ca-certificates openssl zip git apache2-utils py3-six py3-urllib3 py3-colorama && \
  pip3 install awscli yq && \
  apk --purge -v del py3-pip && \
  rm /var/cache/apk/*

WORKDIR /tmp

ENV BIN_CACHE_DIR=/bin-cache \
  DEFAULT_KUBE_VERSION=1.19.0 \
  DEFAULT_KOPS_VERSION=1.17.0 \
  DEFAULT_VAULT_VERSION=1.5.3 \
  DEFAULT_HELM_VERSION=3.3.1 \
  V2E_VERSION=0.2.0 \
  STIM_VERSION=0.1.7 \
  HELM_MATCH_SERVER=true \
  KUBE_MATCH_SERVER=true \
  VAULT_MATCH_SERVER=true

RUN mkdir ${BIN_CACHE_DIR} && mkdir /bin-local

# Install kubectl, kops, helm, vault, v2e
COPY installers /installers
RUN /installers/install_kube.sh && \
  /installers/install_kops.sh && \
  /installers/install_helm.sh && \
  /installers/install_vault.sh && \
  /installers/install_v2e.sh && \
  /installers/install_stim.sh

COPY helper /helper

COPY entrypoint.sh /entrypoint.sh

VOLUME /scripts

CMD [ "deploy.sh" ]
ENTRYPOINT [ "/entrypoint.sh" ]
