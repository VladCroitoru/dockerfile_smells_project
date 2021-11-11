FROM node:alpine

MAINTAINER Wilton Garcia <wiltonog@gmail.com>

RUN apk add --no-cache --virtual .build-deps build-base libffi-dev ruby ruby-dev git \
    && gem install sass compass --no-ri --no-rdoc \
    && apk del build-base libffi-dev ruby-dev \
    && rm -rf /var/cache/* /tmp/* \
    && npm install gulp -g \ 
    && npm install bower -g \
    && npm rebuild node-sass

WORKDIR /workspace    

RUN npm install

CMD ["gulp"]


