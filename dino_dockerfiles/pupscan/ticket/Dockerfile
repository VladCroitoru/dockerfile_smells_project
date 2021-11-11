FROM kkarczmarczyk/node-yarn:latest
MAINTAINER thibaut.mottet@pupscan.fr

RUN yarn global add vue-http-server

WORKDIR /workspace
COPY . .
RUN yarn install
RUN yarn add --force node-sass #Fix problem node-sass not working during build phase
RUN yarn build

EXPOSE 8080

CMD http-server -g -c864000 -f / /workspace/dist