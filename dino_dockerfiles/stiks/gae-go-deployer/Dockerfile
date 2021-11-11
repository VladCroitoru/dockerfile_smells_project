FROM getsentry/sentry-cli AS sentry-build

FROM google/cloud-sdk:alpine

MAINTAINER Kirill Garbar <kirill@iterium.co.uk>

RUN apk --update upgrade \
    && apk add go ca-certificates \
    && rm /var/cache/apk/*

ENV GOROOT /usr/lib/go
ENV GOPATH /go
ENV GOBIN /go/bin
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin

COPY --from=sentry-build /bin/sentry-cli /bin

RUN gcloud config set core/disable_usage_reporting true && \
    gcloud config set component_manager/disable_update_check true && \
    gcloud components install app-engine-go --quiet
