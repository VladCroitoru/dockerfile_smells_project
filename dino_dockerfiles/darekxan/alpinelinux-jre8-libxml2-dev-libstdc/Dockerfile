# Extend minimal jeanblanchard/java:jre-8
FROM jeanblanchard/java:jre-8

MAINTAINER Dariusz Skrzypoń <dariusz.skrzypon@infakt.pl>

    # libxml2 libstdc++ needed for pdf2xml
RUN apk update && apk add libxml2 libstdc++ ghostscript && rm -rf /var/cache/apk/*
    # cleans package manager cache


