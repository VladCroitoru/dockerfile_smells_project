FROM node:7.9.0
MAINTAINER megane42

RUN git clone https://github.com/megane42/onidaku_fukuwarai.git /var/onidaku_fukuwarai
WORKDIR /var/onidaku_fukuwarai
RUN npm install

EXPOSE 3000

CMD node /var/onidaku_fukuwarai/server.js

# docker run -d -p 3000:3000 --name onidaku_fukuwarai megane42/onidaku_fukuwarai
