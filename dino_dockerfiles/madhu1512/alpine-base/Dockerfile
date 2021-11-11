FROM alpine:latest

# Update image and install base packages
RUN apk update && \
    apk upgrade && \
    apk add bash curl nodejs openssl python-dev py-pip gcc musl-dev openldap-dev && \
    rm -rf /var/cache/apk/*
