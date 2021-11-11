FROM node:alpine
MAINTAINER 0x002a@gmail.com
RUN apk --no-cache --update add tini
ENTRYPOINT ["/sbin/tini", "--"]
WORKDIR /usr/src/app
COPY ["index.js", "package.json", "/usr/src/app/"]
EXPOSE 8080
CMD ["npm", "start"]
