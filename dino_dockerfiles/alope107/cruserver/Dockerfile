FROM node:0.12.7

RUN \
  apt-get install git && \
  git clone https://github.com/MysteryCRU/CRUserver.git && \
  cd CRUserver && \
  npm install . && \
  export MONGO_URI=mongodb://capstone-class:capstone-2015-2016@ds049754.mongolab.com:49754/heroku_s75tvv20

CMD ["node", "/CRUserver/index.js"]