FROM node:9.3.0

RUN mkdir -p /{yakbak,tapes} && npm install yakbak --save-dev

VOLUME /tapes

WORKDIR /yakba
COPY proxy.js proxy.js
EXPOSE 3000

ENTRYPOINT ["node", "proxy.js"]
