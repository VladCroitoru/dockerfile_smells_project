#
# aws-kms-resource
#
FROM cgswong/aws:latest
MAINTAINER Shingo Omura <everpeace@gmail.com>

RUN apk -Uuv add --no-cache bash jq coreutils
RUN bash --version
RUN echo test-base64 | base64 | base64 --decode
RUN jq --version
RUN aws --version

COPY check      /opt/resource/check
COPY in         /opt/resource/in
COPY out        /opt/resource/out
COPY decrypt.sh /opt/resource/decrypt.sh

RUN chmod +x /opt/resource/out /opt/resource/in /opt/resource/check

WORKDIR /
