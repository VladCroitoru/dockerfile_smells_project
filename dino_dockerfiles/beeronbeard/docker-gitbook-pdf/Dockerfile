FROM node:slim

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/BeerOnBeard/docker-gitbook-pdf.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="1.0.0-rc1"

RUN apt-get update && \
    apt-get install -y calibre git && \
    npm install gitbook-cli -g && \
    gitbook fetch latest

ENV PDF_NAME Book.pdf

VOLUME ["/book", "/pdf"]

CMD cd /book && \
    gitbook install && \
    gitbook pdf /book /pdf/$PDF_NAME
