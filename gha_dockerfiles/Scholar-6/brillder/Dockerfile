FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install --yes curl
RUN curl --silent --location https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install --yes nodejs
    

WORKDIR /usr/frontend
COPY package.json ./
COPY package-lock.json ./
RUN npm install
COPY ./ ./

CMD ["npm", "start"]