# ################################################################
# DESC: Docker file to run Hashicorp Vault (vaultproject.io)
# ################################################################

FROM alpine:3.3
MAINTAINER Barry Martin <bobb.mrtn@gmail.com>

#Dockerize
RUN apk --update add wget ca-certificates
RUN update-ca-certificates
RUN wget --no-check-certificate https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-linux-amd64-v0.2.0.tar.gz
RUN tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.2.0.tar.gz

# Listener API tcp port
EXPOSE 8200
ADD vault /usr/local/bin/vault
ADD consul.tmpl /config/consul.tmpl
ADD start.sh /start.sh
RUN touch /var/log/vault_audit.log

ENTRYPOINT ["/start.sh"]
