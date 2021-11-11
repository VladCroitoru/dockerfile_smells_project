FROM centos:centos6
MAINTAINER Amit Bakshi <ambakshi@gmail.com>

RUN yum update -y
RUN yum groupinstall -y 'Development tools'
RUN yum install -y ruby ruby-devel rubygems rubygems-devel
RUN yum install -y tar hg bzr
RUN gem install --no-rdoc --no-ri fpm

ENV PATH /usr/local/go/bin:$PATH
ENV GOVERSION 1.3.3

RUN mkdir -p /usr/local/go
RUN curl -sSL https://storage.googleapis.com/golang/go${GOVERSION}.src.tar.gz | tar zxf - --strip-components 1 -C /usr/local/go

## This is 1.3.3 specific to fix sync.Pool leak
RUN cd /usr/local/go/src/pkg && curl -sSL https://codereview.appspot.com/download/issue162980043_100001.diff | patch -p2
##

RUN cd /usr/local/go/src && for GOOS in linux darwin; do GOOS=$GOOS GOARCH=amd64 ./make.bash --no-clean; done
RUN ln -sfn /usr/local/go/bin/go /usr/local/bin && ln -sfn /usr/local/go/bin/gofmt /usr/local/bin

ENV GOPATH /usr/local
RUN for tool in \
    code.google.com/p/go.tools/cmd/benchcmp \
    code.google.com/p/go.tools/cmd/cover \
    code.google.com/p/go.tools/cmd/eg \
    code.google.com/p/go.tools/cmd/godex \
    code.google.com/p/go.tools/cmd/godoc \
    code.google.com/p/go.tools/cmd/goimports \
    code.google.com/p/go.tools/cmd/gotype \
    code.google.com/p/go.tools/cmd/oracle \
    code.google.com/p/go.tools/cmd/present \
    code.google.com/p/go.tools/cmd/ssadump \
    code.google.com/p/go.tools/cmd/vet \
    code.google.com/p/go.tools/cmd/gorename \
    code.google.com/p/rog-go/exp/cmd/godef \
    github.com/golang/lint/golint \
    github.com/kisielk/errcheck \
    github.com/jstemmer/gotags \ 
    github.com/nsf/gocode ; do \
        echo "Installing $tool ..."; go get $tool; done

WORKDIR /tmp
ENV BUILD_VERSION 1
RUN fpm -s dir -t rpm -n golang -v $GOVERSION --iteration $BUILD_VERSION \
    --description "The Go Programming Language" \
    --url http://golang.org --license BSD \
    -a x86_64 --provides golang \
    /usr/local/go /usr/local/bin
CMD /bin/sh -c "mountpoint -q /target && chown `stat --printf '%u:%g' /target` *.rpm && mv *.rpm /target"
