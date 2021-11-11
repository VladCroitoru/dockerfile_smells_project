FROM node:14.16.1-alpine3.13

RUN apk update && apk add \
    g++ \
    make \
    nasm \
    git \
    libtool \
    autoconf \
    automake \
    libpng-dev \
    pkgconfig

WORKDIR /var/nftstore

COPY package*.json /var/nftstore/
RUN npm install

COPY ./ /var/nftstore/

VOLUME /var/nftstore/data

EXPOSE 1111

ENTRYPOINT ["npm", "start"]
