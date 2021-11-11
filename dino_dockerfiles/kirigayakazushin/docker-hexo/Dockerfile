FROM alpine:3.9
MAINTAINER justforlxz,<justforlxz@gmail.com>
RUN apk add --no-cache  \
                nodejs  \
                npm     \
                openssl \
                git     \
                openssh \
                gnupg

RUN npm install hexo-cli -g
RUN addgroup -g 1000 docker
RUN adduser -u 1000 -D -G docker docker
RUN mkdir /Hexo
RUN chown -R docker /Hexo
VOLUME /Hexo
WORKDIR /Hexo
USER docker
CMD ['/bin/bash']
