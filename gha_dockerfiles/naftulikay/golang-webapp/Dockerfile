FROM golang:1.16 as build
MAINTAINER Naftuli Kay <me@naftuli.wtf>

WORKDIR /usr/src/app

# install tools early
RUN go get -u github.com/google/wire/cmd/wire && \
    go get -u github.com/swaggo/swag/cmd/swag

# download modules
COPY Makefile go.mod go.sum ./
RUN make download

# lots of seemingly redundant but not unrequired steps, not an issue at download time due to separate build image
# even with a good .dockerignore, `COPY . .` forces a rebuild every time
COPY main.go ./
COPY cmd/ /usr/src/app/cmd/
COPY pkg/ /usr/src/app/pkg/

# generate code
RUN make generate

# build the application
RUN CGO_ENABLED=0 GOOS=linux go build -o ./api && \
    cp ./api ./api.debug && \
    strip ./api

# copy the binary to an alpine image

# in an ideal world, we could use FROM scratch, but if the underlying application needs to communicate with _anything_
# using TLS, no certificate authorities, and indeed absolutely nothing will be present in the image at runtime, so it
# absolutely won't work unless a) you copy certificate authorities in yourself or b) if you somehow compile certificate
# authorities into your binary
FROM alpine:latest

COPY --from=build /usr/src/app/api /
COPY --from=build /usr/src/app/api.debug /

# default to dev environment
ENV ENV=dev

EXPOSE 8080

ENTRYPOINT ["/api"]
CMD ["serve"]