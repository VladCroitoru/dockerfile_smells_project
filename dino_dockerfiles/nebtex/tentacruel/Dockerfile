FROM node
RUN mkdir /dorman
ADD . /doorman

WORKDIR /doorman

RUN npm install
EXPOSE 8080
ENTRYPOINT [ "npm", "start" ]