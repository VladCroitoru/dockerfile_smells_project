FROM node

RUN npm install bitcore-mnemonic

RUN echo "var Mn = require('bitcore-mnemonic'); console.log(new Mn(Mn.Words.ENGLISH).toString());" \
    > /opt/12-words.js

CMD node /opt/12-words.js
