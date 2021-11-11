FROM mhart/alpine-node
MAINTAINER wyvernnot <wyvernnot@gmail.com>
WORKDIR /src
COPY . .
RUN npm install
EXPOSE 3000
CMD ["node","server.js"]
