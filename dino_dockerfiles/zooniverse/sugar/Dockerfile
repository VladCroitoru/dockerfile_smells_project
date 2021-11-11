FROM node:10-slim

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /node_app

COPY package.json /node_app/
COPY package-lock.json /node_app/
RUN npm install .

COPY . /node_app

EXPOSE 2999

CMD ["/node_app/docker/start.sh"]