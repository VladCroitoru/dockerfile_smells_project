FROM alpine
MAINTAINER Octoblu Inc. <serveradmin@octoblu.com>

RUN apk add --no-cache apache2-utils bash curl grep pv

WORKDIR /usr/src/app
COPY ./script.sh script.sh

CMD ["/bin/bash"]
