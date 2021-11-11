FROM alpine:latest

MAINTAINER Kalle M. Aagaard <docker@k-moeller.dk>

RUN apk add --no-cache poppler-utils

ENTRYPOINT ["/usr/bin/pdftotext"]

CMD ["-layout", "-", "-"] 
