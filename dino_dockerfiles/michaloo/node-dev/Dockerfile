# michaloo/node-dev
#
# VERSION               0.0.1

FROM michaloo/node

MAINTAINER Michal Raczka me@michaloo.net

RUN apt-get update -y \
    && apt-get install -y curl git gcc make build-essential python

RUN npm install -g grunt-cli bower gulp

ENTRYPOINT ["/bin/bash"]
