FROM golang:1.5.1
ENV GO15VENDOREXPERIMENT 1
RUN go-wrapper download github.com/tools/godep
RUN cd /go/src/github.com/tools/godep && go-wrapper install
RUN ln -s /go/bin/godep /usr/local/bin/godep
WORKDIR /go/src/app
ENV BINARY app
ENV CG0_ENABLED 0
ENV GOOS linux
CMD [ "/bin/bash" , "-c" , "godep get || true && godep restore && godep go build --ldflags '-extldflags \"-static\"' -o ${BINARY}"]
