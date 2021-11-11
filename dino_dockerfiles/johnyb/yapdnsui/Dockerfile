FROM node:8-alpine
LABEL maintainer="Julian Bäume <julian@svg4all.de>"

WORKDIR /app/yapdnsui

ENTRYPOINT ["/app/yapdnsui/startup.sh"]
CMD ["start"]

EXPOSE 8080
VOLUME ["/app/yapdnsui/data"]

COPY . /tmp

RUN cd /tmp && yarn --cache-folder=/tmp/yarn-cache &&\
  yarn build &&\
  mkdir -p /app/yapdnsui &&\
  cp -r dist middleware bin startup.sh package.json yarn.lock /app/yapdnsui &&\
  chmod +x /app/yapdnsui/startup.sh &&\
  cd /app/yapdnsui &&\
  yarn --production --cache-folder=/tmp/yarn-cache &&\
  rm -rf /tmp/*
