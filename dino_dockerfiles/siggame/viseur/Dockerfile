FROM node:latest
LABEL maintainer=siggame@mst.edu

ADD . vis
WORKDIR vis

RUN npm install
RUN npm run bundle

EXPOSE 8080

CMD ["npm", "run", "start"]
