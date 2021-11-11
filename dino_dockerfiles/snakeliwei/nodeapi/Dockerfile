FROM alpine
MAINTAINER Lyndon li <snakeliwei@gmail.com>
# install env
RUN apk add --update nodejs curl \
    && rm -rf /var/cache/apk/* \
    && mkdir /nodeapi
COPY . /nodeapi

RUN npm install -g nodemon \
    && cd /nodeapi \
    && npm install

WORKDIR /nodeapi
EXPOSE 1337

# Configure container to run as an executable
CMD ["nodemon","bin/www"]

