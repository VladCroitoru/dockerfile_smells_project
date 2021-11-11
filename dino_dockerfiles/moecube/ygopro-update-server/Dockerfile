FROM node

# 都是逼的
# RUN apt-get update
# RUN apt-get  -y --force-yes install vim

WORKDIR /usr/src/app
COPY package.json /usr/src/app
COPY package-lock.json /usr/src/app

RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN npm install

COPY . /usr/src/app
ENTRYPOINT npm start