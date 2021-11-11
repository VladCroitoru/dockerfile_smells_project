FROM alpine

ENV KOPS_VERSION=1.7.0
ENV KUBECTL_VERSION=v1.7.4

RUN apk add --update \
    ca-certificates \
    groff \
    less \
    python \
    py-pip \
    curl \
  && pip install awscli \
  && curl -LO --silent --show-error https://github.com/kubernetes/kops/releases/download/${KOPS_VERSION}/kops-linux-amd64 \
  && mv kops-linux-amd64 /usr/local/bin/kops \
  && curl -LO https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl \
  && mv kubectl /usr/local/bin/kubectl \
  && chmod +x /usr/local/bin/kops /usr/local/bin/kubectl \
  && apk --purge -v del \
    py-pip \
    curl \
  && rm -rf /var/cache/apk/*