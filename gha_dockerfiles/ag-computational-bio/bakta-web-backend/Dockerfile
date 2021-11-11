FROM alpine:latest as certs
RUN apk --update add ca-certificates

FROM golang:latest as builder

RUN mkdir /BAKTA-Web-Backend
WORKDIR /BAKTA-Web-Backend
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -ldflags '-extldflags "-static"' -o BaktaBackend .

FROM scratch
ARG GITHUB_SHA
ENV GITHUB_SHA=$GITHUB_SHA
COPY --from=certs /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /BAKTA-Web-Backend/BaktaBackend .

ENTRYPOINT [ "/BaktaBackend" ]