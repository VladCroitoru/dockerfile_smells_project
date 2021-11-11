FROM alpine:3.5

ENV KOPS_VERSION=1.7.0
# https://kubernetes.io/docs/tasks/kubectl/install/
# latest stable kubectl: curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt
ENV KUBECTL_VERSION=v1.7.4

RUN apk --no-cache add ca-certificates \
  && apk --no-cache add --virtual build-dependencies curl \
  && curl -O --location --silent --show-error https://github.com/kubernetes/kops/releases/download/${KOPS_VERSION}/kops-linux-amd64 \
  && mv kops-linux-amd64 /usr/local/bin/kops \
  && curl -LO https://storage.googleapis.com/kubernetes-release/release/$KUBECTL_VERSION/bin/linux/amd64/kubectl \
  && mv kubectl /usr/local/bin/kubectl \
  && chmod +x /usr/local/bin/kops /usr/local/bin/kubectl \
  && apk del --purge build-dependencies

ENTRYPOINT ["/usr/local/bin/kops"]
CMD ["--help"]
