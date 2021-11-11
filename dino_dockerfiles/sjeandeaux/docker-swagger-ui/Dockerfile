FROM node:0.10

MAINTAINER Stéphane Jeandeaux <stephane.jeandeaux@gmail.com>

RUN npm update npm &&\
    npm install http-server replace


RUN mkdir -p /tmp/swagger
ADD https://github.com/swagger-api/swagger-ui/archive/master.tar.gz /tmp/swagger/swaggerui.tar.gz
RUN tar --strip-components 1 -C /tmp/swagger -xzf /tmp/swagger/swaggerui.tar.gz 

RUN mkdir -p /swaggerui/dist/swagger-ui &&\
    mv /tmp/swagger/dist/* /swaggerui/dist/swagger-ui &&\
    rm -rf /tmp/swagger

ENV API_URL http://petstore.swagger.io/v2/swagger.json 

RUN echo "'use strict';\
var path = require('path');\
var createServer = require('http-server').createServer;\
var dist = path.join('swaggerui', 'dist');\
var replace = require('replace');\
replace({regex: 'http.*swagger.json', replacement : process.env.API_URL, paths: ['/swaggerui/dist/swagger-ui/index.html'], recursive:false, silent:true,});\
var swaggerUI = createServer({ root: dist, cors: true });\
swaggerUI.listen(8888);" > /swaggerui/index.js

EXPOSE 8888
CMD ["node", "/swaggerui/index.js"]
