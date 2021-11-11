FROM sorccu/adb:latest

ENV PACKAGES="\
  git \
  python \
  #python2-dev \
  py-pip \
  py-matplotlib \
  python3 \
  #freetype-dev \
"


RUN apk update

RUN echo \
  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" > /etc/apk/repositories \
  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
  && echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories

RUN apk add --no-cache $PACKAGES || \
  (sed -i -e 's/dl-cdn/dl-4/g' /etc/apk/repositories && apk add --no-cache $PACKAGES)

RUN pip install --upgrade pip

RUN pip install androidviewclient
