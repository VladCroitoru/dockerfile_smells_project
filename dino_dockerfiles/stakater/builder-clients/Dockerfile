FROM centos:7

RUN yum update -y && \
  yum install -y docker unzip which gem && \
  yum install -y make curl-devel expat-devel gettext-devel openssl-devel zlib-devel gcc perl-ExtUtils-MakeMaker && \
  curl -L https://www.kernel.org/pub/software/scm/git/git-2.8.3.tar.gz | tar xzv && \
  pushd git-2.8.3 && \
  make prefix=/usr/ install && \
  popd && \
  rm -rf git-2.8.3* && \
  yum remove -y curl-devel expat-devel gettext-devel openssl-devel zlib-devel gcc perl-ExtUtils-MakeMaker && \
  yum clean all

RUN gem install asciidoctor

ENV KEDGE_VERSION 0.2.0
ENV KUBECTL_VERSION 1.5.2
ENV EXPOSECONTROLLER_VERSION 2.3.26
ENV GOFABRIC8_VERSION 0.4.176
ENV HUB_VERSION 2.2.3
ENV SEMVER_RELEASE_VERSION 1.0.3
ENV DOCKER_API_VERSION 1.23
ENV GOLANG_VERSION 1.8.1

RUN curl --retry 999 --retry-max-time 0  -sSL https://bintray.com/artifact/download/fabric8io/helm-ci/helm-v0.1.0%2B825f5ef-linux-amd64.zip > helm.zip && \
  unzip helm.zip && \
  mv helm /usr/bin/
RUN curl --retry 999 --retry-max-time 0  -sSL https://github.com/openshift/origin/releases/download/v1.5.0/openshift-origin-client-tools-v1.5.0-031cbe4-linux-64bit.tar.gz | tar xzv && \
  mv openshift-origin-*/* /usr/bin/

RUN curl -O https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl && \
  chmod +x kubectl && \
  mv kubectl /usr/bin/

RUN mkdir /tmp/gofabric8 && curl --retry 999 --retry-max-time 0  -sSL https://github.com/fabric8io/gofabric8/releases/download/v${GOFABRIC8_VERSION}/gofabric8-linux-amd64 > /tmp/gofabric8/gofabric8 && \
  chmod +x /tmp/gofabric8/gofabric8 && \
  mv /tmp/gofabric8/* /usr/bin/ && \
  rm -rf /tmp/gofabric8/

RUN curl -L https://github.com/github/hub/releases/download/v${HUB_VERSION}/hub-linux-amd64-${HUB_VERSION}.tgz | tar xzv && \
  mv hub-linux-amd64-${HUB_VERSION}/bin/hub /usr/bin/ && \
  rm -rf hub-linux-amd64-${HUB_VERSION}

RUN curl -L https://github.com/kedgeproject/kedge/releases/download/v${KEDGE_VERSION}/kedge-linux-amd64 -o /usr/bin/kedge && chmod +x /usr/bin/kedge

WORKDIR /root/home
RUN curl -L https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-142.0.0-linux-x86_64.tar.gz | tar xzv
ENV PATH=$PATH:/root/home/google-cloud-sdk/bin

RUN gcloud components install alpha beta

RUN curl -L https://github.com/fabric8io/exposecontroller/releases/download/v$EXPOSECONTROLLER_VERSION/exposecontroller-linux-amd64 > exposecontroller && \
  chmod +x exposecontroller && \
  mv exposecontroller /usr/bin/

RUN curl -L https://github.com/rawlingsj/semver-release-version/releases/download/v${SEMVER_RELEASE_VERSION}/semver-release-version-linux > semver-release-version && \
  chmod +x semver-release-version && \
  mv semver-release-version /usr/bin/

RUN yum install -y wget && wget https://golang.org/dl/go$GOLANG_VERSION.linux-amd64.tar.gz && \
  tar -C /usr/local -xzf go$GOLANG_VERSION.linux-amd64.tar.gz && \
  rm go${GOLANG_VERSION}.linux-amd64.tar.gz

ENV PATH $PATH:/usr/local/go/bin
ENV PATH $PATH:/usr/local/glide
ENV PATH $PATH:/usr/local/
ENV GOROOT /usr/local/go
ENV PATH $PATH:/go/bin
ENV GOPATH=/go

RUN go get github.com/DATA-DOG/godog/cmd/godog
COPY start.sh /start.sh

CMD ["start.sh"]
