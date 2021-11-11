FROM golang:1.10-alpine as build

# args
ARG version="1.0.1"
ARG repo="github.com/productionwentdown/text-server"

# source
WORKDIR $GOPATH/src/${repo}
COPY . .

# build
ENV CGO_ENABLED=0
ENV GOOS=linux
ENV GOARCH=amd64
RUN go build -ldflags "-s -w" -o /text-server


FROM scratch

ARG version

# labels
LABEL org.label-schema.vcs-url="https://github.com/productionwentdown/text-server"
LABEL org.label-schema.version=${version}
LABEL org.label-schema.schema-version="1.0"

# copy binary
COPY --from=build /text-server /text-server

EXPOSE 8080

ENTRYPOINT ["/text-server"]
