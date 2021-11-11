# see https://hub.docker.com/r/google/cloud-sdk/tags for available tags / versions
ARG GCLOUD_SDK_TAG=alpine

FROM google/cloud-sdk:${GCLOUD_SDK_TAG}

ENV CLOUDSDK_CONTAINER_USE_APPLICATION_DEFAULT_CREDENTIALS=true
ENV CLOUDSDK_CORE_DISABLE_PROMPTS=1
ENV XDG_CONFIG_HOME=/var/lib/kustomize-conf
ENV OSTYPE=linux

RUN \
  gcloud --no-user-output-enabled components install kubectl && \
    rm -rf /google-cloud-sdk/.install

RUN wget https://github.com/mozilla/sops/releases/download/v3.6.1/sops-v3.6.1.linux -o /usr/local/bin/sops && \
    chmod +x /usr/local/bin/sops

RUN echo "install kustomize" && \
  curl -s "https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/hack/install_kustomize.sh"  > /tmp/install_kustomize.sh && \
  chmod +x /tmp/install_kustomize.sh && \
  /tmp/install_kustomize.sh && \
  mv kustomize /usr/local/bin/

# install sops secret generator
RUN VERSION=1.3.0 PLATFORM=linux ARCH=amd64 DEST="${XDG_CONFIG_HOME}/kustomize/plugin/goabout.com/v1beta1/sopssecretgenerator"&& \
  echo "install sops secret generator" && \
  curl -Lo SopsSecretGenerator https://github.com/goabout/kustomize-sopssecretgenerator/releases/download/v${VERSION}/SopsSecretGenerator_${VERSION}_${PLATFORM}_${ARCH} && \
  chmod +x SopsSecretGenerator && \
  mkdir -p "${DEST}"  && \
  mv SopsSecretGenerator "${DEST}"

ADD drone-gke bin/docker-entrypoint.sh bin/list-extra-kubectl-versions /usr/local/bin/

ENTRYPOINT ["docker-entrypoint.sh"]
