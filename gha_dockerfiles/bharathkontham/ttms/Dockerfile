FROM node:10
## Add the wait script to the image
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait
WORKDIR /opt/bussrapp
COPY ./package.json ./
RUN npm install
COPY ./ ./
EXPOSE 4444
CMD [ "node", "server/server.js" ]
