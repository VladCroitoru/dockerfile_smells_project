FROM node:8.9

RUN git clone -b master https://github.com/antirek/number-archer.git /usr/src/number-archer

WORKDIR	/usr/src/number-archer

RUN npm install

CMD ["npm", "start"]