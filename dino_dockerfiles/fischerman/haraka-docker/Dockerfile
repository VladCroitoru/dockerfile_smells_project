FROM node:6.11.5

EXPOSE 25 587

RUN npm install -g Haraka@2.8.18 sqlite3 express
RUN haraka -i /haraka
WORKDIR /haraka
RUN npm i haraka-plugin-graph

ADD rcpt_to.mba.js plugins/

CMD ["haraka", "-c", "/haraka"]