FROM node:8.11-slim

RUN groupadd -r rocketchat \
&&  useradd -r -g rocketchat rocketchat \
&&  mkdir -p /app/uploads \
&&  chown rocketchat.rocketchat /app/uploads

VOLUME /app/uploads


WORKDIR /app

COPY /tmp/build/Rocket.Chat.tar.gz .
RUN tar czf Rocket.Chat.tar.gz bundle
RUN rm Rocket.Chat.tar.gz
RUN cd bundle/programs/server &&  npm install

USER rocketchat

WORKDIR /app/bundle

# needs a mongoinstance - defaults to container linking with alias 'db'
ENV DEPLOY_METHOD=docker-official \
    MONGO_URL=mongodb://db:27017/meteor \
    HOME=/tmp \
    PORT=3000 \
    ROOT_URL=http://localhost:3000 \
    Accounts_AvatarStorePath=/app/uploads

EXPOSE 3000

CMD ["node", "main.js"]