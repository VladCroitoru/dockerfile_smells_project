FROM node:alpine
LABEL maintainer="Gary A. Stafford <garystafford@rochester.rr.com>"
ENV REFRESHED_AT 2017-11-21

RUN set -x \
  && apk update \
  && apk upgrade \
  && apk add git unzip

RUN mkdir client \
  && git clone --depth 1 --branch build-artifacts \
      "https://github.com/garystafford/voter-client.git" client \
  && cd client \
  && ls -ah \
  && pwd \
  && unzip *.zip

WORKDIR /client/dist
ENV NODE_ENV=production
RUN npm install --production
EXPOSE 8080

CMD [ "node", "server.js" ]
