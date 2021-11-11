FROM golang:1.17 as stage
WORKDIR /app
COPY . .
ENV CGO_ENABLED=0
WORKDIR /app
RUN go build -o discovery
RUN chmod +x discovery

FROM gcr.io/distroless/base
COPY --from=stage --chown=nonroot:nonroot /app/discovery /discovery
USER nonroot
ENTRYPOINT [ "/discovery" ]