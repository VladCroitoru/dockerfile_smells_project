FROM node:0.12
MAINTAINER megane42

RUN git clone https://github.com/megane42/asedaku_fukuwarai.git /var/asedaku_fukuwarai
WORKDIR /var/asedaku_fukuwarai
RUN npm install

EXPOSE 3000

CMD node /var/asedaku_fukuwarai/server.js

# docker run -d --name asedaku_fukuwarai megane42/asedaku_fukuwarai