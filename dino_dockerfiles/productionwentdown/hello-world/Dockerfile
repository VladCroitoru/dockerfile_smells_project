FROM golang:1.10-alpine as build

# args
ARG version="1.0.1"
ARG repo="github.com/productionwentdown/hello-world"

# source
WORKDIR $GOPATH/src/${repo}
COPY . .

# build
ENV CGO_ENABLED=0
ENV GOOS=linux
ENV GOARCH=amd64
RUN go build -ldflags "-s -w" -o /hello-world


FROM scratch

ARG version

# labels
LABEL org.label-schema.vcs-url="https://github.com/productionwentdown/hello-world"
LABEL org.label-schema.version=${version}
LABEL org.label-schema.schema-version="1.0"

# copy binary
COPY --from=build /hello-world /hello-world

EXPOSE 8080

ENTRYPOINT ["/hello-world"]
