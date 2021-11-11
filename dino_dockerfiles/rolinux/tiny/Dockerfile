# build container
FROM golang as builder

WORKDIR /go/src/tiny/

COPY tiny.go /go/src/tiny/

RUN CGO_ENABLED=0 go build -a -installsuffix cgo -o tiny .
RUN chmod +x tiny

# run container with app on top on scratch empty container
FROM scratch

COPY --from=builder /go/src/tiny/tiny /tiny

EXPOSE 8080

CMD ["/tiny"]
