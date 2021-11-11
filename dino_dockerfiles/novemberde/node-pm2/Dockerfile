FROM node:8.11.1

# Default NODE_ENV is production!
ENV NODE_ENV production

RUN npm install -g pm2 node-gyp

VOLUME /var/lib/node
VOLUME /root/.pm2

EXPOSE 80 443