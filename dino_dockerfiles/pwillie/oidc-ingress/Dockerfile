# Build Stage
FROM golang:1.9.2-alpine3.7 AS build-stage

LABEL app="build-oidc-ingress"
LABEL REPO="https://github.com/pwillie/oidc-ingress"

ENV GOROOT=/usr/local/go \
    GOPATH=/gopath \
    GOBIN=/gopath/bin \
    PROJPATH=/gopath/src/github.com/pwillie/oidc-ingress

RUN apk add -U -q --no-progress build-base git
RUN wget -q https://github.com/golang/dep/releases/download/v0.3.2/dep-linux-amd64 -O /usr/local/bin/dep \
 && chmod +x /usr/local/bin/dep

# Because of https://github.com/docker/docker/issues/14914
ENV PATH=$PATH:$GOROOT/bin:$GOPATH/bin

WORKDIR /gopath/src/github.com/pwillie/oidc-ingress
ADD . /gopath/src/github.com/pwillie/oidc-ingress

RUN make get-deps && make build-alpine

# Final Stage (pwillie/oidc-ingress)
FROM alpine:3.7

ARG GIT_COMMIT
ARG VERSION
LABEL REPO="https://github.com/pwillie/oidc-ingress"
LABEL GIT_COMMIT=$GIT_COMMIT
LABEL VERSION=$VERSION

# Because of https://github.com/docker/docker/issues/14914
ENV PATH=$PATH:/opt/oidc-ingress/bin

RUN apk add -U -q --no-progress ca-certificates

WORKDIR /opt/oidc-ingress/bin

COPY --from=build-stage /gopath/src/github.com/pwillie/oidc-ingress/bin/oidc-ingress /opt/oidc-ingress/bin/
RUN chmod +x /opt/oidc-ingress/bin/oidc-ingress

ENTRYPOINT [ "/opt/oidc-ingress/bin/oidc-ingress" ] 
