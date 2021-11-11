FROM alpine:3.4

MAINTAINER CenturyLink Labs <clt-labs-futuretech@centurylink.com>

RUN apk add --no-cache openssl
CMD ! test -e "${CERT_DIR:-/certs}/${KEY_FILE:-${KEY_NAME}.key}" -a -e "${CERT_DIR:-/certs}/${CRT_FILE:-${KEY_NAME}.crt}" && \
    /usr/bin/openssl genrsa -out "${CERT_DIR:-/certs}/${KEY_FILE:-${KEY_NAME}.key}" 2048 && \
    /usr/bin/openssl req  -new -sha256 -newkey rsa:4096 -days "${LIFETIME:-365}" -nodes -subj "/C=${COUNTRY_NAME}/ST=/L=/O=/CN=${COMMON_NAME}" -keyout "${CERT_DIR:-/certs}/${KEY_FILE:-${KEY_NAME}.key}" -out "${CERT_DIR:-/certs}/${KEY_FILE:-${KEY_NAME}}.csr"  && \
    /usr/bin/openssl x509 -req -days "${LIFETIME:-365}" -in "${CERT_DIR:-/certs}/${KEY_FILE:-${KEY_NAME}}.csr" -signkey "${CERT_DIR:-/certs}/${KEY_FILE:-${KEY_NAME}.key}" -out "${CERT_DIR:-/certs}/${CRT_FILE:-${KEY_NAME}.crt}"
