FROM gliderlabs/alpine:latest
# MAINTAINER Anthony Rawlins <anthony.rawlins@unimelb.edu.au>
RUN apk add --update python3 py-pip && pip3 install mkdocs && rm -rf /var/cache/apk/*
RUN pip3 install mkdocs-material typing
ADD VERSION .
RUN mkdir /documents
COPY documents /documents
WORKDIR /documents
EXPOSE 8800
ENTRYPOINT ["mkdocs"]
