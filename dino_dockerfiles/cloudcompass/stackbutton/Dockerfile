FROM node:4.4.3-wheezy

# Sails setup
WORKDIR /app/
ADD package.json /app/
ADD Gruntfile.js /app/
RUN npm install npm -g && npm install
ADD . .
RUN ./node_modules/.bin/grunt buildProd

RUN adduser --system devex && chown -R devex:0 . && chmod -R 770 .

USER devex

VOLUME ["/app/api", "/app/assets", "/app/config", "app/tasks", "app/views"]

EXPOSE 1337

ENV sails_hooks__grunt=false NODE_ENV=production SB_WEBHOOK_BASE_URL=http://www.stackbutton.com

CMD ["node","app.js"]
