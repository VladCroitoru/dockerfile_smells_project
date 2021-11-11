FROM node:4.2.2
MAINTAINER sgrant

COPY . /src
RUN cd /src && npm install && npm run build

EXPOSE 8000

CMD ["node", "/src/server.js"]
