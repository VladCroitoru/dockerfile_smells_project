FROM node:latest
MAINTAINER wailorman

RUN mkdir /max-crm
ADD . /max-crm
WORKDIR /max-crm
RUN npm install --production

EXPOSE 27017
EXPOSE 21080:21080

CMD ["node", "app.js"]
