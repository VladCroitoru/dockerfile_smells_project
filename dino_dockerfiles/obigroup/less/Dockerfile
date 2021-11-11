# Build:
# docker build -t obigroup/less .
#
# Run: 
# docker run --rm -v `pwd`:/src -ti obigroup/less styles.less > styles.css

FROM node:latest
MAINTAINER Rony Dray <contact@obigroup.fr>
RUN npm install -g less

VOLUME ["/src"]
WORKDIR /src

ENTRYPOINT ["/usr/local/bin/lessc"]
