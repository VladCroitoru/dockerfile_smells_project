FROM golang:latest
MAINTAINER cblomart@gmail.com

# install nodejs
RUN curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -;\
    echo 'deb http://deb.nodesource.com/node_10.x stretch main' > /etc/apt/sources.list.d/nodesource.list;\
    apt-get update && apt-get install -y\
    nodejs\
    xz-utils\
    jq\
    musl\
    musl-tools &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#install last version of upx
RUN export UPX_VERSION=$(curl -sf "https://api.github.com/repos/upx/upx/releases/latest" | jq -r .tag_name | grep -o "[.0-9]*") \
    && UPX_URL="https://github.com/upx/upx/releases/download/v${UPX_VERSION}/upx-${UPX_VERSION}-amd64_linux.tar.xz" \
    && echo UPX URL: $UPX_URL \
    && curl -SsfL $UPX_URL | tar -C /tmp -Jxf - \
    && mv /tmp/upx-${UPX_VERSION}-amd64_linux/upx /usr/local/bin/ \
    && rm -rf /tmp/upx-${UPX_VERSION}-amd64_linux

# install the latest version of staticcheck
RUN export STATICCHECK_VERSION=$(curl -sf "https://api.github.com/repos/dominikh/go-tools/releases/latest" | jq -r .tag_name) \
    && STATICCHECK_URL="https://github.com/dominikh/go-tools/releases/download/${STATICCHECK_VERSION}/staticcheck_linux_amd64.tar.gz" \
    && echo STATICCHECK URL: $STATICCHECK_URL \
    && curl -SsfL $STATICCHECK_URL | tar -C /tmp -zxf - \
    && mv /tmp/staticcheck/staticcheck /usr/local/bin/ \
    && chmod +x /usr/local/bin/staticcheck \
    && upx -qq --best --lzma /usr/local/bin/staticcheck

# install golang checkers
RUN export CGO=0;\
    go get -ldflags '-s -w' -a github.com/cblomart/git-version;\
    go get -ldflags '-s -w' -a golang.org/x/lint/golint;\
    go get -ldflags '-s -w' -a github.com/gordonklaus/ineffassign;\
    go get -ldflags '-s -w' -a github.com/securego/gosec/cmd/gosec/...;\
    go get -ldflags '-s -w' -a github.com/dave/courtney;\
    go get -ldflags '-s -w' -a gitlab.com/opennota/check/cmd/aligncheck;\
    go get -ldflags '-s -w' -a gitlab.com/opennota/check/cmd/structcheck;\
    go get -ldflags '-s -w' -a gitlab.com/opennota/check/cmd/varcheck;\
    go get -ldflags '-s -w' -a github.com/mgechev/revive;\
    go get -ldflags '-s -w' -a github.com/fzipp/gocyclo/cmd/gocyclo;\
    upx -qq --best --lzma ./bin/git-version;\
    upx -qq --best --lzma ./bin/golint;\
    upx -qq --best --lzma ./bin/ineffassign;\
    upx -qq --best --lzma ./bin/gosec;\
    upx -qq --best --lzma ./bin/courtney;\
    upx -qq --best --lzma ./bin/aligncheck;\
    upx -qq --best --lzma ./bin/structcheck;\
    upx -qq --best --lzma ./bin/varcheck;\
    upx -qq --best --lzma ./bin/revive;\
    upx -qq --best --lzma ./bin/gocyclo;\
    cp ./bin/* /usr/local/bin/;\
    rm -rf ./*

# Install Docker
RUN export DOCKER_VERSION=$(curl -sf https://download.docker.com/linux/static/stable/x86_64/ | egrep -o -e 'docker-[.0-9]*(-ce)?\.tgz' | sort -r | head -n 1) \
  && DOCKER_URL="https://download.docker.com/linux/static/stable/x86_64/${DOCKER_VERSION}" \
  && echo Docker URL: $DOCKER_URL \
  && curl -Ssf $DOCKER_URL | tar -C /tmp -zxf  - \
  && mv /tmp/docker/docker /usr/local/bin/ \
  && upx -qq --best --lzma /usr/local/bin/docker \
  && which docker \
  && (docker version || true)

# codeclimate cover reporter
ADD https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64 /usr/local/bin/test-reporter

# install minio
RUN wget -q https://dl.minio.io/client/mc/release/linux-amd64/mc -O /usr/local/bin/mc \
    && chmod 777 /usr/local/bin/mc \
    && upx -qq --best --lzma /usr/local/bin/mc
