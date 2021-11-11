FROM node:6.13.1

RUN apt update && apt install -y netcat
COPY . /ethereum-bridge
WORKDIR /ethereum-bridge
RUN npm install

ENTRYPOINT ["node", "bridge"]
