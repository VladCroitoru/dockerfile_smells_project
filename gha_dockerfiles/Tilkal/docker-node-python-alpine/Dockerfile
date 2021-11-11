FROM node:14-alpine

RUN apk --update --no-cache add curl bash build-base python3 docker zip git && \
  pip3 install --upgrade pip && \
  pip --no-cache-dir install awscli --upgrade && \
  npm install --global npm@latest

CMD ["/bin/sh"]
