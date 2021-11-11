FROM node

RUN mkdir -p /opt/hotscounters
WORKDIR /opt/hotscounters
EXPOSE 8080
RUN apt-get -qq update && \
    apt-get install -y ruby ruby-dev && \
    gem install sass && \
    npm install -g grunt
COPY package.json .
RUN npm install
COPY . .
RUN grunt build

CMD ["node", "server.js"]

