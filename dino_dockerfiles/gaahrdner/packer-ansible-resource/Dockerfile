FROM alpine:3.6

ARG PACKER_VER=1.1.1
ENV USER ansible

RUN sed -i -e 's/v3\.6/edge/g' /etc/apk/repositories \ 
  && apk --no-cache add jq bash git ca-certificates openssh-client sed openssl ansible \
  && wget -O /tmp/packer.zip \
    "https://releases.hashicorp.com/packer/${PACKER_VER}/packer_${PACKER_VER}_linux_amd64.zip" \
  && unzip -o /tmp/packer.zip -d /usr/local/bin \
  && rm -f /tmp/packer.zip \
  && apk --no-network del openssl

ADD bin /opt/resource
