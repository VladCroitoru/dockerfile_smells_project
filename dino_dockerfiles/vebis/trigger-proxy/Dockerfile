FROM golang:1.14 as builder
WORKDIR /src/
COPY ./*.go /src/
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

FROM scratch
LABEL maintainer="Stephan Kirsten <vebis@gmx.net>"
LABEL description="trigger-proxy docker container"
LABEL org.opencontainers.image.source="https://github.com/vebis/trigger-proxy"
WORKDIR /root/
COPY --from=builder /src/app .
COPY ./examples/example.csv mapping.csv
CMD [ "./app" ]
