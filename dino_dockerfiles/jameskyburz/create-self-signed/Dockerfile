from alpine:3.9

label maintainer="James Kyburz james.kyburz@gmail.com"

ENV CERT_FILENAME cert.pem
ENV PRIVKEY_FILENAME privkey.key

run apk --no-cache add openssl

add ./src/create-certs .
add ./src/openssl.cnf .

run cat ./openssl.cnf >> /etc/ssl/openssl.cnf

cmd ./create-certs
