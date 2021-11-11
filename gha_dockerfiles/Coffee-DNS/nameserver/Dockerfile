FROM golang:1.17 as stage
WORKDIR /app
COPY . .
ENV CGO_ENABLED=0
WORKDIR /app/cmd/nameserver
RUN go build -o nameserver
RUN chmod +x nameserver
WORKDIR /ns
RUN cp /app/cmd/nameserver/nameserver /ns/nameserver

FROM gcr.io/distroless/base
COPY --from=stage --chown=nonroot:nonroot /ns /ns
WORKDIR /ns
USER nonroot
ENTRYPOINT [ "/ns/nameserver", "server" ]