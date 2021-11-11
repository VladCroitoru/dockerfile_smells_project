FROM node:10-buster
RUN mkdir -p /usr/src/app
COPY package.json /usr/src/app
COPY package-lock.json /usr/src/app
WORKDIR /usr/src/app
RUN ["npm", "install"]
COPY . /usr/src/app
RUN ["npm", "run", "build"]
VOLUME /usr/src/app/data
ENTRYPOINT ["node", "build/dist/server.js"]
EXPOSE 8080
