FROM node:alpine

RUN apk update && apk add openssl

WORKDIR /app

ADD package.json /app/

ADD src /app/src

RUN npm install -g . || true

EXPOSE 53/udp 80 8080 443 8443

ENTRYPOINT ["semi-transparent-proxy","--cacert","/ca/cert.pem","--cakey","/ca/key.pem"]
