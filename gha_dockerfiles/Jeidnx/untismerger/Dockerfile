FROM node:latest

WORKDIR /untismerger
COPY . /untismerger/
RUN npm install
EXPOSE 8080

ENTRYPOINT [ "node", "index.js" ]

