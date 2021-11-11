FROM golang:1.10

# Install vendoring tools
RUN go get -u github.com/Masterminds/glide
RUN go get -u github.com/golang/dep/cmd/dep
RUN go get -u github.com/kardianos/govendor
RUN go get -u github.com/tools/godep

# Install static analysis tools
RUN go get -u github.com/golang/lint/golint
RUN go get -u github.com/bradleyfalzon/apicompat/...
RUN go get -u honnef.co/go/tools/cmd/gosimple
RUN go get -u honnef.co/go/tools/cmd/staticcheck
RUN go get -u honnef.co/go/tools/cmd/unused
RUN go get -u mvdan.cc/unparam
RUN go get -u github.com/mdempsky/unconvert

# Program to detect if file is generated or not
RUN go get -u github.com/gopherci/isFileGenerated

# Script to detect vendor tool and install deps
COPY install-deps.sh /usr/local/bin/

# GopherCI supports installing apt packages, so prepare the apt indexes.
RUN apt-get update

# GopherCI shows the output of lsb_release
RUN apt-get install -y lsb-release

# Remove source code so we can clone into these directories if we happen
# to have fetched the tool and then receive a PR for it (we can't clone
# into a non-empty directory.)
RUN rm -rf $GOPATH/src/*

CMD ["sleep", "infinity"]
