FROM golang:1.17-alpine as builder
RUN apk add --no-cache git make curl
ENV GOOS=linux
ENV CGO_ENABLED=0
COPY . /src
WORKDIR /src
RUN make kubebuilder
RUN make test
RUN make alpine

FROM alpine:3.14
RUN apk add --no-cache ca-certificates git curl
RUN curl -L -f https://github.com/mikefarah/yq/releases/download/2.4.1/yq_linux_amd64 > /usr/local/bin/yq && chmod +x /usr/local/bin/yq
RUN export PATH=$PATH:/app
WORKDIR /app
COPY --from=builder /src/bin/hookd /app/hookd
COPY --from=builder /src/bin/deployd /app/deployd
COPY --from=builder /src/bin/deploy /app/deploy
COPY --from=builder /src/bin/provision /app/provision
