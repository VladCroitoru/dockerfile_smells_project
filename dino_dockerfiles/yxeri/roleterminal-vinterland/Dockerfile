FROM node:7.1.0
EXPOSE 8888
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

RUN npm prune && npm install

CMD [ "/usr/src/app/node_modules/roleHaven/start.sh" ]
