FROM jguyomard/hugo-builder:latest

ENV S3DEPLOY_VERSION 2.0.0

RUN curl -L https://github.com/bep/s3deploy/releases/download/v2.0.0/s3deploy_${S3DEPLOY_VERSION}_Linux-64bit.tar.gz | tar -xz && \
    mv s3deploy /usr/local/bin/s3deploy

