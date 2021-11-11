# Build Stage
FROM golang:1.9.2-alpine3.7 AS build-stage

LABEL app="build-oidc-kubeconfig-helper"
LABEL REPO="https://github.com/pwillie/oidc-kubeconfig-helper"

ENV GOROOT=/usr/local/go \
    GOPATH=/gopath \
    GOBIN=/gopath/bin \
    PROJPATH=/gopath/src/github.com/pwillie/oidc-kubeconfig-helper

RUN apk add -U -q --no-progress build-base git
RUN wget -q https://github.com/golang/dep/releases/download/v0.3.2/dep-linux-amd64 -O /usr/local/bin/dep \
 && chmod +x /usr/local/bin/dep

# Because of https://github.com/docker/docker/issues/14914
ENV PATH=$PATH:$GOROOT/bin:$GOPATH/bin

WORKDIR /gopath/src/github.com/pwillie/oidc-kubeconfig-helper
ADD . /gopath/src/github.com/pwillie/oidc-kubeconfig-helper

RUN make get-deps && make build-alpine

# Final Stage (pwillie/oidc-kubeconfig-helper)
FROM alpine:3.7

ARG GIT_COMMIT
ARG VERSION
LABEL REPO="https://github.com/pwillie/oidc-kubeconfig-helper"
LABEL GIT_COMMIT=$GIT_COMMIT
LABEL VERSION=$VERSION

# Because of https://github.com/docker/docker/issues/14914
ENV PATH=$PATH:/opt/oidc-kubeconfig-helper/bin

RUN apk add -U -q --no-progress ca-certificates

WORKDIR /opt/oidc-kubeconfig-helper/bin

COPY --from=build-stage /gopath/src/github.com/pwillie/oidc-kubeconfig-helper/bin/oidc-kubeconfig-helper /opt/oidc-kubeconfig-helper/bin/
RUN chmod +x /opt/oidc-kubeconfig-helper/bin/oidc-kubeconfig-helper

ENTRYPOINT [ "/opt/oidc-kubeconfig-helper/bin/oidc-kubeconfig-helper" ] 
