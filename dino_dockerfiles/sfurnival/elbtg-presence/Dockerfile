FROM node:6-alpine
MAINTAINER "Stephen Furnival" <sfurnival@gmail.com>

RUN mkdir -p /opt/elbtg-presence/
WORKDIR /opt/elbtg-presence/
COPY . /opt/elbtg-presence/
RUN rm -rf node_modules
RUN npm set progress=false
RUN npm install --production

CMD ["node", "app.js"]