# Builder

FROM golang:1.8 as builder
WORKDIR /go/src/github.com/smpio/default-http-backend/
COPY . .
RUN make


# Runner

FROM scratch
COPY --from=builder /go/src/github.com/smpio/default-http-backend/default-http-backend /
COPY /www /www
ENTRYPOINT ["/default-http-backend"]
