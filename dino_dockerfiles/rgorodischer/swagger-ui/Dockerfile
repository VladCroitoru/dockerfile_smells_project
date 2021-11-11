FROM node:0.10
MAINTAINER Roman Gorodyshcher "roman.gorodischer@gmail.com"

RUN npm update npm \
    && npm install http-server replace

RUN groupadd -r swagger \
    && useradd -r -g swagger swagger 

RUN mkdir -p /tmp/swagger /home/swagger/swaggerui/dist/swagger-ui \
    && wget -O /tmp/swagger/swagger.tar.gz https://github.com/swagger-api/swagger-ui/archive/master.tar.gz \
    && tar --strip-components 1 -C /tmp/swagger -xzf /tmp/swagger/swagger.tar.gz \
    && mv /tmp/swagger/dist/* /home/swagger/swaggerui/dist/swagger-ui \
    && rm -rf /tmp/swagger 

ENV API_URL http://petstore.swagger.io/v2/swagger.json
ENV TITLE swagger

COPY ./index.js /home/swagger/swaggerui/index.js

RUN chown -R swagger /home/swagger 
USER swagger
WORKDIR /home/swagger

EXPOSE 9090
CMD ["node", "./swaggerui/index.js"]
 

