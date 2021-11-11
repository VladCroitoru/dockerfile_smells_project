FROM node
WORKDIR /home/www
COPY . .
RUN npm install
WORKDIR /home/www/app
RUN npm install && npm run build
WORKDIR /home/www
EXPOSE 80
VOLUME [ "/home/www/config.js" ]
CMD ["npm","start"]