#
# Runs Hugo static site generator as a local server
#

FROM devopsdays/docker-hugo:v0.30.2
MAINTAINER Matt Stratton <matt.stratton@gmail.com>

WORKDIR /site
ENV VIRTUAL_HOST="http://docker.local:1313"

EXPOSE 1313

CMD hugo --renderToDisk=true --watch=true --bind="0.0.0.0" --baseURL="${VIRTUAL_HOST}" server /site
