FROM alpine:3.4

#Compile first externally
# CC=$(which musl-gcc) go build --ldflags '-w -linkmode external -extldflags "-static"' server.go
ADD server /

ENTRYPOINT ["/server"]
  
