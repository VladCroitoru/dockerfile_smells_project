FROM golang:1.17 as stage
WORKDIR /app
COPY . .
ENV CGO_ENABLED=0
WORKDIR /app/cmd/coffee
RUN go build -o coffee
RUN chmod +x coffee

FROM gcr.io/distroless/base
WORKDIR /
COPY --from=stage --chown=nonroot:nonroot /app/cmd/coffee/coffee .
USER nonroot
ENTRYPOINT [ "/coffee", "server" ]