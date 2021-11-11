FROM node:10.16.3
EXPOSE 8888
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

RUN npm prune && npm install

RUN /usr/src/app/node_modules/rolehaven/start.sh
CMD ["npm", "start"]
