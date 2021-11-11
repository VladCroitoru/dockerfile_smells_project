FROM nasoym/bash_socat_server
MAINTAINER Sinan Goo

RUN apk --no-cache add html-xml-utils
RUN apk --no-cache add curl

RUN rm -rf /handlers; mkdir /handlers
ADD search /handlers/search

