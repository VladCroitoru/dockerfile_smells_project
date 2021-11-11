FROM ubuntu:16.04

RUN apt-get update \
 && apt-get -y install build-essential git unzip ruby ruby-dev vim \
        libxml2-dev libxslt-dev libcurl4-openssl-dev pkg-config libfontconfig1 \
        build-essential zlib1g-dev libssl-dev libreadline6-dev libyaml-dev \
        libsqlite3-dev cmake libxml2 zlibc zlib1g-dev openssl golang zip \
        libreadline6 sqlite3 curl wget jq ca-certificates file \
        iptables dnsutils uuid-runtime \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# install docker
RUN wget 'https://get.docker.com/builds/Linux/x86_64/docker-1.11.0.tgz' \
 && tar -zxf docker-1.11.0.tgz \
 && mv docker/* /usr/local/bin/. \
 && chmod u+x /usr/local/bin/docker*
RUN /usr/local/bin/docker --version

# install bosh-init
RUN wget 'https://s3.amazonaws.com/bosh-init-artifacts/bosh-init-0.0.94-linux-amd64' \
 && mv bosh-init-0.0.94-linux-amd64 /usr/local/bin/bosh-init \
 && chmod u+x /usr/local/bin/bosh-init

# install spiff
RUN wget 'https://github.com/cloudfoundry-incubator/spiff/releases/download/v1.0.7/spiff_linux_amd64.zip' \
 && unzip spiff_linux_amd64.zip \
 && mv spiff /usr/local/bin/spiff \
 && chmod u+x /usr/local/bin/spiff \
 && rm -f spiff_linux_amd64.zip

# install cf-cli
RUN wget -O cf-cli.tgz 'https://cli.run.pivotal.io/stable?release=linux64-binary&version=6.21.0&source=github-rel' \
 && tar -xzf cf-cli.tgz \
 && mv cf /usr/local/bin/cf \
 && chmod u+x /usr/local/bin/cf \
 && rm -f cf-cli.tgz

# install spruce
RUN wget 'https://github.com/geofffranks/spruce/releases/download/v1.7.0/spruce-linux-amd64' \
  && mv spruce-linux-amd64 /usr/local/bin/spruce \
  && chmod u+x /usr/local/bin/spruce

# install bosh-workspace
RUN gem install bundler --no-rdoc --no-ri
RUN gem install bosh_cli -v 1.3262.4.0 --no-rdoc --no-ri
RUN gem install bosh_cli_plugin_micro -v 1.3262.4.0 --no-rdoc --no-ri
RUN gem install bosh-workspace -v 0.9.13 --no-rdoc --no-ri
RUN gem install cf-uaac -v 3.3.0 --no-rdoc --no-ri
RUN gem install rake -v 10.5.0 --no-rdoc --no-ri
RUN gem install thor -v 0.19.1 --no-rdoc --no-ri
RUN gem install etcd -v 0.3.0 --no-rdoc --no-ri
RUN gem install mechanize -v 2.7.4 --no-rdoc --no-ri

# go env
ENV GOPATH=/gopath
ENV PATH=/gopath/bin:$PATH
ENV TERM=xterm

# install go packages
RUN go get golang.org/x/tools/cmd/goimports \
 && go get golang.org/x/tools/cmd/oracle \
 && go get golang.org/x/tools/cmd/gorename \
 && go get github.com/golang/lint/golint \
 && go get github.com/tools/godep \
 && go get github.com/jteeuwen/go-bindata/... \
 && go get github.com/stretchr/testify/assert \
 && go get github.com/onsi/ginkgo/ginkgo \
 && go get github.com/onsi/gomega \
 && go get github.com/mitchellh/gox
