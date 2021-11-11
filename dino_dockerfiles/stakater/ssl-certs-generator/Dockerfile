FROM stakater/base-alpine:3.5

RUN apk --update add openssl

WORKDIR /certs

COPY generate-certs /usr/local/bin/generate-certs

CMD /usr/local/bin/generate-certs

VOLUME /certs
