FROM node:lts
COPY . /AAAforREST
WORKDIR /AAAforREST
RUN npm install

ENTRYPOINT ["node","app/proxy.js"]
