FROM gliderlabs/alpine:edge
ENTRYPOINT ["/bin/translator"]

COPY . /go/src/github.com/tetsusat/translator
RUN apk-install -t build-deps build-base go git mercurial \
        && cd /go/src/github.com/tetsusat/translator \
        && export GOPATH=/go \
        && go get \
        && go build -o /bin/translator \
        && cp -R playbooks / \
        && rm -rf /go \
        && apk del --purge build-deps
RUN apk-install ansible py2-pip \
        && pip install --upgrade paramiko \
