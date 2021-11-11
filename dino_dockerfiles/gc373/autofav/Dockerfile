FROM node:8-slim

COPY nodefiles /autofav
WORKDIR /autofav
RUN npm i --production --no-progress \
    && npm cache clean -f

CMD ["node" , "autofav.js"]