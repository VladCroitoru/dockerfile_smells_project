FROM alpine:3.4

RUN apk update && apk add --no-cache mysql-client wget unzip bash perl openssh

# Environment variables
ENV TERRAFORM_VERSION="0.6.16" \
    GLIBC_VERSION="2.23-r1"

# System preparation & terraform installation
RUN apk add --update wget ca-certificates unzip git bash m4 && \
    wget -q "https://github.com/andyshinn/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk" && \
    apk add --allow-untrusted glibc-${GLIBC_VERSION}.apk && \
    wget -q -O /terraform.zip "https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip" && \
    unzip /terraform.zip -d /bin && \
    apk del --purge wget ca-certificates unzip && \
    rm -rf /var/cache/apk/* /terraform.zip glibc-${GLIBC_VERSION}.apk
