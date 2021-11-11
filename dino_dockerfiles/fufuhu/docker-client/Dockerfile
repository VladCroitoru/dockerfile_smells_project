FROM alpine:latest AS builder
RUN apk add --no-cache curl
RUN curl -L -o /tmp/docker-17.09.1-ce.tgz https://download.docker.com/linux/static/stable/x86_64/docker-17.09.1-ce.tgz

FROM python:3-alpine
COPY --from=builder /tmp/docker-17.09.1-ce.tgz /tmp
RUN tar -xz -C /tmp -f /tmp/docker-17.09.1-ce.tgz && mv /tmp/docker/* /usr/bin && rm -rf /tmp/*
RUN pip install docker-compose