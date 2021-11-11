FROM golang:1.9 as build
WORKDIR $GOPATH/src/github.com/logicmonitor/chart-uploader
COPY ./ ./
ARG VERSION
RUN go get \
    && GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -o /chart-uploader -ldflags "-X \"github.com/logicmonitor/k8s-chart-uploader/pkg/constants.Version=${VERSION}\""

FROM golang:1.9 as helm
ENV HELM_VERSION="v2.6.1"
RUN curl -L https://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz | tar -xz -C /tmp

FROM golang:1.9 as test
ARG CI
ENV CI=$CI
WORKDIR $GOPATH/src/github.com/logicmonitor/chart-uploader
RUN go get -u github.com/alecthomas/gometalinter
RUN gometalinter --install
COPY --from=build $GOPATH $GOPATH
RUN chmod +x ./scripts/test.sh; sync; ./scripts/test.sh
RUN cp coverage.txt /coverage.txt

FROM alpine:3.6
LABEL maintainer="Jeff Wozniak <jeff.wozniak@logicmonitor.com>"

RUN apk --update add ca-certificates \
    && rm -rf /var/cache/apk/* \
    && rm -rf /var/lib/apk/*

WORKDIR /charts
COPY --from=build /chart-uploader /bin
COPY --from=helm /tmp/linux-amd64/helm /usr/local/bin/helm
COPY --from=test /coverage.txt /coverage.txt
RUN chmod +x /usr/local/bin/*

ENTRYPOINT ["chart-uploader"]
