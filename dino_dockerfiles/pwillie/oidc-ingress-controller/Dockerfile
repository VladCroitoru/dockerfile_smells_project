# Build Stage
FROM golang:1.9.2-alpine3.7 AS build-stage

LABEL app="build-oidc-ingress-controller"
LABEL REPO="https://github.com/pwillie/oidc-ingress-controller"

ENV GOROOT=/usr/local/go \
    GOPATH=/gopath \
    GOBIN=/gopath/bin \
    PROJPATH=/gopath/src/github.com/pwillie/oidc-ingress-controller

RUN apk add -U -q --no-progress build-base git
RUN wget -q https://github.com/golang/dep/releases/download/v0.3.2/dep-linux-amd64 -O /usr/local/bin/dep \
 && chmod +x /usr/local/bin/dep

# Because of https://github.com/docker/docker/issues/14914
ENV PATH=$PATH:$GOROOT/bin:$GOPATH/bin

WORKDIR /gopath/src/github.com/pwillie/oidc-ingress-controller
ADD . /gopath/src/github.com/pwillie/oidc-ingress-controller

RUN make get-deps && make build-alpine

# Final Stage (pwillie/oidc-ingress-controller)
FROM alpine:3.7

ARG GIT_COMMIT
ARG VERSION
LABEL REPO="https://github.com/pwillie/oidc-ingress-controller"
LABEL GIT_COMMIT=$GIT_COMMIT
LABEL VERSION=$VERSION

# Because of https://github.com/docker/docker/issues/14914
ENV PATH=$PATH:/opt/oidc-ingress-controller/bin

RUN apk add -U -q --no-progress ca-certificates

WORKDIR /opt/oidc-ingress-controller/bin

COPY --from=build-stage /gopath/src/github.com/pwillie/oidc-ingress-controller/bin/oidc-ingress-controller /opt/oidc-ingress-controller/bin/
RUN chmod +x /opt/oidc-ingress-controller/bin/oidc-ingress-controller

ENTRYPOINT [ "/opt/oidc-ingress-controller/bin/oidc-ingress-controller" ] 
