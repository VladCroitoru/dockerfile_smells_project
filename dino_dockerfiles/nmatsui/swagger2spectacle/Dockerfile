FROM node:8.11-alpine
MAINTAINER Nobuyuki Matsui <nobuyuki.matsui@gmail.com>

WORKDIR /opt
COPY entrypoint.sh /opt/entrypoint.sh
RUN apk update && apk upgrade && \
    apk add --no-cache --virtual .build git && \
    git clone https://github.com/sourcey/spectacle.git /opt/spectacle && \
    cd /opt/spectacle && \
    npm install && \
    cd /opt && \
    npm install inline-source-cli && \
    apk del .build && \
    chmod 755 /opt/entrypoint.sh

ENTRYPOINT ["/opt/entrypoint.sh"]

# entrypoint.sh is like below:
# #!/bin/sh
# 
# if [ $# -ne 1 ]; then
#   echo "usage: docker run --rm --volume \$(pwd):/mnt nmatsui/swagger2spectacle swagger_filename.yaml"
#   exit 1
# fi
# 
# YAML_FILE=${1}
# BASE_NAME=${YAML_FILE%.*}
# 
# if [ ! -e /mnt/${YAML_FILE} ]; then
#   echo "${YAML_FILE} not found"
#   exit 1
# fi
# 
# node /opt/spectacle/bin/spectacle.js -t . /mnt/${YAML_FILE}
# sed -i -e 's#<link rel="stylesheet" href="stylesheets/foundation.min.css" />#<link inline rel="stylesheet" href="stylesheets/foundation.min.css" />#' /opt/index.html
# sed -i -e 's#<link rel="stylesheet" href="stylesheets/spectacle.min.css" />#<link inline rel="stylesheet" href="stylesheets/spectacle.min.css" />#' /opt/index.html
# sed -i -e 's#<script src="javascripts/spectacle.min.js"></script>#<script inline src="javascripts/spectacle.min.js"></script>#' /opt/index.html
# /opt/node_modules/.bin/inline-source --compress false index.html > /mnt/${BASE_NAME}.html
# 
# exit 0
