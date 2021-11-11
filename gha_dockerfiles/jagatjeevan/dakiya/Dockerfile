FROM node:8.0
WORKDIR /app

EXPOSE 9001


RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
RUN echo "deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu precise/mongodb-org/3.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.4.list
RUN apt-get update && apt-get install -y mongodb-org-tools

ADD cloud /app/cloud
ADD build /app/build
ADD seed-data /app/seed-data
ADD index.js package.json seed.sh /app/

RUN cd /app && yarn install --production

ENTRYPOINT ["yarn", "serve"]
