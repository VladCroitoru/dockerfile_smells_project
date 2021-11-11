FROM node:7-alpine

WORKDIR /var/www/html

COPY $PWD/package.json /var/www/html/

RUN npm install --production

ADD $PWD/ /var/www/html

CMD if [ -e "package.json" ]; then \
      if [ ! -e "node_modules" ]; then \
        npm install; \
      fi; \
    fi; \
    npm start;