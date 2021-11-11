FROM golang:alpine

RUN sed -i -e 's/v3\.8/edge/g' /etc/apk/repositories
RUN apk update --update-cache
RUN apk add git nodejs-current yarn

COPY goget.sh /
RUN /goget.sh
RUN rm /goget.sh

COPY package.json /
RUN cd / && yarn install --no-lockfile
RUN rm /package.json
