FROM alpine

RUN apk --no-cache add bash curl

COPY register-api register-apis update-api enable-plugin enable-plugins /usr/local/bin/

WORKDIR /usr/local/bin
