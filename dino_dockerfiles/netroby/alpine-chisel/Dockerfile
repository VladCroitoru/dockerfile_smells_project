FROM alpine
RUN apk update ; \
    apk add git go;\
	export GOPATH=/opt/go; \
	go get -v github.com/jpillora/chisel;\
	mv /opt/go/bin/chisel /bin/chisel;\
	apk del openssl ca-certificates libssh2 curl expat pcre git go;\
	rm -rf /opt/go ;\
	rm -rf /usr/lib/go;\
