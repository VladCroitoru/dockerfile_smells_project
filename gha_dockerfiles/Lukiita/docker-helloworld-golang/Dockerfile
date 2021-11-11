FROM golang AS builder
WORKDIR /src
COPY hello-world.go .
RUN go build hello-world.go

FROM scratch
COPY --from=builder /src/hello-world .
CMD ["./hello-world"]
