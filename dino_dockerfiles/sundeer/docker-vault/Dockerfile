FROM progrium/busybox
MAINTAINER Stephane Jourdan <fasten@fastmail.fm>
ENV REFRESHED_AT 2016-01-28
ENV VAULT_VERSION 0.5.0

# x509 expects certs to be in this file only.
ADD https://raw.githubusercontent.com/bagder/ca-bundle/master/ca-bundle.crt /etc/ssl/certs/ca-certificates.crt

ADD https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip /tmp/vault.zip

ADD ./config /config/

RUN cd /bin && unzip /tmp/vault.zip && chmod +x /bin/vault && rm /tmp/vault.zip

EXPOSE 8200

ENTRYPOINT ["/bin/vault"]
