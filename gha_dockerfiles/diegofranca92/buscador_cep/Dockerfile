# Comando pra ser executado: docker-compose up --build -d
# Importante verificar os IPs hostname -I | pegar o primeiro
# https://haseebmajid.dev/blog/running-react-native-in-docker

FROM node:latest
LABEL version=1.2.1

ENV ADB_IP="192.168.1.3"
ENV REACT_NATIVE_PACKAGER_HOSTNAME="192.168.1.5"

EXPOSE 19000
EXPOSE 19001

RUN apt-get update && \
    apt-get install -y android-tools-adb
WORKDIR /app

COPY package.json yarn.lock app.json ./
RUN yarn --network-timeout 100000 && yarn install && npm install -y --global expo-cli 
CMD adb connect $ADB_IP && \
        yarn run android