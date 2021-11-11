FROM  golang

MAINTAINER Chanchai Junlouchai "neverlock@gmail.com"

RUN apt-get update && apt-get install -y vim && apt-get install -y vim-nox &&apt-get clean 
COPY vimrc /root/.vimrc
COPY vim-1 /root/.vim
RUN echo "alias ls='ls --color'" >> /root/.bashrc
RUN go get github.com/nsf/gocode
RUN go get github.com/alecthomas/gometalinter
RUN go get golang.org/x/tools/cmd/goimports
RUN go get golang.org/x/tools/cmd/guru
RUN go get golang.org/x/tools/cmd/gorename
RUN go get golang.org/x/lint/golint
RUN go get github.com/rogpeppe/godef
RUN go get github.com/kisielk/errcheck
RUN go get github.com/jstemmer/gotags
RUN go get github.com/klauspost/asmfmt/cmd/asmfmt
RUN go get github.com/fatih/motion
RUN go get github.com/fatih/gomodifytags
RUN go get github.com/zmb3/gogetdoc
RUN go get github.com/josharian/impl
RUN go get github.com/dominikh/go-tools/cmd/keyify

ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

WORKDIR $GOPATH

