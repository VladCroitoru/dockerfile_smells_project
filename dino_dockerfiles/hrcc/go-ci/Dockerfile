FROM golang:latest
LABEL maintainer="HRcc"

RUN curl -fsSL https://goss.rocks/install | sh

RUN wget https://github.com/golang/dep/releases/download/v0.3.2/dep-linux-amd64 -O /go/bin/dep \
    && chmod +x /go/bin/dep

RUN go get github.com/mattn/goveralls
RUN go get golang.org/x/tools/cmd/cover
RUN go get github.com/onsi/ginkgo/ginkgo
RUN go get github.com/onsi/gomega  
RUN go get github.com/golang/lint/golint
RUN go get github.com/tmthrgd/go-bindata/...

COPY ./config/bitbucket-pipelines-go.sh /bitbucket-pipelines-go.sh
RUN chmod +x /bitbucket-pipelines-go.sh
        