FROM alpine

MAINTAINER Matthias Pall Gissurarson <mpg@mpg.is>

ENV VERSION 0.4.1

ADD https://releases.hashicorp.com/vault/${VERSION}/vault_${VERSION}_linux_amd64.zip /tmp/
ADD https://releases.hashicorp.com/vault/${VERSION}/vault_${VERSION}_SHA256SUMS      /tmp/
ADD https://releases.hashicorp.com/vault/${VERSION}/vault_${VERSION}_SHA256SUMS.sig  /tmp/

WORKDIR /tmp/

# Verify the sig with hashicorps public key (0x348FFC4C)
RUN apk --update add --virtual verify gpgme \
 && gpg --keyserver pgp.mit.edu --recv-key 0x348FFC4C \
 && gpg --verify /tmp/vault_${VERSION}_SHA256SUMS.sig \
 && apk del verify \
 && cat vault_${VERSION}_SHA256SUMS | grep linux_amd64 | sha256sum -c \
 && unzip vault_${VERSION}_linux_amd64.zip \
 && mv vault /usr/bin/ \
 && rm -rf /tmp/* \
 && rm -rf /var/cache/apk/*

WORKDIR /

EXPOSE 8200


ENTRYPOINT ["vault"]
CMD ["server", "-dev"]
