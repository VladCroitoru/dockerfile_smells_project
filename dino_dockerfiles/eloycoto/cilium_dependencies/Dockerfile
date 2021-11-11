FROM cilium/dependencies

ENV GOROOT /usr/local/go
ENV GOPATH /tmp/cilium-net-build
ENV PATH "$GOROOT/bin:/usr/local/clang+llvm/bin:$GOPATH/bin:$PATH"

RUN go get -u github.com/jteeuwen/go-bindata/...
