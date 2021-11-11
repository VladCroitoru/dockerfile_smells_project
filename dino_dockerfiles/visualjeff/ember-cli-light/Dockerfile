# Built using Docker 1.82
#
# To Build:
#   docker build --force-rm=true -t visualjeff/ember-cli-light:1.13.12 .
# To Run:
#   docker run -t -i -p 4200:4200 -p 35729:35729 visualjeff/ember-cli-light:latest /bin/bash
# 

FROM alpine:edge 
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories 
RUN apk update
RUN apk add --update bash wget git nodejs && rm -rf /var/cache/apk/*
RUN apk update
RUN apk upgrade
RUN npm install -g ember-cli@1.13.15 bower phantomjs
RUN npm cache clean && bower cache clean --allow-root
EXPOSE 4200 35729
WORKDIR /root
CMD ["bash"]
