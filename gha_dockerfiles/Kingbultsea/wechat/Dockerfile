FROM node:10-slim

WORKDIR /project

COPY . ./

RUN npm install --registry=https://registry.npm.taobao.org

ENV HOST 0.0.0.0
ENV PORT 8080

EXPOSE 81

CMD [ "npm", "run", "core2" ]
