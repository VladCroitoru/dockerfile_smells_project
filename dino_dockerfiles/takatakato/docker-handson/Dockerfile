FROM alpine:3.5

ENV GOPATH=/go

WORKDIR /app
ADD app.go /app

RUN apk add --no-cache ca-certificates
RUN apk --no-cache add --virtual build-dependencies bash gcc musl-dev openssl go git \

    # Compile docker-webui 
    && go build app.go \
    && mv ./app /usr/bin/ \
    ##&& mv /go/bin/app /usr/bin/ \

    # Clean up
    && apk del --purge -r build-dependencies \
    && rm -rf /usr/local/go /usr/lib/go /golang.tar.gz /*.patch /go/pkg /go/bin \
        /go/src/golang.org

EXPOSE 80

ENTRYPOINT ["app"]
