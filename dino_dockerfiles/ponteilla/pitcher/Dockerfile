FROM golang:1.9
WORKDIR /go/src/github.com/ponteilla/pitcher
COPY . .
RUN make

FROM gcr.io/distroless/base
COPY --from=0 /go/bin/pitcher .
ENTRYPOINT ["/pitcher"]
