FROM node:boron

RUN groupadd -r nodejs && useradd -m -r -g nodejs nodejs
RUN mkdir -p /home/nodejs/app
WORKDIR /home/nodejs/app

COPY app /home/nodejs/app
RUN npm install --production

EXPOSE 8080
USER nodejs

CMD ["npm", "start"]
