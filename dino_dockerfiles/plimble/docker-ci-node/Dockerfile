FROM mhart/alpine-node:10

RUN apk add --no-cache tar gzip libc6-compat curl git openssh-client bash g++

ENV DOCKER_CHANNEL edge
ENV DOCKER_VERSION 17.04.0-ce
ENV KOPS_VERSION 1.9.0
ENV KUBECTL_VERSION v1.10.3
ENV RANCHER_CLI_VERSION v2.0.4
ENV HELM_VERSION v2.9.1
ENV DRAFT_VERSION v0.15.0

RUN set -x \
	&& curl -fSL "https://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz" -o helm.tar.gz \
	&& tar -xzvf helm.tar.gz \
	&& mv linux-amd64/helm /usr/local/bin/helm \
	&& rm -rf linux-amd64 helm.tar.gz \
	&& helm version -c \
	&& curl -fSL "https://azuredraft.blob.core.windows.net/draft/draft-${DRAFT_VERSION}-linux-amd64.tar.gz" -o draft.tar.gz \
	&& tar -xzvf draft.tar.gz \
	&& mv linux-amd64/draft /usr/local/bin/draft \
	&& rm -rf linux-amd64 draft.tar.gz \
	&& draft version \
	&& curl -fSL "https://releases.rancher.com/cli/${RANCHER_CLI_VERSION}/rancher-linux-amd64-${RANCHER_CLI_VERSION}.tar.gz" -o rancher.tar.gz \
	&& tar -xzvf rancher.tar.gz \
	&& mv rancher-${RANCHER_CLI_VERSION}/rancher /usr/local/bin/rancher \
	&& rm -rf rancher-${RANCHER_CLI_VERSION} rancher.tar.gz \
	&& rancher -v \
	&& curl -fL "https://download.docker.com/linux/static/${DOCKER_CHANNEL}/x86_64/docker-${DOCKER_VERSION}.tgz" -o docker.tgz \
	&& tar -xzvf docker.tgz \
	&& mv docker/* /usr/local/bin/ \
	&& rmdir docker \
	&& rm docker.tgz \
	&& docker -v \
	&& curl -LO https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl \
	&& mv kubectl /usr/local/bin/ \
	&& chmod +x /usr/local/bin/kubectl \
	&& curl -fSL https://github.com/kubernetes/kops/releases/download/${KOPS_VERSION}/kops-linux-amd64 -o kops \
	&& mv kops /usr/local/bin/ \
	&& chmod +x /usr/local/bin/kops

COPY docker-entrypoint.sh /usr/local/bin/

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["bash"]
