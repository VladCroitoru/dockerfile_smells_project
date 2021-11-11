FROM golang:1.6.2
RUN mkdir -p /go/src/github.com/aacebedo \
 && cd /go/src/github.com/aacebedo \
 && git clone https://github.com/aacebedo/dnsdock.git \
 && cd dnsdock \
 && go get -v github.com/tools/godep \
 && godep restore \
 && cd src \
 && go build -o /go/bin/dnsdock -ldflags "-X main.version=$(git describe --tags HEAD)$(if [ -n "$(command git status --porcelain --untracked-files=no 2>/dev/null)" ]; then echo "-dirty"; fi)"
ENTRYPOINT ["/go/bin/dnsdock"]
