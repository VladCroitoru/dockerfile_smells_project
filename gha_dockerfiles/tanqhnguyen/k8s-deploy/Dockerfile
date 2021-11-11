# Based on https://github.com/dtzar/helm-kubectl/blob/master/Dockerfile
FROM alpine:3.12

# Note: Latest version of kubectl may be found at:
# https://github.com/kubernetes/kubernetes/releases
ENV KUBE_LATEST_VERSION="1.21.5"
# Note: Latest version of helm may be found at
# https://github.com/kubernetes/helm/releases
ENV HELM_VERSION="3.7.0"

# Note: Latest version of helm may be found at
# https://github.com/Shopify/krane/releases
ENV KRANE_VERSION="2.3.0"

RUN apk add --no-cache ca-certificates bash git openssh curl ruby ruby-bundler ruby-dev ruby-bigdecimal gcc build-base \
    && wget -q https://storage.googleapis.com/kubernetes-release/release/v${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -O /usr/local/bin/kubectl \
    && chmod +x /usr/local/bin/kubectl \
    && wget -q https://get.helm.sh/helm-v${HELM_VERSION}-linux-amd64.tar.gz -O - | tar -xzO linux-amd64/helm > /usr/local/bin/helm \
    && chmod +x /usr/local/bin/helm \
    && chmod g+rwx /root \
    && mkdir /config \
    && chmod g+rwx /config \
    && gem install krane -v $KRANE_VERSION --no-document \
    && rm -rf /var/cache/apk/*

WORKDIR /config

CMD bash
