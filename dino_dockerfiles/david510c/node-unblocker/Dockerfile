FROM node:alpine

MAINTAINER David Chen <david@davidchen.blog>

RUN npm install --prefix unblocker -g https://github.com/david510c/nunblocker/tarball/master

WORKDIR /unblocker/lib/node_modules/nodeunblocker.com

EXPOSE 8080

CMD ["npm", "start"]
