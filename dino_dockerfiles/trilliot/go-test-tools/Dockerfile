FROM golang

RUN curl -s https://glide.sh/get | sh && \
    go get -v -u honnef.co/go/tools/cmd/staticcheck && \
    go get -v -u github.com/golang/lint/golint && \
    go get -v -u honnef.co/go/tools/cmd/gosimple && \
    rm -r src/ pkg/
